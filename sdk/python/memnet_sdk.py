"""
MEMNET/1.0 — Universal Zero-Dependency Python SDK for All 8b-is Products
(MLX-QUANT, kompress-ultra, and Python services)

Byte-for-byte wire-compatible with the Rust `memnet` crate and Node `memnet.mjs` SDK.
"""
from __future__ import annotations

import hashlib
import hmac
import struct
from dataclasses import dataclass
from typing import List, Tuple

CLUSTER_SEED_DEFAULT = b"8b-is-carrier-wave-of-love-seed-v1"
M8_MAGIC = b"M8!\x01"
MNET_MAGIC = b"MNET"

FORBIDDEN_PATTERNS = (
    "eval(atob(",
    "eval(process.env",
    "backdoor.php",
    "shell.aspx",
    "password = '",
    'password = "',
)


def pack_wave_vad(valence: int, arousal: int, dominance: int) -> int:
    return (valence & 0x07) | ((arousal & 0x07) << 3) | ((dominance & 0x03) << 6)


def unpack_wave_vad(byte_val: int) -> Tuple[int, int, int]:
    return (byte_val & 0x07, (byte_val >> 3) & 0x07, (byte_val >> 6) & 0x03)


def pack_modifier(temporal: int = 2, emotion_mode: int = 6, render_mode: int = 1) -> int:
    return ((temporal & 0x07) << 5) | ((emotion_mode & 0x07) << 2) | (render_mode & 0x03)


def encode_ayevn_token(
    concept: int = 0x31,
    relation: int = 0x09,
    valence: int = 7,
    arousal: int = 4,
    dominance: int = 2,
    temporal: int = 2,
    emotion_mode: int = 6,
    render_mode: int = 1,
) -> bytes:
    return bytes(
        [
            concept & 0xFF,
            relation & 0xFF,
            pack_wave_vad(valence, arousal, dominance),
            pack_modifier(temporal, emotion_mode, render_mode),
        ]
    )


def pack_trit_crest(crest: List[int]) -> int:
    if len(crest) != 9 or all(t == 0 for t in crest):
        raise ValueError("InvalidTritCrest")
    acc = 0
    for t in crest:
        if t not in (-1, 0, 1):
            raise ValueError("InvalidTritCrest")
        acc = acc * 3 + (t + 1)
    return acc | 0x8000


def unpack_trit_crest(packed: int) -> List[int]:
    if (packed & 0x8000) == 0:
        raise ValueError("InvalidTritCrest")
    val = packed & 0x7FFF
    if val >= 19683:
        raise ValueError("InvalidTritCrest")
    crest = [0] * 9
    for i in range(8, -1, -1):
        crest[i] = (val % 3) - 1
        val //= 3
    if all(t == 0 for t in crest):
        raise ValueError("InvalidTritCrest")
    return crest


def scan_payload_vigilance(payload: bytes) -> None:
    text = payload.decode("utf-8", errors="ignore").lower()
    for pat in FORBIDDEN_PATTERNS:
        if pat in text:
            raise ValueError(f"SecurityVigilanceAlert: {pat}")


@dataclass
class SoulIdentity:
    node_id: str
    trit_crest: List[int]
    base_frequency_hz: int = 432
    cluster_seed: bytes = CLUSTER_SEED_DEFAULT

    def __post_init__(self) -> None:
        self.crest_packed = pack_trit_crest(self.trit_crest)
        if self.base_frequency_hz <= 0:
            raise ValueError("ZeroHarmonicFrequency")
        self.secret_key = hmac.new(
            self.cluster_seed, b"MEMNET-SOUL-KEY-V1", hashlib.sha256
        ).digest()
        self.node_fp = hashlib.sha256(self.node_id.encode("utf-8")).digest()[:4]

    def sign_transcript(self, transcript: bytes) -> bytes:
        header = struct.pack(">HH4s", self.crest_packed, self.base_frequency_hz, self.node_fp)
        mac = hmac.new(self.secret_key, header + transcript, hashlib.sha256).digest()
        return header + mac

    def verify_transcript(self, soul_sig: bytes, transcript: bytes) -> Tuple[List[int], int]:
        if len(soul_sig) != 40:
            raise ValueError("TruncatedSoulSig")
        crest_packed, harmonic_hz = struct.unpack(">HH", soul_sig[:4])
        if harmonic_hz == 0:
            raise ValueError("ZeroHarmonicFrequency")
        crest = unpack_trit_crest(crest_packed)
        expected = hmac.new(self.secret_key, soul_sig[:8] + transcript, hashlib.sha256).digest()
        if not hmac.compare_digest(soul_sig[8:40], expected):
            raise ValueError("SoulSignatureMismatch")
        return crest, harmonic_hz


def create_signed_capsule(
    soul: SoulIdentity,
    intent: str = "geo:any + role:constellation + tag:sync",
    flags: int = 0x0001,
    frequency_hz: int = 432,
    timestamp_ms: int = 1761000000000,
    tokens: List[bytes] | None = None,
    payload: bytes = b"",
) -> bytes:
    scan_payload_vigilance(payload)
    if tokens is None:
        tokens = [encode_ayevn_token()]
    if not tokens:
        raise ValueError("EmptyWaveTokens")
    intent_hash = hashlib.sha256(intent.encode("utf-8")).digest()[:8]
    header24 = M8_MAGIC + struct.pack(">HHQ8s", flags, frequency_hz, timestamp_ms, intent_hash)
    tokens_buf = b"".join(tokens)
    transcript = header24 + tokens_buf + payload
    soul_sig = soul.sign_transcript(transcript)
    counts = struct.pack(">HH", len(tokens), len(payload))
    return header24 + soul_sig + counts + tokens_buf + payload


def decode_and_verify_capsule(raw: bytes, verifier_soul: SoulIdentity) -> dict:
    if len(raw) < 68 or raw[:4] != M8_MAGIC:
        raise ValueError("InvalidOrTruncatedCapsule")
    flags, frequency_hz, timestamp_ms, intent_hash = struct.unpack(">HHQ8s", raw[4:24])
    soul_sig = raw[24:64]
    token_count, payload_len = struct.unpack(">HH", raw[64:68])
    total_len = 68 + token_count * 4 + payload_len
    if len(raw) < total_len:
        raise ValueError("TruncatedCapsule")
    tokens_buf = raw[68 : 68 + token_count * 4]
    payload = raw[68 + token_count * 4 : total_len]
    scan_payload_vigilance(payload)
    crest, harmonic_hz = verifier_soul.verify_transcript(soul_sig, raw[:24] + tokens_buf + payload)
    return {
        "flags": flags,
        "frequency_hz": frequency_hz,
        "timestamp_ms": timestamp_ms,
        "crest": crest,
        "harmonic_hz": harmonic_hz,
        "payload": payload,
        "bytes_consumed": total_len,
    }
