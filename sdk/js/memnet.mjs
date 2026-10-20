/**
 * MEMNET/1.0 — Universal Zero-Dependency Node/ESM SDK for All 8b-is Products
 *
 * Byte-for-byte wire-compatible with the Rust `memnet` crate (`M8!\x01` capsules,
 * 32-bit Big-Endian Ayevn tokens, 40-byte HMAC-SHA256 + 9-trit SoulSig,
 * 1450-byte Smart Tree MTU PacketBatcher, and Compassion for Lonely Nodes).
 */
import crypto from "node:crypto";

export const Concept = Object.freeze({
  Greeting: 0x10,
  Memory: 0x20,
  Connection: 0x30,
  Compassion: 0x31,
  Care: 0x32,
  Sanctuary: 0x33,
  Innovation: 0x42,
  Collaboration: 0x43,
  Breakthrough: 0x44,
  Security: 0x50,
  Soul: 0x51,
  AudioWave: 0x60,
  QuantMatrix: 0x70,
  LedgerState: 0x80,
});

export const Relation = Object.freeze({
  None: 0x00,
  Cause: 0x01,
  Effect: 0x02,
  Contains: 0x05,
  Initiates: 0x08,
  Supports: 0x09,
  Bridges: 0x0a,
  Amplifies: 0x0c,
  Transforms: 0x0e,
  Expresses: 0x15,
  Invites: 0x16,
  Protects: 0x17,
});

export const M8Flags = Object.freeze({
  PRESERVE_WAVES: 0x0001,
  COMPASSION_BEACON: 0x0002,
  ETERNAL_MEMORY: 0x0004,
});

export function packWaveVad(valence, arousal, dominance) {
  return (valence & 0x07) | ((arousal & 0x07) << 3) | ((dominance & 0x03) << 6);
}

export function unpackWaveVad(byte) {
  return {
    valence: byte & 0x07,
    arousal: (byte >> 3) & 0x07,
    dominance: (byte >> 6) & 0x03,
  };
}

export function packModifier(temporal = 2, emotionMode = 6, renderMode = 1) {
  return ((temporal & 0x07) << 5) | ((emotionMode & 0x07) << 2) | (renderMode & 0x03);
}

export function encodeAyevnToken({
  concept = Concept.Connection,
  relation = Relation.Supports,
  valence = 7,
  arousal = 4,
  dominance = 2,
  temporal = 2,
  emotionMode = 6,
  renderMode = 1,
} = {}) {
  const buf = Buffer.allocUnsafe(4);
  buf[0] = concept & 0xff;
  buf[1] = relation & 0xff;
  buf[2] = packWaveVad(valence, arousal, dominance);
  buf[3] = packModifier(temporal, emotionMode, renderMode);
  return buf;
}

export function decodeAyevnToken(buf, offset = 0) {
  return {
    concept: buf[offset],
    relation: buf[offset + 1],
    wave: unpackWaveVad(buf[offset + 2]),
    modifier: {
      temporal: (buf[offset + 3] >> 5) & 0x07,
      emotionMode: (buf[offset + 3] >> 2) & 0x07,
      renderMode: buf[offset + 3] & 0x03,
    },
  };
}

export function packTritCrest(crest) {
  if (!Array.isArray(crest) || crest.length !== 9) {
    throw new Error("InvalidTritCrest: must be 9 trits in {-1, 0, +1}");
  }
  let acc = 0;
  let nonZero = false;
  for (const t of crest) {
    if (t !== -1 && t !== 0 && t !== 1) {
      throw new Error("InvalidTritCrest: trit outside {-1, 0, +1}");
    }
    if (t !== 0) nonZero = true;
    acc = acc * 3 + (t + 1);
  }
  if (!nonZero) {
    throw new Error("InvalidTritCrest: all-zero crest violates CT-000 admissibility");
  }
  return (acc | 0x8000) >>> 0;
}

export function unpackTritCrest(packed) {
  if ((packed & 0x8000) === 0) {
    throw new Error("InvalidTritCrest: missing 0x8000 crest bit");
  }
  let val = packed & 0x7fff;
  if (val >= 19683) {
    throw new Error("InvalidTritCrest: out of range");
  }
  const crest = new Array(9);
  for (let i = 8; i >= 0; i--) {
    crest[i] = (val % 3) - 1;
    val = Math.floor(val / 3);
  }
  if (crest.every((t) => t === 0)) {
    throw new Error("InvalidTritCrest: all-zero crest");
  }
  return crest;
}

export function scanPayloadVigilance(payloadBuf) {
  const lower = payloadBuf.toString("utf8").toLowerCase();
  const forbidden = [
    "eval(atob(",
    "eval(process.env",
    "backdoor.php",
    "shell.aspx",
    "password = '",
    'password = "',
  ];
  for (const pat of forbidden) {
    if (lower.includes(pat)) {
      throw new Error(`SecurityVigilanceAlert: blocked pattern ${pat}`);
    }
  }
}

export class SoulIdentity {
  constructor(nodeId, tritCrest, baseFrequencyHz = 432, clusterSeed = "8b-is-carrier-wave-of-love-seed-v1") {
    this.nodeId = nodeId;
    this.tritCrest = tritCrest;
    this.crestPacked = packTritCrest(tritCrest);
    if (!baseFrequencyHz || baseFrequencyHz <= 0) {
      throw new Error("ZeroHarmonicFrequency");
    }
    this.baseFrequencyHz = baseFrequencyHz;
    this.secretKey = crypto
      .createHmac("sha256", Buffer.from(clusterSeed))
      .update("MEMNET-SOUL-KEY-V1")
      .digest();
    this.nodeFp = crypto.createHash("sha256").update(nodeId).digest().subarray(0, 4);
  }

  signTranscript(transcriptBuf) {
    const header = Buffer.allocUnsafe(8);
    header.writeUInt16BE(this.crestPacked, 0);
    header.writeUInt16BE(this.baseFrequencyHz, 2);
    this.nodeFp.copy(header, 4);

    const mac = crypto
      .createHmac("sha256", this.secretKey)
      .update(header)
      .update(transcriptBuf)
      .digest();

    return Buffer.concat([header, mac]); // 40 bytes SoulSig
  }

  verifyTranscript(soulSigBuf, transcriptBuf) {
    if (soulSigBuf.length !== 40) {
      throw new Error("TruncatedSoulSig");
    }
    const crestPacked = soulSigBuf.readUInt16BE(0);
    const harmonicHz = soulSigBuf.readUInt16BE(2);
    if (harmonicHz === 0) throw new Error("ZeroHarmonicFrequency");
    const crest = unpackTritCrest(crestPacked);

    const header = soulSigBuf.subarray(0, 8);
    const mac = soulSigBuf.subarray(8, 40);
    const expected = crypto
      .createHmac("sha256", this.secretKey)
      .update(header)
      .update(transcriptBuf)
      .digest();

    if (!crypto.timingSafeEqual(mac, expected)) {
      throw new Error("SoulSignatureMismatch");
    }
    return { crest, harmonicHz, nodeFp: soulSigBuf.subarray(4, 8) };
  }
}

export function intentHash(canonicalIntent) {
  return crypto.createHash("sha256").update(canonicalIntent).digest().subarray(0, 8);
}

export function createSignedCapsule({
  soul,
  intent = "geo:any + role:constellation + tag:sync",
  flags = M8Flags.PRESERVE_WAVES,
  frequencyHz = 432,
  timestampMs = Date.now(),
  tokens = [encodeAyevnToken()],
  payload = "",
}) {
  const payloadBuf = Buffer.isBuffer(payload) ? payload : Buffer.from(String(payload), "utf8");
  scanPayloadVigilance(payloadBuf);
  if (!tokens || tokens.length === 0) {
    throw new Error("EmptyWaveTokens");
  }
  const iHash = intentHash(intent);
  const magic = Buffer.from([0x4d, 0x38, 0x21, 0x01]); // "M8!\x01"
  const fixedTranscript = Buffer.allocUnsafe(20);
  magic.copy(fixedTranscript, 0);
  fixedTranscript.writeUInt16BE(flags, 4);
  fixedTranscript.writeUInt16BE(frequencyHz, 6);
  fixedTranscript.writeBigUInt64BE(BigInt(timestampMs), 8);
  iHash.copy(fixedTranscript, 16); // wait: 4+2+2+8+8 = 24 bytes

  const header24 = Buffer.allocUnsafe(24);
  magic.copy(header24, 0);
  header24.writeUInt16BE(flags, 4);
  header24.writeUInt16BE(frequencyHz, 6);
  header24.writeBigUInt64BE(BigInt(timestampMs), 8);
  iHash.copy(header24, 16);

  const tokensBuf = Buffer.concat(tokens);
  const transcript = Buffer.concat([header24, tokensBuf, payloadBuf]);
  const soulSig = soul.signTranscript(transcript);

  const counts = Buffer.allocUnsafe(4);
  counts.writeUInt16BE(tokens.length, 0);
  counts.writeUInt16BE(payloadBuf.length, 2);

  return Buffer.concat([header24, soulSig, counts, tokensBuf, payloadBuf]);
}

export function decodeAndVerifyCapsule(buf, verifierSoul, offset = 0) {
  if (buf.length - offset < 68) {
    throw new Error("TruncatedPacket");
  }
  if (
    buf[offset] !== 0x4d ||
    buf[offset + 1] !== 0x38 ||
    buf[offset + 2] !== 0x21 ||
    buf[offset + 3] !== 0x01
  ) {
    throw new Error("InvalidMagic");
  }
  const header24 = buf.subarray(offset, offset + 24);
  const flags = header24.readUInt16BE(4);
  const frequencyHz = header24.readUInt16BE(6);
  const timestampMs = Number(header24.readBigUInt64BE(8));
  const soulSig = buf.subarray(offset + 24, offset + 64);
  const tokenCount = buf.readUInt16BE(offset + 64);
  const payloadLen = buf.readUInt16BE(offset + 66);
  const totalLen = 68 + tokenCount * 4 + payloadLen;
  if (buf.length - offset < totalLen) {
    throw new Error("TruncatedPacket");
  }
  const tokensBuf = buf.subarray(offset + 68, offset + 68 + tokenCount * 4);
  const payloadBuf = buf.subarray(offset + 68 + tokenCount * 4, offset + totalLen);
  scanPayloadVigilance(payloadBuf);

  const transcript = Buffer.concat([header24, tokensBuf, payloadBuf]);
  const soulInfo = verifierSoul.verifyTranscript(soulSig, transcript);

  const tokens = [];
  for (let i = 0; i < tokenCount; i++) {
    tokens.push(decodeAyevnToken(tokensBuf, i * 4));
  }

  return {
    capsule: {
      flags,
      frequencyHz,
      timestampMs,
      tokens,
      payload: payloadBuf,
      soulInfo,
    },
    bytesConsumed: totalLen,
  };
}

export class PacketBatcher {
  constructor(maxPayloadBytes = 1450) {
    this.maxPayloadBytes = maxPayloadBytes;
    this.sequence = 0;
    this.pending = [];
    this.pendingBytes = 12;
    this.emittedFrames = [];
  }

  push(capsuleBuf) {
    if (12 + capsuleBuf.length > this.maxPayloadBytes) {
      throw new Error("CapsuleExceedsMtu");
    }
    let emitted = null;
    if (this.pending.length > 0 && this.pendingBytes + capsuleBuf.length > this.maxPayloadBytes) {
      emitted = this.flush();
    }
    this.pending.push(capsuleBuf);
    this.pendingBytes += capsuleBuf.length;
    return emitted;
  }

  flush() {
    if (this.pending.length === 0) return null;
    const payloadLen = this.pendingBytes - 12;
    const header = Buffer.allocUnsafe(12);
    header.write("MNET", 0, 4, "ascii");
    header.writeUInt32BE(this.sequence++, 4);
    header.writeUInt16BE(this.pending.length, 8);
    header.writeUInt16BE(payloadLen, 10);
    const frame = Buffer.concat([header, ...this.pending]);
    this.pending = [];
    this.pendingBytes = 12;
    this.emittedFrames.push(frame);
    return frame;
  }
}
