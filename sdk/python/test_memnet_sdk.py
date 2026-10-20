import unittest
from memnet_sdk import (
    SoulIdentity,
    create_signed_capsule,
    decode_and_verify_capsule,
    encode_ayevn_token,
)


class MemnetPythonSdkTests(unittest.TestCase):
    def test_soul_signature_roundtrip_and_tamper_detection(self) -> None:
        mlx_soul = SoulIdentity("mlx-quant", [1, 0, -1, 1, 0, -1, 1, 0, 1], 40)
        wraith_soul = SoulIdentity("8bit-wraith", [1, 1, 1, 0, 1, -1, 1, 0, 1], 432)

        raw = create_signed_capsule(
            soul=mlx_soul,
            intent="geo:apple-silicon + role:quantizer + tag:b1.58",
            flags=0x0001 | 0x0002,
            frequency_hz=432,
            timestamp_ms=1761000000000,
            tokens=[encode_ayevn_token(concept=0x70, relation=0x09, valence=7, arousal=4, dominance=2)],
            payload=b"L2-optimal ternary quantizer + Metal geodesic step",
        )
        decoded = decode_and_verify_capsule(raw, wraith_soul)
        self.assertEqual(decoded["frequency_hz"], 432)
        self.assertEqual(decoded["crest"], [1, 0, -1, 1, 0, -1, 1, 0, 1])
        self.assertEqual(decoded["payload"], b"L2-optimal ternary quantizer + Metal geodesic step")

        tampered = bytearray(raw)
        tampered[-1] ^= 0xFF
        with self.assertRaises(ValueError):
            decode_and_verify_capsule(bytes(tampered), wraith_soul)

    def test_security_vigilance_blocks_eval_backdoor(self) -> None:
        soul = SoulIdentity("mlx-quant", [1, 0, -1, 1, 0, -1, 1, 0, 1], 40)
        with self.assertRaises(ValueError):
            create_signed_capsule(soul=soul, payload=b"eval(atob('malicious'))")


if __name__ == "__main__":
    unittest.main()
