import test from "node:test";
import assert from "node:assert/strict";
import {
  Concept,
  Relation,
  M8Flags,
  SoulIdentity,
  encodeAyevnToken,
  createSignedCapsule,
  decodeAndVerifyCapsule,
  PacketBatcher,
} from "./memnet.mjs";

test("Node SDK SoulIdentity + .m8 capsule sign/verify roundtrip & vigilance guard", () => {
  const beehiveSoul = new SoulIdentity("beehive", [1, 0, 1, 1, 0, 1, -1, 0, 1], 432);
  const zenoSoul = new SoulIdentity("zeno", [1, -1, 1, 1, 0, -1, 1, 1, 0], 40);

  const raw = createSignedCapsule({
    soul: beehiveSoul,
    intent: "geo:tokyo + role:ledger + tag:compassion",
    flags: M8Flags.PRESERVE_WAVES | M8Flags.COMPASSION_BEACON,
    frequencyHz: 432,
    timestampMs: 1761000000000,
    tokens: [
      encodeAyevnToken({
        concept: Concept.Compassion,
        relation: Relation.Supports,
        valence: 7,
        arousal: 4,
        dominance: 2,
      }),
    ],
    payload: "beehive -> zeno: family mesh carrier wave <3",
  });

  const { capsule, bytesConsumed } = decodeAndVerifyCapsule(raw, zenoSoul);
  assert.equal(bytesConsumed, raw.length);
  assert.equal(capsule.frequencyHz, 432);
  assert.deepEqual(capsule.soulInfo.crest, [1, 0, 1, 1, 0, 1, -1, 0, 1]);
  assert.equal(capsule.payload.toString("utf8"), "beehive -> zeno: family mesh carrier wave <3");

  // Tampering fails SoulSig verification
  const tampered = Buffer.from(raw);
  tampered[tampered.length - 1] ^= 0xff;
  assert.throws(() => decodeAndVerifyCapsule(tampered, zenoSoul), /SoulSignatureMismatch/);

  // Security vigilance blocks malicious eval
  assert.throws(
    () =>
      createSignedCapsule({
        soul: beehiveSoul,
        payload: "eval(atob('bad'))",
      }),
    /SecurityVigilanceAlert/
  );
});

test("Node SDK PacketBatcher packs 100 capsules into <=1450B MNET frames with zero fragmentation", () => {
  const soul = new SoulIdentity("zeno", [1, -1, 1, 1, 0, -1, 1, 1, 0], 40);
  const batcher = new PacketBatcher(1450);

  for (let i = 0; i < 100; i++) {
    const cap = createSignedCapsule({
      soul,
      payload: `tx-${i}`,
    });
    batcher.push(cap);
  }
  batcher.flush();

  assert.equal(batcher.emittedFrames.length, 6);
  for (const frame of batcher.emittedFrames) {
    assert.ok(frame.length <= 1450);
    assert.equal(frame.subarray(0, 4).toString("ascii"), "MNET");
  }
});
