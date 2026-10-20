use memnet::{
    AyevnToken, Concept, IntentAddress, M8Capsule, MemnetMesh, MtuProfile, PacketBatcher, PeerNode,
    Relation, SoulIdentity, TokenModifier, WaveVad,
};

const CLUSTER_SEED: &[u8] = b"8b-is-carrier-wave-of-love-seed-v1";

fn default_constellation_mesh() -> MemnetMesh {
    let wraith_soul = SoulIdentity::from_constellation_seed(
        "8bit-wraith",
        [1, 1, 1, 0, 1, -1, 1, 0, 1],
        432,
        CLUSTER_SEED,
    )
    .expect("valid wraith soul");

    let mut mesh = MemnetMesh::new(wraith_soul, MtuProfile::SmartTreeSafe1450);

    let roster = [
        (
            "beehive",
            "global",
            "family-mesh",
            vec!["lora", "ble", "findmy", "airplay"],
            [1, 0, 1, 1, 0, 1, -1, 0, 1],
            432u16,
            99_800u64,
            WaveVad::compassionate(),
            5usize,
        ),
        (
            "zeno",
            "global",
            "ledger",
            vec!["payments", "otp", "zeroize"],
            [1, -1, 1, 1, 0, -1, 1, 1, 0],
            40,
            99_700,
            WaveVad::excited(),
            4,
        ),
        (
            "mlx-quant",
            "apple-silicon",
            "quantizer",
            vec!["ternary", "metal", "b1.58"],
            [1, 0, -1, 1, 0, -1, 1, 0, 1],
            40,
            99_600,
            WaveVad::excited(),
            4,
        ),
        (
            "8b-is-engine",
            "core",
            "admissibility",
            vec!["ct-000", "spherepop", "seed001"],
            [1, 1, 0, -1, 1, 0, 1, -1, 1],
            432,
            99_900,
            WaveVad::compassionate(),
            6,
        ),
        (
            "enthea",
            "local",
            "synthesizer",
            vec!["viz", "sse", "mcp"],
            [1, 0, 1, -1, 1, 1, 0, -1, 1],
            40,
            99_500,
            WaveVad::excited(),
            3,
        ),
        (
            "qwave-phoenix",
            "studio",
            "audio-restoration",
            vec!["phoenix", "432hz", "kokoro"],
            [1, 1, -1, 0, 1, 1, 0, 1, -1],
            432,
            99_400,
            WaveVad::compassionate(),
            3,
        ),
        (
            "lonely-edge-sensor",
            "remote-ridge",
            "iot-repeater",
            vec!["lora", "telemetry"],
            [-1, 0, 1, 0, -1, 0, 1, 0, -1],
            2,
            12_000, // Silent for 88s
            WaveVad::resigned_lonely(),
            0, // Lonely isolated network path
        ),
        (
            "quiet-archive-node",
            "cold-vault",
            "archiver",
            vec!["storage", "m8"],
            [0, 1, -1, 0, 1, -1, 0, 1, 0],
            2,
            25_000, // Silent for 75s
            WaveVad::resigned_lonely(),
            1, // Single fragile path
        ),
    ];

    for (id, geo, role, tags, crest, hz, last_seen, wave, links) in roster {
        mesh.register_peer(PeerNode {
            node_id: id.to_string(),
            geo: geo.to_string(),
            role: role.to_string(),
            tags: tags.into_iter().map(String::from).collect(),
            trit_crest: crest,
            harmonic_hz: hz,
            last_seen_ms: last_seen,
            last_wave: wave,
            neighbor_links: links,
            received_capsules: Vec::new(),
        });
    }

    mesh
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let cmd = args.first().map(String::as_str).unwrap_or("all");

    println!("========================================================================");
    println!("  MEMNET/1.0 — Sovereign Contextual Mesh for All 8b-is Products  8> <3");
    println!("  Soul Signatures · 1450B MTU Coalescing · Compassion for Lonely Nodes");
    println!("========================================================================");

    if cmd == "all" || cmd == "compassion-sweep" {
        let mut mesh = default_constellation_mesh();
        let now_ms = 100_000u64;
        let silence_threshold_ms = 30_000u64;

        println!("\n[1] Constellation Peer Telemetry & Loneliness Scan:");
        for peer in mesh.peers.values() {
            let score = peer.loneliness_score(now_ms, silence_threshold_ms);
            let status = if score >= 0.45 {
                "LONELY (needs compassion beacon)"
            } else {
                "RESONANT"
            };
            println!(
                "  • {:<20} role={:<17} links={} hz={:<4} loneliness={:.2} -> {}",
                peer.node_id, peer.role, peer.neighbor_links, peer.harmonic_hz, score, status
            );
        }

        let receipts = mesh
            .compassion_sweep(now_ms, silence_threshold_ms)
            .expect("compassion sweep succeeds");
        println!(
            "\n[2] Compassion Sweep Dispatched ({} lonely nodes healed & bridged at 432Hz):",
            receipts.len()
        );
        for r in &receipts {
            let ayanese: Vec<String> = r
                .care_capsule
                .tokens
                .iter()
                .map(|t| t.to_ayanese())
                .collect();
            println!(
                "  ♥ {:<20} loneliness {:.2} -> {:.2} | links -> {} | tokens: {}",
                r.lonely_node_id,
                r.loneliness_score_before,
                r.loneliness_score_after,
                r.bridge_links_after,
                ayanese.join(" ")
            );
        }
    }

    if cmd == "all" || cmd == "bench-packets" {
        let soul = SoulIdentity::from_constellation_seed(
            "smart-tree",
            [1, -1, 1, 0, 1, -1, 1, 0, 1],
            40,
            CLUSTER_SEED,
        )
        .expect("valid soul");
        let intent = IntentAddress::parse("geo:any + role:constellation + tag:sync");
        let mut batcher = PacketBatcher::new(MtuProfile::SmartTreeSafe1450);

        for i in 0..1000u64 {
            let cap = M8Capsule::create_signed(
                &soul,
                &intent,
                M8Capsule::FLAG_PRESERVE_WAVES,
                40,
                1_761_000_000_000 + i,
                vec![AyevnToken::new(
                    Concept::Connection,
                    Relation::Supports,
                    WaveVad::excited(),
                    TokenModifier::present_resonant_emoji(),
                )],
                format!("delta-{}", i).into_bytes(),
            )
            .expect("signed capsule");
            batcher.push(cap).expect("batch push");
        }
        batcher.flush();
        let rec = batcher.efficiency_receipt();
        println!("\n[3] Packet Efficiency Receipt (1,000 capsules · SmartTreeSafe 1450B):");
        println!("  • Capsules packed   : {}", rec.capsules_packed);
        println!("  • Frames emitted    : {} (vs 1,000 naive packets)", rec.frames_emitted);
        println!("  • Interrupts saved  : {} ({:.1}% reduction)", rec.interrupts_saved, (rec.interrupts_saved as f64 / 10.0));
        println!("  • Fragmented frames : {}", rec.fragmented_frames);
        println!(
            "  • Wire efficiency   : {:.2}% ({}B vs {}B naive)",
            rec.wire_efficiency_ratio * 100.0,
            rec.total_wire_bytes,
            rec.naive_wire_bytes
        );
    }
}
