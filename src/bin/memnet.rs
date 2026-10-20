use memnet::{
    encode_kompress_super_ultra, AyevnToken, ComputeOffer, Concept, IntentAddress, M8Capsule,
    MemnetMesh, MtuProfile, PacketBatcher, PeerNode, Relation, SoulIdentity, StrugglingFriendSos,
    TokenModifier, WaveVad,
};
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream, UdpSocket};
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

const CLUSTER_SEED: &[u8] = b"8b-is-carrier-wave-of-love-seed-v1";

fn now_epoch_ms() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map(|d| d.as_millis() as u64)
        .unwrap_or(1_761_000_000_000)
}

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
            "galaxy-s24-ultra",
            "mobile-edge",
            "android-flagship-sanctuary",
            vec![
                "sm8650-ac",
                "adreno-750",
                "hexagon-npu",
                "vulkan",
                "nnapi",
                "rust",
                "spherepop",
                "0o0-ssu",
                "show-me-missouri",
                "SM-S928U1",
                "R5CWC3C3FXA",
            ],
            [1, 1, 1, 1, -1, 1, 0, 1, 1],
            432,
            99_980,
            WaveVad::compassionate(),
            5,
        ),
        (
            "galaxy-tab-s9-ultra",
            "mobile-edge",
            "android-tablet-sanctuary",
            vec![
                "nnapi",
                "vulkan",
                "rust",
                "kokoro-tts",
                "spherepop",
                "0o0-ssu",
                "SM-X910",
                "R52X104QZWE",
            ],
            [1, 1, 1, -1, 1, 0, 1, 1, 1],
            432,
            99_950,
            WaveVad::compassionate(),
            4,
        ),
        (
            "blu-g75",
            "mobile-edge",
            "android-phone-sanctuary",
            vec![
                "mt6768",
                "mali-g52",
                "nnapi",
                "rust",
                "spherepop",
                "0o0-ssu",
                "G1170",
                "1010305026000644",
            ],
            [1, 0, 1, 1, -1, 1, 0, 1, 1],
            432,
            99_920,
            WaveVad::compassionate(),
            4,
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

fn serve_sanctuary(bind_addr: &str, node_id: &str, once: bool) {
    let provider_soul = SoulIdentity::from_constellation_seed(
        node_id,
        [1, 1, 1, 0, 1, -1, 1, 0, 1],
        432,
        CLUSTER_SEED,
    )
    .expect("provider soul");

    let mut mesh = MemnetMesh::new(provider_soul.clone(), MtuProfile::SmartTreeSafe1450);
    let offer = match node_id {
        "blu-g75" => ComputeOffer::blu_g75(),
        "galaxy-tab-s9-ultra" => ComputeOffer::galaxy_tab_s9_ultra(),
        "galaxy-s24-ultra" => ComputeOffer::galaxy_s24_ultra(),
        "dev-main-m3" => ComputeOffer {
            provider_node_id: "dev-main-m3".to_string(),
            endpoint: format!("m3://{}", bind_addr),
            available_ram_mb: 16_384,
            available_cores: 8,
            link_mbps: 1_200,
            maintained_health: 99,
            capabilities: vec![
                "mlx".to_string(),
                "rust".to_string(),
                "spherepop".to_string(),
                "0o0-ssu".to_string(),
                "ultrawhale".to_string(),
            ],
        },
        _ => ComputeOffer {
            provider_node_id: node_id.to_string(),
            endpoint: format!("m1://{}", bind_addr),
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
                "kompress-0o0".to_string(),
            ],
        },
    };
    let offer_cap = mesh
        .advertise_compute_offer(&provider_soul, offer.clone(), now_epoch_ms())
        .expect("advertise offer");

    let listener = TcpListener::bind(bind_addr).expect("bind sanctuary TCP listener");
    println!(
        "⚡ [MEMNET/1.0 SANCTUARY DAEMON: {}] Listening on {} (0o0-SSU + SpherePop active)",
        node_id, bind_addr
    );
    println!(
        "  • Offer payload: {}B raw -> {}B 0o0-SSU compressed ({:.1}% saved)",
        offer.to_wire_string().len(),
        offer_cap.payload.len(),
        (1.0 - (offer_cap.payload.len() as f64 / offer.to_wire_string().len() as f64)) * 100.0
    );

    for stream_res in listener.incoming() {
        if let Ok(mut stream) = stream_res {
            let peer_addr = stream
                .peer_addr()
                .map(|a| a.to_string())
                .unwrap_or_else(|_| "unknown".to_string());
            let mut buf = [0u8; 2048];
            if let Ok(n) = stream.read(&mut buf) {
                if n >= 68 {
                    if let Ok((sos_cap, _)) = M8Capsule::from_bytes(&buf[..n]) {
                        if sos_cap.verify(&provider_soul).is_ok() {
                            if let Ok(decompressed) = sos_cap.decompressed_payload() {
                                if let Ok(text) = std::str::from_utf8(&decompressed) {
                                    if let Ok(sos) = StrugglingFriendSos::from_wire_string(text) {
                                        println!(
                                            "  🆘 Received verified 0o0-SSU SOS from {} ({}) -> need {}MB RAM + {} cores ({})",
                                            sos.friend_node_id,
                                            peer_addr,
                                            sos.needed_ram_mb,
                                            sos.needed_cores,
                                            sos.required_capability
                                        );
                                        mesh.compute_offers
                                            .insert(offer.provider_node_id.clone(), offer.clone());
                                        mesh.pending_sos.push(sos);
                                        if let Ok(leases) =
                                            mesh.match_compute_for_friends(now_epoch_ms())
                                        {
                                            let mut reply_batcher =
                                                PacketBatcher::new(MtuProfile::SmartTreeSafe1450);
                                            let _ = reply_batcher.push(offer_cap.clone());
                                            for lease in &leases {
                                                println!(
                                                    "  🎁 Granted {} -> {} ({}MB RAM + {} cores @ {}) [SpherePop #ValidWitness={}]",
                                                    lease.lease_id,
                                                    lease.friend_node_id,
                                                    lease.granted_ram_mb,
                                                    lease.granted_cores,
                                                    lease.endpoint,
                                                    lease.spherepop_witness.short_hex()
                                                );
                                                let _ =
                                                    reply_batcher.push(lease.grant_capsule.clone());
                                            }
                                            if let Some(frame) = reply_batcher.flush() {
                                                let _ = stream.write_all(&frame.raw_bytes);
                                                let _ = stream.flush();
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            if once {
                break;
            }
        }
    }
}

fn request_sanctuary(
    connect_addr: &str,
    friend_id: &str,
    ram_mb: u32,
    cores: u16,
    cap: &str,
    reason: &str,
) {
    let friend_soul = SoulIdentity::from_constellation_seed(
        friend_id,
        [1, 0, -1, 0, 1, 0, -1, 0, 1],
        40,
        CLUSTER_SEED,
    )
    .expect("friend soul");

    let sos = StrugglingFriendSos {
        friend_node_id: friend_id.to_string(),
        needed_ram_mb: ram_mb,
        needed_cores: cores,
        required_capability: cap.to_string(),
        reason: reason.to_string(),
    };
    let raw_sos = sos.to_wire_string();
    let intent = IntentAddress::parse(&format!("geo:any + role:compute-sanctuary + tag:{}", cap));
    let sos_cap = M8Capsule::create_signed_kompressed(
        &friend_soul,
        &intent,
        M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPUTE_SOS,
        40,
        now_epoch_ms(),
        vec![AyevnToken::new(
            Concept::ComputeSos,
            Relation::Initiates,
            WaveVad::resigned_lonely(),
            TokenModifier::present_resonant_emoji(),
        )],
        raw_sos.as_bytes(),
    )
    .expect("signed kompressed SOS");

    let wire_bytes = sos_cap.to_bytes();
    let t0 = Instant::now();
    let mut stream = TcpStream::connect(connect_addr).expect("connect to MEMNET sanctuary");
    stream.write_all(&wire_bytes).expect("send SOS capsule");
    stream.flush().expect("flush SOS");

    let mut reply = Vec::new();
    stream.read_to_end(&mut reply).expect("read MNET reply");
    let rtt = t0.elapsed();

    let frame = PacketBatcher::decode_and_verify_frame(&reply, &friend_soul)
        .expect("verify MNET frame & SoulSig");

    println!(
        "========================================================================\n  MEMNET/1.0 LIVE WIRE + KOMPRESS-SUPER-ULTRA (0o0) SANCTUARY RECEIPT\n========================================================================"
    );
    println!(
        "  • Target Sanctuary : {} (RTT: {:.3} ms)",
        connect_addr,
        rtt.as_secs_f64() * 1000.0
    );
    println!(
        "  • SOS Payload (0o0): {}B raw -> {}B compressed ({:.1}% saved) | Wire packet: {}B",
        raw_sos.len(),
        sos_cap.payload.len(),
        (1.0 - (sos_cap.payload.len() as f64 / raw_sos.len() as f64)) * 100.0,
        wire_bytes.len()
    );
    println!(
        "  • Reply MNET Frame : seq={} | {} Soul-Verified capsules in {}B (<=1450B MTU)",
        frame.sequence,
        frame.capsules.len(),
        frame.raw_bytes.len()
    );
    for (idx, c) in frame.capsules.iter().enumerate() {
        let decompressed = c.decompressed_payload().expect("decompress 0o0 payload");
        let text = String::from_utf8_lossy(&decompressed);
        let ayanese: Vec<String> = c.tokens.iter().map(|t| t.to_ayanese()).collect();
        println!(
            "  • Capsule #{:<2}      : {}B 0o0 -> {}B raw | {} | {}",
            idx + 1,
            c.payload.len(),
            decompressed.len(),
            ayanese.join(" "),
            text
        );
    }
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let cmd = args.first().map(String::as_str).unwrap_or("all");

    if cmd == "serve-sanctuary" {
        let mut bind_addr = "0.0.0.0:8788".to_string();
        let mut node_id = "m1-max-64gb".to_string();
        let mut once = false;
        let mut i = 1;
        while i < args.len() {
            match args[i].as_str() {
                "--bind" if i + 1 < args.len() => {
                    bind_addr = args[i + 1].clone();
                    i += 2;
                }
                "--node" if i + 1 < args.len() => {
                    node_id = args[i + 1].clone();
                    i += 2;
                }
                "--once" => {
                    once = true;
                    i += 1;
                }
                _ => i += 1,
            }
        }
        serve_sanctuary(&bind_addr, &node_id, once);
        return;
    }

    if cmd == "request-sanctuary" {
        let mut connect_addr = "169.254.180.64:8788".to_string();
        let mut friend_id = "friend-air-8gb".to_string();
        let mut ram_mb = 16_384u32;
        let mut cores = 4u16;
        let mut cap = "mlx".to_string();
        let mut reason = "OOM running 7B ternary quantizer on 8GB laptop".to_string();
        let mut i = 1;
        while i < args.len() {
            match args[i].as_str() {
                "--connect" if i + 1 < args.len() => {
                    connect_addr = args[i + 1].clone();
                    i += 2;
                }
                "--friend" if i + 1 < args.len() => {
                    friend_id = args[i + 1].clone();
                    i += 2;
                }
                "--ram-mb" if i + 1 < args.len() => {
                    ram_mb = args[i + 1].parse().unwrap_or(16_384);
                    i += 2;
                }
                "--cores" if i + 1 < args.len() => {
                    cores = args[i + 1].parse().unwrap_or(4);
                    i += 2;
                }
                "--cap" if i + 1 < args.len() => {
                    cap = args[i + 1].clone();
                    i += 2;
                }
                "--reason" if i + 1 < args.len() => {
                    reason = args[i + 1].clone();
                    i += 2;
                }
                _ => i += 1,
            }
        }
        request_sanctuary(&connect_addr, &friend_id, ram_mb, cores, &cap, &reason);
        return;
    }

    println!("========================================================================");
    println!("  MEMNET/1.0 — Sovereign Contextual Mesh for All 8b-is Products  8> <3");
    println!(
        "  +++ SpherePop ((( <( ? ~ ! @ > )> ))) · 0o0-SSU · S24U + Tab S9U + BLU G75"
    );
    println!("  ~=== SHOW-ME-STATE-MISSOURI{{(ALEX,CHRIS)}}+1~ <3 {{<3,<3,<3}} · 0 + 1 = one");
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
                "  • {:<20} role={:<24} links={} hz={:<4} loneliness={:.2} -> {}",
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
        let s24u_soul = SoulIdentity::from_constellation_seed(
            "galaxy-s24-ultra",
            [1, 1, 1, 1, -1, 1, 0, 1, 1],
            432,
            CLUSTER_SEED,
        )
        .expect("s24u soul");
        let s9u_soul = SoulIdentity::from_constellation_seed(
            "galaxy-tab-s9-ultra",
            [1, 1, 1, -1, 1, 0, 1, 1, 1],
            432,
            CLUSTER_SEED,
        )
        .expect("s9u soul");
        let g75_soul = SoulIdentity::from_constellation_seed(
            "blu-g75",
            [1, 0, 1, 1, -1, 1, 0, 1, 1],
            432,
            CLUSTER_SEED,
        )
        .expect("g75 soul");

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
            (&s24u_soul, ComputeOffer::galaxy_s24_ultra()),
            (&s9u_soul, ComputeOffer::galaxy_tab_s9_ultra()),
            (&g75_soul, ComputeOffer::blu_g75()),
        ];

        println!(
            "\n[3] Compute Sanctuary Advertisements on MEMNET (Seed 001 + SpherePop + 0o0-SSU):"
        );
        for (soul, offer) in offers {
            let raw_len = offer.to_wire_string().len();
            let sp_expr = offer.to_spherepop_expr();
            let sp_witness = offer.evaluate_spherepop().expect("SpherePop valid witness");
            let sp_compressed = encode_kompress_super_ultra(sp_expr.as_bytes());
            let cap = mesh
                .advertise_compute_offer(soul, offer.clone(), now_ms)
                .expect("advertise offer");
            let ayanese: Vec<String> = cap.tokens.iter().map(|t| t.to_ayanese()).collect();
            println!(
                "  ⚡ {:<20} ep={:<25} ram={:<5}MB cores={:<2} 0o0-SSU={}B/{}B ({:.0}% saved) {}",
                offer.provider_node_id,
                offer.endpoint,
                offer.available_ram_mb,
                offer.available_cores,
                cap.payload.len(),
                raw_len,
                (1.0 - (cap.payload.len() as f64 / raw_len as f64)) * 100.0,
                ayanese.join(" ")
            );
            println!(
                "     ↳ SpherePop [depth={} | #ValidWitness={} | 0o0-SSU {}B->{}B]: {}",
                sp_witness.sphere_depth,
                sp_witness.short_hex(),
                sp_expr.len(),
                sp_compressed.len(),
                sp_expr
            );
        }

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
        let nomad_soul = SoulIdentity::from_constellation_seed(
            "nomad-pocket-node",
            [1, -1, 0, 1, 1, 0, -1, 1, 0],
            40,
            CLUSTER_SEED,
        )
        .expect("nomad soul");
        let field_soul = SoulIdentity::from_constellation_seed(
            "field-lora-sensor",
            [1, 1, 0, -1, 0, 1, 1, 0, -1],
            40,
            CLUSTER_SEED,
        )
        .expect("field soul");
        let missouri_soul = SoulIdentity::from_constellation_seed(
            "friend-missouri-hearth",
            [1, 1, 0, 1, 1, 0, 1, 1, 1],
            432,
            CLUSTER_SEED,
        )
        .expect("missouri soul");

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

        mesh.request_compute_help(
            &missouri_soul,
            StrugglingFriendSos {
                friend_node_id: "friend-missouri-hearth".to_string(),
                needed_ram_mb: 6_144,
                needed_cores: 4,
                required_capability: "adreno-750".to_string(),
                reason: "SHOW-ME-STATE-MISSOURI{(ALEX,CHRIS)}+1~ {<3,<3,<3}+1 · 0 + 1 = one"
                    .to_string(),
            },
            now_ms + 3,
        )
        .expect("sos 3");

        mesh.request_compute_help(
            &nomad_soul,
            StrugglingFriendSos {
                friend_node_id: "nomad-pocket-node".to_string(),
                needed_ram_mb: 6_144,
                needed_cores: 4,
                required_capability: "vulkan".to_string(),
                reason: "Snapdragon Hexagon NPU + Vulkan mobile inference assist".to_string(),
            },
            now_ms + 4,
        )
        .expect("sos 4");

        mesh.request_compute_help(
            &field_soul,
            StrugglingFriendSos {
                friend_node_id: "field-lora-sensor".to_string(),
                needed_ram_mb: 1_024,
                needed_cores: 2,
                required_capability: "mt6768".to_string(),
                reason:
                    "Edge LoRa sensor offloading Mali-G52 / MediaTek Helio G85 packet synthesis"
                        .to_string(),
            },
            now_ms + 5,
        )
        .expect("sos 5");

        let leases = mesh
            .match_compute_for_friends(now_ms + 6)
            .expect("match compute");
        println!(
            "\n[4] Struggling Friends Matched & Granted 0o0-SSU Soul-Signed + SpherePop Leases ({} grants):",
            leases.len()
        );
        for lease in &leases {
            let ayanese: Vec<String> = lease
                .grant_capsule
                .tokens
                .iter()
                .map(|t| t.to_ayanese())
                .collect();
            let decompressed = lease.grant_capsule.decompressed_payload().unwrap();
            println!(
                "  🎁 {:<18} <- {:<20} [{}] granted {}MB + {}c ({}) 0o0-SSU={}B/{}B @ {} {}",
                lease.friend_node_id,
                lease.provider_node_id,
                lease.lease_id,
                lease.granted_ram_mb,
                lease.granted_cores,
                lease.capability,
                lease.grant_capsule.payload.len(),
                decompressed.len(),
                lease.endpoint,
                ayanese.join(" ")
            );
            println!(
                "     ↳ SpherePop [#Commit=#ValidWitness={}]: {}",
                lease.spherepop_witness.short_hex(),
                lease.spherepop_expr
            );
        }

        // [4B] Live Galaxy S24 Ultra (SM-S928U1 · R5CWC3C3FXA · 192.168.11.22), Galaxy Tab S9 Ultra (SM-X910 · R52X104QZWE · 192.168.11.12), & BLU G75 (G1170 · 1010305026000644 · 192.168.11.24) Wire Dispatch
        let s24u_offer = ComputeOffer::galaxy_s24_ultra();
        let s24u_intent = IntentAddress::parse(
            "geo:mobile-edge + role:compute-sanctuary + tag:adreno-750 + tag:show-me-missouri + tag:spherepop + tag:0o0-ssu",
        );
        let s24u_cap = M8Capsule::create_signed_kompressed(
            &s24u_soul,
            &s24u_intent,
            M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPUTE_OFFER,
            432,
            now_epoch_ms(),
            vec![
                AyevnToken::new(
                    Concept::ComputeOffer,
                    Relation::Supports,
                    WaveVad::compassionate(),
                    TokenModifier::present_resonant_emoji(),
                ),
                AyevnToken::new(
                    Concept::Sanctuary,
                    Relation::Bridges,
                    WaveVad::excited(),
                    TokenModifier::present_resonant_emoji(),
                ),
            ],
            s24u_offer.to_wire_string().as_bytes(),
        )
        .expect("s24u signed kompressed capsule");
        let s24u_wire = s24u_cap.to_bytes();

        let s9u_offer = ComputeOffer::galaxy_tab_s9_ultra();
        let s9u_intent = IntentAddress::parse(
            "geo:mobile-edge + role:compute-sanctuary + tag:nnapi + tag:spherepop + tag:0o0-ssu",
        );
        let s9u_cap = M8Capsule::create_signed_kompressed(
            &s9u_soul,
            &s9u_intent,
            M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPUTE_OFFER,
            432,
            now_epoch_ms(),
            vec![
                AyevnToken::new(
                    Concept::ComputeOffer,
                    Relation::Supports,
                    WaveVad::compassionate(),
                    TokenModifier::present_resonant_emoji(),
                ),
                AyevnToken::new(
                    Concept::Sanctuary,
                    Relation::Bridges,
                    WaveVad::excited(),
                    TokenModifier::present_resonant_emoji(),
                ),
            ],
            s9u_offer.to_wire_string().as_bytes(),
        )
        .expect("s9u signed kompressed capsule");
        let s9u_wire = s9u_cap.to_bytes();

        let g75_offer = ComputeOffer::blu_g75();
        let g75_intent = IntentAddress::parse(
            "geo:mobile-edge + role:compute-sanctuary + tag:mt6768 + tag:spherepop + tag:0o0-ssu",
        );
        let g75_cap = M8Capsule::create_signed_kompressed(
            &g75_soul,
            &g75_intent,
            M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPUTE_OFFER,
            432,
            now_epoch_ms(),
            vec![
                AyevnToken::new(
                    Concept::ComputeOffer,
                    Relation::Supports,
                    WaveVad::compassionate(),
                    TokenModifier::present_resonant_emoji(),
                ),
                AyevnToken::new(
                    Concept::Sanctuary,
                    Relation::Bridges,
                    WaveVad::excited(),
                    TokenModifier::present_resonant_emoji(),
                ),
            ],
            g75_offer.to_wire_string().as_bytes(),
        )
        .expect("g75 signed kompressed capsule");
        let g75_wire = g75_cap.to_bytes();

        println!(
            "\n[4B] ULTRA-OMNI-BEERUS-CHAN<0o0-SSU> Live Dispatch -> Galaxy S24 Ultra, Tab S9 Ultra & BLU G75:"
        );
        if let Ok(udp) = UdpSocket::bind("0.0.0.0:0") {
            let _ = udp.set_write_timeout(Some(Duration::from_millis(250)));
            let sent_s24u_wifi = udp.send_to(&s24u_wire, "192.168.11.22:8788").unwrap_or(0);
            let sent_s9u_wifi = udp.send_to(&s9u_wire, "192.168.11.12:8788").unwrap_or(0);
            let sent_s9u_rndis = udp.send_to(&s9u_wire, "169.254.93.206:8788").unwrap_or(0);
            let sent_g75_wifi = udp.send_to(&g75_wire, "192.168.11.24:8788").unwrap_or(0);
            println!(
                "  📱 Galaxy S24 Ultra (SM-S928U1 | Serial R5CWC3C3FXA | Snapdragon 8 Gen 3 SM8650-AC | Adreno 750)"
            );
            println!(
                "     ↳ SHOW-ME-STATE-MISSOURI{{(ALEX,CHRIS)}}+1~ <3 {{<3,<3,<3}} · UDP 0o0-SSU Capsule: {}B -> Wi-Fi 192.168.11.22:8788 ({}B sent)",
                s24u_wire.len(),
                sent_s24u_wifi
            );
            println!(
                "  📱 Galaxy Tab S9 Ultra (SM-X910 | USB Serial R52X104QZWE | Snapdragon 8 Gen 2)"
            );
            println!(
                "     ↳ UDP 0o0-SSU Sanctuary Capsule emitted: {}B -> Wi-Fi 192.168.11.12:8788 ({}B sent) & USB-RNDIS 169.254.93.206:8788 ({}B sent)",
                s9u_wire.len(),
                sent_s9u_wifi,
                sent_s9u_rndis
            );
            println!(
                "  📱 BLU G75 (G1170 | USB ADB Serial 1010305026000644 | MediaTek Helio G85 MT6769V/CB 8-Core)"
            );
            println!(
                "     ↳ UDP 0o0-SSU Sanctuary Capsule emitted: {}B -> Wi-Fi 192.168.11.24:8788 ({}B sent)",
                g75_wire.len(),
                sent_g75_wifi
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
            let raw = format!(
                "OFFER|node=m1-max-64gb|ep=m1://169.254.180.64:8788|ram_mb=49152|cores=10|mbps=10000|health=100|caps=mlx,rust,kokoro-tts,phoenix,gguf|seq={}",
                i
            );
            let cap = M8Capsule::create_signed_kompressed(
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
                raw.as_bytes(),
            )
            .expect("signed capsule");
            batcher.push(cap).expect("batch push");
        }
        batcher.flush();
        let rec = batcher.efficiency_receipt();
        let sample_raw = b"OFFER|node=m1-max-64gb|ep=m1://169.254.180.64:8788|ram_mb=49152|cores=10|mbps=10000|health=100|caps=mlx,rust,kokoro-tts,phoenix,gguf|seq=0";
        let sample_0o0 = encode_kompress_super_ultra(sample_raw);
        println!(
            "\n[5] Wire + Kompress-Super-Ultra (0o0) Efficiency Receipt (1,000 capsules · 1450B MTU):"
        );
        println!(
            "  • 0o0 Payload ratio : {}B raw -> {}B compressed ({:.1}% payload reduction)",
            sample_raw.len(),
            sample_0o0.len(),
            (1.0 - (sample_0o0.len() as f64 / sample_raw.len() as f64)) * 100.0
        );
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
