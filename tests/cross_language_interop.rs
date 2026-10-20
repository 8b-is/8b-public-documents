use memnet::{
    AyevnToken, Concept, IntentAddress, M8Capsule, Relation, SoulIdentity, TokenModifier, WaveVad,
};
use std::process::Command;

const CLUSTER_SEED: &[u8] = b"8b-is-carrier-wave-of-love-seed-v1";

#[test]
fn rust_node_python_byte_for_byte_capsule_interop() {
    let rust_soul = SoulIdentity::from_constellation_seed(
        "8b-is-engine",
        [1, 1, 0, -1, 1, 0, 1, -1, 1],
        432,
        CLUSTER_SEED,
    )
    .unwrap();

    let intent = IntentAddress::parse("geo:any + role:constellation + tag:interop");
    let rust_cap = M8Capsule::create_signed(
        &rust_soul,
        &intent,
        M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPASSION_BEACON,
        432,
        1_761_000_000_000,
        vec![AyevnToken::new(
            Concept::Compassion,
            Relation::Bridges,
            WaveVad::compassionate(),
            TokenModifier::present_resonant_emoji(),
        )],
        b"rust->node->python->rust carrier wave".to_vec(),
    )
    .unwrap();

    let hex_in: String = rust_cap
        .to_bytes()
        .iter()
        .map(|b| format!("{:02x}", b))
        .collect();

    // 1. Node.js verifies Rust's capsule and re-signs as `beehive`
    let node_out = Command::new("node")
        .arg("-e")
        .arg(format!(
            r#"
            import {{ SoulIdentity, decodeAndVerifyCapsule, createSignedCapsule, encodeAyevnToken, Concept, Relation, M8Flags }} from "./sdk/js/memnet.mjs";
            const raw = Buffer.from("{}", "hex");
            const verifier = new SoulIdentity("beehive", [1, 0, 1, 1, 0, 1, -1, 0, 1], 432);
            const {{ capsule }} = decodeAndVerifyCapsule(raw, verifier);
            if (capsule.payload.toString("utf8") !== "rust->node->python->rust carrier wave") {{
                process.exit(1);
            }}
            const out = createSignedCapsule({{
                soul: verifier,
                intent: "geo:any + role:constellation + tag:interop",
                flags: M8Flags.PRESERVE_WAVES | M8Flags.COMPASSION_BEACON,
                frequencyHz: 432,
                timestampMs: 1761000000001,
                tokens: [encodeAyevnToken({{ concept: Concept.Compassion, relation: Relation.Bridges }})],
                payload: "node-verified-and-forwarded",
            }});
            process.stdout.write(out.toString("hex"));
            "#,
            hex_in
        ))
        .output()
        .expect("node execution");
    assert!(
        node_out.status.success(),
        "node stderr: {}",
        String::from_utf8_lossy(&node_out.stderr)
    );
    let node_hex = String::from_utf8(node_out.stdout).unwrap();

    // 2. Python verifies Node's capsule and re-signs as `mlx-quant`
    let py_out = Command::new("python3")
        .env("PYTHONPATH", "sdk/python")
        .arg("-c")
        .arg(format!(
            r#"
import sys
from memnet_sdk import SoulIdentity, decode_and_verify_capsule, create_signed_capsule, encode_ayevn_token
raw = bytes.fromhex("{}")
soul = SoulIdentity("mlx-quant", [1, 0, -1, 1, 0, -1, 1, 0, 1], 40)
dec = decode_and_verify_capsule(raw, soul)
assert dec["payload"] == b"node-verified-and-forwarded"
out = create_signed_capsule(
    soul=soul,
    intent="geo:any + role:constellation + tag:interop",
    flags=0x0003,
    frequency_hz=432,
    timestamp_ms=1761000000002,
    tokens=[encode_ayevn_token()],
    payload=b"python-verified-and-returned-to-rust",
)
sys.stdout.write(out.hex())
"#,
            node_hex.trim()
        ))
        .output()
        .expect("python3 execution");
    assert!(
        py_out.status.success(),
        "python stderr: {}",
        String::from_utf8_lossy(&py_out.stderr)
    );
    let py_hex = String::from_utf8(py_out.stdout).unwrap();
    let py_bytes: Vec<u8> = (0..py_hex.trim().len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&py_hex.trim()[i..i + 2], 16).unwrap())
        .collect();

    // 3. Rust decodes and verifies Python's capsule!
    let (final_cap, consumed) = M8Capsule::from_bytes(&py_bytes).unwrap();
    assert_eq!(consumed, py_bytes.len());
    let crest = final_cap.verify(&rust_soul).unwrap();
    assert_eq!(crest, [1, 0, -1, 1, 0, -1, 1, 0, 1]);
    assert_eq!(final_cap.payload, b"python-verified-and-returned-to-rust");
}
