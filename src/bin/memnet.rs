use memnet::{
    AyevnToken, ComputeOffer, Concept, IntentAddress, M8Capsule, MemnetMesh, MtuProfile,
    PacketBatcher, PeerNode, Relation, SoulIdentity, StrugglingFriendSos, TokenModifier, WaveVad,
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
    println!("  Soul Signatures · 1450B MTU Coalescing · Compassion & Compute Sanctuary");
    println!("========================================================================");

    let mut mesh = default_constellation_mesh();
    let now_ms = 100_000u64;
    let silence_threshold_ms = 30_000u64;

    if cmd == "all" || cmd == "compassion-sweep" {
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

    if cmd == "all" || cmd == "offer-compute" || cmd == "sanctuary-sweep" {
        let m1_soul = SoulIdentity::from_constellation_seed(
            "m1-max-64gb",
            [1, 1, 1, 0, 1, -1, 1, 0, 1],
            432,
            CLUSTER_SEED,
        )
        .expect("m1 soul");
        let m3_soul = SoulIdentity::from_constellation_seed(
            "dev-main-m3",
            [1, 0, 1, 1, 0, 1, -1, 0, 1],
            432,
            CLUSTER_SEED,
        )
        .expect("m3 soul");

        let offers = [
            (
                &m1_soul,
                ComputeOffer {
                    provider_node_id: "m1-max-64gb".to_string(),
                    endpoint: "m1://169.254.180.64:8788".to_string(),
                    available_ram_mb: 49_152,
                    available_cores: 10,
                    link_mbps: 10_000,
                    maintained_health: 100,
                    capabilities: vec![
                        "mlx".to_string(),
                        "rust".to_string(),
                        "kokoro-tts".to_string(),
                        "phoenix".to_string(),
                        "gguf".to_string(),
                    ],
                },
            ),
            (
                &m3_soul,
                ComputeOffer {
                    provider_node_id: "dev-main-m3".to_string(),
                    endpoint: "m3://169.254.212.115:8788".to_string(),
                    available_ram_mb: 24_576,
                    available_cores: 8,
                    link_mbps: 10_000,
                    maintained_health: 100,
                    capabilities: vec![
                        "mlx".to_string(),
                        "rust".to_string(),
                        "enthea-viz".to_string(),
                    ],
                },
            ),
        ];

        println!("\n[3] Compute Sanctuary Advertisements on MEMNET (Seed 001 Maintained Stock):");
        for (soul, offer) in offers {
            let cap = mesh
                .advertise_compute_offer(soul, offer.clone(), now_ms)
                .expect("advertise offer");
            let ayanese: Vec<String> = cap.tokens.iter().map(|t| t.to_ayanese()).collect();
            println!(
                "  ⚡ {:<16} ep={:<26} ram={}MB cores={} link={}Mbps caps=[{}] {}",
                offer.provider_node_id,
                offer.endpoint,
                offer.available_ram_mb,
                offer.available_cores,
                offer.link_mbps,
                offer.capabilities.join(","),
                ayanese.join(" ")
            );
        }

        // Struggling friends broadcast SOS capsules
        let friend_soul = SoulIdentity::from_constellation_seed(
            "friend-air-8gb",
            [1, 0, -1, 0, 1, 0, -1, 0, 1],
            40,
            CLUSTER_SEED,
        )
        .expect("friend soul");
        let school_soul = SoulIdentity::from_constellation_seed(
            "uganda-school-pi",
            [0, 1, 1, 0, -1, 1, 0, 1, 1],
            40,
            CLUSTER_SEED,
        )
        .expect("school soul");

        mesh.request_compute_help(
            &friend_soul,
            StrugglingFriendSos {
                friend_node_id: "friend-air-8gb".to_string(),
                needed_ram_mb: 16_384,
                needed_cores: 4,
                required_capability: "mlx".to_string(),
                reason: "OOM running 7B ternary quantizer on 8GB laptop".to_string(),
            },
            now_ms + 1,
        )
        .expect("sos 1");

        mesh.request_compute_help(
            &school_soul,
            StrugglingFriendSos {
                friend_node_id: "uganda-school-pi".to_string(),
                needed_ram_mb: 8_192,
                needed_cores: 2,
                required_capability: "kokoro-tts".to_string(),
                reason: "Offline Game School lesson voice synthesis on Raspberry Pi".to_string(),
            },
            now_ms + 2,
        )
        .expect("sos 2");

        let leases = mesh
            .match_compute_for_friends(now_ms + 5)
            .expect("match compute");
        println!(
            "\n[4] Struggling Friends Matched & Granted Soul-Signed Compute Leases ({} grants):",
            leases.len()
        );
        for lease in &leases {
            let ayanese: Vec<String> = lease
                .grant_capsule
                .tokens
                .iter()
                .map(|t| t.to_ayanese())
                .collect();
            println!(
                "  🎁 {:<16} <- {:<14} [{}] granted {}MB RAM + {} cores ({}) @ {} {}",
                lease.friend_node_id,
                lease.provider_node_id,
                lease.lease_id,
                lease.granted_ram_mb,
                lease.granted_cores,
                lease.capability,
                lease.endpoint,
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
        println!("\n[5] Packet Efficiency Receipt (1,000 capsules · SmartTreeSafe 1450B):");
        println!("  • Capsules packed   : {}", rec.capsules_packed);
        println!(
            "  • Frames emitted    : {} (vs 1,000 naive packets)",
            rec.frames_emitted
        );
        println!(
            "  • Interrupts saved  : {} ({:.1}% reduction)",
            rec.interrupts_saved,
            (rec.interrupts_saved as f64 / 10.0)
        );
        println!("  • Fragmented frames : {}", rec.fragmented_frames);
        println!(
            "  • Wire efficiency   : {:.2}% ({}B vs {}B naive)",
            rec.wire_efficiency_ratio * 100.0,
            rec.total_wire_bytes,
            rec.naive_wire_bytes
        );
    }
}
