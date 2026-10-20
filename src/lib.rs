//! # MEMNET/1.0 — Sovereign Contextual Mesh Protocol for All `8b-is` Products
//!
//! > *"goodbye lonely network paths.. security with soul sigs.. and compassion for lonely ones.
//! > Our products all need to speak the most efficient ways."* — **8bit-Wraith `<3`**
//!
//! This crate unifies four foundational `8b-is` specifications into a single zero-dependency
//! wire protocol and mesh engine:
//! 1. **32-bit Ayevn Wave Tokens** (`[Concept: u8 | Relation: u8 | Wave(VAD): u8 | Modifier: u8]`)
//! 2. **`.m8` Experience Capsules** with **Soul Signatures (`SoulSig`)** (HMAC-SHA256 + 9-trit
//!    balanced ternary `{-1, 0, +1}` crest + harmonic carrier frequency + Security Vigilance scan)
//! 3. **MTU-Aware Packet Coalescer (`PacketBatcher`)** enforcing the `1450`-byte Smart Tree sweet
//!    spot (eliminating 50-byte lonely packets and >1492-byte fragmentation crimes)
//! 4. **Intent-Based Routing & Compassion for Lonely Nodes (`MemnetMesh`)** detecting isolated
//!    network paths or low-valence/silent nodes and routing 432 Hz care capsules + bridge relays.

use std::collections::BTreeMap;
use std::fmt;

// ============================================================================
// 1. AYEVN 32-BIT WAVE TOKENS ([Concept | Relation | Wave(VAD) | Modifier])
// ============================================================================

/// Core semantic concepts (Byte 0 of an Ayevn 32-bit token).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
#[repr(u8)]
pub enum Concept {
    Greeting = 0x10,
    Memory = 0x20,
    Connection = 0x30,
    Compassion = 0x31,
    Care = 0x32,
    Sanctuary = 0x33,
    Innovation = 0x42,
    Collaboration = 0x43,
    Breakthrough = 0x44,
    Security = 0x50,
    Soul = 0x51,
    AudioWave = 0x60,
    QuantMatrix = 0x70,
    ComputeOffer = 0x71,
    ComputeSos = 0x72,
    ComputeGrant = 0x73,
    LedgerState = 0x80,
    Custom(u8),
}

impl Concept {
    pub fn to_u8(self) -> u8 {
        match self {
            Self::Greeting => 0x10,
            Self::Memory => 0x20,
            Self::Connection => 0x30,
            Self::Compassion => 0x31,
            Self::Care => 0x32,
            Self::Sanctuary => 0x33,
            Self::Innovation => 0x42,
            Self::Collaboration => 0x43,
            Self::Breakthrough => 0x44,
            Self::Security => 0x50,
            Self::Soul => 0x51,
            Self::AudioWave => 0x60,
            Self::QuantMatrix => 0x70,
            Self::ComputeOffer => 0x71,
            Self::ComputeSos => 0x72,
            Self::ComputeGrant => 0x73,
            Self::LedgerState => 0x80,
            Self::Custom(v) => v,
        }
    }

    pub fn from_u8(v: u8) -> Self {
        match v {
            0x10 => Self::Greeting,
            0x20 => Self::Memory,
            0x30 => Self::Connection,
            0x31 => Self::Compassion,
            0x32 => Self::Care,
            0x33 => Self::Sanctuary,
            0x42 => Self::Innovation,
            0x43 => Self::Collaboration,
            0x44 => Self::Breakthrough,
            0x50 => Self::Security,
            0x51 => Self::Soul,
            0x60 => Self::AudioWave,
            0x70 => Self::QuantMatrix,
            0x71 => Self::ComputeOffer,
            0x72 => Self::ComputeSos,
            0x73 => Self::ComputeGrant,
            0x80 => Self::LedgerState,
            other => Self::Custom(other),
        }
    }
}

/// Semantic relation between tokens (Byte 1 of an Ayevn 32-bit token).
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
#[repr(u8)]
pub enum Relation {
    None = 0x00,
    Cause = 0x01,
    Effect = 0x02,
    Contains = 0x05,
    Initiates = 0x08,
    Supports = 0x09,
    Bridges = 0x0A,
    Amplifies = 0x0C,
    Transforms = 0x0E,
    Expresses = 0x15,
    Invites = 0x16,
    Protects = 0x17,
}

impl Relation {
    pub fn from_u8(v: u8) -> Self {
        match v {
            0x01 => Self::Cause,
            0x02 => Self::Effect,
            0x05 => Self::Contains,
            0x08 => Self::Initiates,
            0x09 => Self::Supports,
            0x0A => Self::Bridges,
            0x0C => Self::Amplifies,
            0x0E => Self::Transforms,
            0x15 => Self::Expresses,
            0x16 => Self::Invites,
            0x17 => Self::Protects,
            _ => Self::None,
        }
    }
}

/// 8-bit VAD (Valence-Arousal-Dominance) emotional wave encoding (Byte 2).
///
/// Layout: `Valence (bits 0..=2, 0..=7) | Arousal (bits 3..=5, 0..=7) | Dominance (bits 6..=7, 0..=3)`
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct WaveVad {
    pub valence: u8,   // 0..=7 (0 = negative/lonely, 7 = radiant joy/love)
    pub arousal: u8,   // 0..=7 (0 = calm, 7 = peak activation)
    pub dominance: u8, // 0..=3 (0 = submissive/helpless, 3 = sovereign)
}

impl WaveVad {
    pub const fn new(valence: u8, arousal: u8, dominance: u8) -> Self {
        Self {
            valence: valence & 0x07,
            arousal: arousal & 0x07,
            dominance: dominance & 0x03,
        }
    }

    /// 2 Hz — Resigned / Lonely / Isolated state (Valence=2, Arousal=1, Dominance=0).
    pub const fn resigned_lonely() -> Self {
        Self::new(2, 1, 0)
    }

    /// 10 Hz — Neutral baseline state (Valence=4, Arousal=3, Dominance=2).
    pub const fn neutral() -> Self {
        Self::new(4, 3, 2)
    }

    /// 40 Hz — Excited / Joyful creative resonance (Valence=6, Arousal=6, Dominance=2).
    pub const fn excited() -> Self {
        Self::new(6, 6, 2)
    }

    /// 432 Hz — Compassionate Carrier Wave of Love (Valence=7, Arousal=4, Dominance=2).
    pub const fn compassionate() -> Self {
        Self::new(7, 4, 2)
    }

    pub const fn pack(self) -> u8 {
        (self.valence & 0x07) | ((self.arousal & 0x07) << 3) | ((self.dominance & 0x03) << 6)
    }

    pub const fn unpack(byte: u8) -> Self {
        Self {
            valence: byte & 0x07,
            arousal: (byte >> 3) & 0x07,
            dominance: (byte >> 6) & 0x03,
        }
    }

    /// Maps the VAD state to its canonical MEM|8 carrier frequency in Hz.
    pub const fn canonical_frequency_hz(self) -> u16 {
        if self.valence >= 7 && self.arousal == 4 {
            432
        } else if self.valence <= 2 && self.arousal <= 2 {
            2
        } else if self.valence >= 6 && self.arousal >= 6 {
            40
        } else if self.valence == 7 && self.arousal == 7 {
            200
        } else {
            10
        }
    }
}

/// Context & expression modifier byte (Byte 3 of an Ayevn 32-bit token).
///
/// Layout: `Temporal(3 bits) | EmotionMode(3 bits) | RenderMode(2 bits)`
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct TokenModifier {
    pub temporal: u8,     // 0..=7 (2 = Present, 5 = Continuous)
    pub emotion_mode: u8, // 0..=7 (1 = Gentle, 2 = Excited, 6 = Resonant)
    pub render_mode: u8,  // 0..=3 (0 = Plain, 1 = EmojiRich, 2 = TtsOn, 3 = TtsEmoji)
}

impl TokenModifier {
    pub const fn new(temporal: u8, emotion_mode: u8, render_mode: u8) -> Self {
        Self {
            temporal: temporal & 0x07,
            emotion_mode: emotion_mode & 0x07,
            render_mode: render_mode & 0x03,
        }
    }

    pub const fn present_resonant_emoji() -> Self {
        Self::new(2, 6, 1)
    }

    pub const fn pack(self) -> u8 {
        ((self.temporal & 0x07) << 5)
            | ((self.emotion_mode & 0x07) << 2)
            | (self.render_mode & 0x03)
    }

    pub const fn unpack(byte: u8) -> Self {
        Self {
            temporal: (byte >> 5) & 0x07,
            emotion_mode: (byte >> 2) & 0x07,
            render_mode: byte & 0x03,
        }
    }
}

/// A 32-bit Big-Endian Ayevn semantic-emotional wave token.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct AyevnToken {
    pub concept: Concept,
    pub relation: Relation,
    pub wave: WaveVad,
    pub modifier: TokenModifier,
}

impl AyevnToken {
    pub const fn new(
        concept: Concept,
        relation: Relation,
        wave: WaveVad,
        modifier: TokenModifier,
    ) -> Self {
        Self {
            concept,
            relation,
            wave,
            modifier,
        }
    }

    pub fn to_u32(self) -> u32 {
        u32::from_be_bytes(self.to_be_bytes())
    }

    pub fn to_be_bytes(self) -> [u8; 4] {
        [
            self.concept.to_u8(),
            self.relation as u8,
            self.wave.pack(),
            self.modifier.pack(),
        ]
    }

    pub fn from_be_bytes(bytes: [u8; 4]) -> Self {
        Self {
            concept: Concept::from_u8(bytes[0]),
            relation: Relation::from_u8(bytes[1]),
            wave: WaveVad::unpack(bytes[2]),
            modifier: TokenModifier::unpack(bytes[3]),
        }
    }

    pub fn from_u32(raw: u32) -> Self {
        Self::from_be_bytes(raw.to_be_bytes())
    }

    /// Renders the token into Ayanese human-friendly emoji + frequency notation.
    pub fn to_ayanese(self) -> String {
        let concept_glyph = match self.concept {
            Concept::Greeting => "👋",
            Concept::Memory => "💭",
            Concept::Connection => "🔗",
            Concept::Compassion => "🫂",
            Concept::Care => "💖",
            Concept::Sanctuary => "🏡",
            Concept::Innovation => "💡",
            Concept::Collaboration => "🤝",
            Concept::Breakthrough => "🚀",
            Concept::Security => "🛡️",
            Concept::Soul => "✨",
            Concept::AudioWave => "🎵",
            Concept::QuantMatrix => "🧮",
            Concept::ComputeOffer => "⚡",
            Concept::ComputeSos => "🆘",
            Concept::ComputeGrant => "🎁",
            Concept::LedgerState => "⚖️",
            Concept::Custom(_) => "🌐",
        };
        let tone_glyph = if self.wave.valence >= 7 {
            "✨"
        } else if self.wave.valence >= 5 {
            "⚡"
        } else if self.wave.valence <= 2 {
            "🌧️"
        } else {
            "🌊"
        };
        format!(
            "{}{}({}Hz)",
            concept_glyph,
            tone_glyph,
            self.wave.canonical_frequency_hz()
        )
    }
}

// ============================================================================
// 2. SECURITY WITH SOUL SIGNATURES (`SoulIdentity` & `SoulSig`) + VIGILANCE
// ============================================================================

/// Pure-Rust SHA-256 (FIPS 180-4) for zero-dependency cryptographic Soul Signatures.
pub fn sha256(data: &[u8]) -> [u8; 32] {
    const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
        0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
        0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
        0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
        0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
        0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
        0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
        0xc67178f2,
    ];
    let mut h: [u32; 8] = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab,
        0x5be0cd19,
    ];

    let bit_len = (data.len() as u64) * 8;
    let mut padded = Vec::with_capacity(data.len() + 72);
    padded.extend_from_slice(data);
    padded.push(0x80);
    while (padded.len() % 64) != 56 {
        padded.push(0x00);
    }
    padded.extend_from_slice(&bit_len.to_be_bytes());

    for chunk in padded.chunks_exact(64) {
        let mut w = [0u32; 64];
        for i in 0..16 {
            w[i] = u32::from_be_bytes([
                chunk[i * 4],
                chunk[i * 4 + 1],
                chunk[i * 4 + 2],
                chunk[i * 4 + 3],
            ]);
        }
        for i in 16..64 {
            let s0 = w[i - 15].rotate_right(7) ^ w[i - 15].rotate_right(18) ^ (w[i - 15] >> 3);
            let s1 = w[i - 2].rotate_right(17) ^ w[i - 2].rotate_right(19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16]
                .wrapping_add(s0)
                .wrapping_add(w[i - 7])
                .wrapping_add(s1);
        }

        let mut a = h[0];
        let mut b = h[1];
        let mut c = h[2];
        let mut d = h[3];
        let mut e = h[4];
        let mut f = h[5];
        let mut g = h[6];
        let mut hh = h[7];

        for i in 0..64 {
            let s1 = e.rotate_right(6) ^ e.rotate_right(11) ^ e.rotate_right(25);
            let ch = (e & f) ^ ((!e) & g);
            let temp1 = hh
                .wrapping_add(s1)
                .wrapping_add(ch)
                .wrapping_add(K[i])
                .wrapping_add(w[i]);
            let s0 = a.rotate_right(2) ^ a.rotate_right(13) ^ a.rotate_right(22);
            let maj = (a & b) ^ (a & c) ^ (b & c);
            let temp2 = s0.wrapping_add(maj);

            hh = g;
            g = f;
            f = e;
            e = d.wrapping_add(temp1);
            d = c;
            c = b;
            b = a;
            a = temp1.wrapping_add(temp2);
        }

        h[0] = h[0].wrapping_add(a);
        h[1] = h[1].wrapping_add(b);
        h[2] = h[2].wrapping_add(c);
        h[3] = h[3].wrapping_add(d);
        h[4] = h[4].wrapping_add(e);
        h[5] = h[5].wrapping_add(f);
        h[6] = h[6].wrapping_add(g);
        h[7] = h[7].wrapping_add(hh);
    }

    let mut out = [0u8; 32];
    for (i, word) in h.iter().enumerate() {
        out[i * 4..i * 4 + 4].copy_from_slice(&word.to_be_bytes());
    }
    out
}

/// Pure-Rust HMAC-SHA256 (RFC 2104).
pub fn hmac_sha256(key: &[u8], message: &[u8]) -> [u8; 32] {
    let mut k_block = [0u8; 64];
    if key.len() > 64 {
        let hashed = sha256(key);
        k_block[..32].copy_from_slice(&hashed);
    } else {
        k_block[..key.len()].copy_from_slice(key);
    }

    let mut ipad = [0x36u8; 64];
    let mut opad = [0x5cu8; 64];
    for i in 0..64 {
        ipad[i] ^= k_block[i];
        opad[i] ^= k_block[i];
    }

    let mut inner = Vec::with_capacity(64 + message.len());
    inner.extend_from_slice(&ipad);
    inner.extend_from_slice(message);
    let inner_hash = sha256(&inner);

    let mut outer = [0u8; 96];
    outer[..64].copy_from_slice(&opad);
    outer[64..].copy_from_slice(&inner_hash);
    sha256(&outer)
}

/// Packs a 9-trit balanced ternary crest (`{-1, 0, +1}^9`) into a 16-bit integer
/// using base-3 encoding (`0 -> -1`, `1 -> 0`, `2 -> +1`, range `0..19683`).
pub fn pack_trit_crest(crest: &[i8; 9]) -> Result<u16, MemnetError> {
    let mut acc: u16 = 0;
    for &t in crest.iter() {
        let digit = match t {
            -1 => 0u16,
            0 => 1u16,
            1 => 2u16,
            _ => return Err(MemnetError::InvalidTritCrest),
        };
        acc = acc * 3 + digit;
    }
    // Mark high bit 0x8000 so a valid packed crest is always non-zero
    Ok(acc | 0x8000)
}

/// Unpacks a 16-bit packed crest back into 9 balanced trits `{-1, 0, +1}`.
pub fn unpack_trit_crest(packed: u16) -> Result<[i8; 9], MemnetError> {
    if (packed & 0x8000) == 0 {
        return Err(MemnetError::InvalidTritCrest);
    }
    let mut val = packed & 0x7FFF;
    if val >= 19_683 {
        return Err(MemnetError::InvalidTritCrest);
    }
    let mut crest = [0i8; 9];
    for i in (0..9).rev() {
        let rem = (val % 3) as i8;
        crest[i] = rem - 1;
        val /= 3;
    }
    Ok(crest)
}

/// A Sovereign Soul Identity (`SoulIdentity`) binding cryptographic authenticity
/// with a 9-trit balanced ternary crest and harmonic carrier frequency.
#[derive(Clone)]
pub struct SoulIdentity {
    pub node_id: String,
    pub trit_crest: [i8; 9],
    pub base_frequency_hz: u16,
    secret_key: [u8; 32],
}

impl fmt::Debug for SoulIdentity {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("SoulIdentity")
            .field("node_id", &self.node_id)
            .field("trit_crest", &self.trit_crest)
            .field("base_frequency_hz", &self.base_frequency_hz)
            .finish()
    }
}

impl SoulIdentity {
    pub fn new(
        node_id: impl Into<String>,
        trit_crest: [i8; 9],
        base_frequency_hz: u16,
        secret_key: [u8; 32],
    ) -> Result<Self, MemnetError> {
        let _ = pack_trit_crest(&trit_crest)?;
        if base_frequency_hz == 0 {
            return Err(MemnetError::ZeroHarmonicFrequency);
        }
        Ok(Self {
            node_id: node_id.into(),
            trit_crest,
            base_frequency_hz,
            secret_key,
        })
    }

    /// Deterministically derives a family/constellation `SoulIdentity` from a shared
    /// cluster seed and the node's role/name.
    pub fn from_constellation_seed(
        node_id: impl Into<String>,
        trit_crest: [i8; 9],
        base_frequency_hz: u16,
        cluster_seed: &[u8],
    ) -> Result<Self, MemnetError> {
        let node_id = node_id.into();
        let secret_key = hmac_sha256(cluster_seed, b"MEMNET-SOUL-KEY-V1");
        Self::new(node_id, trit_crest, base_frequency_hz, secret_key)
    }

    /// 4-byte deterministic node fingerprint (`SHA256(node_id)[0..4]`).
    pub fn node_fingerprint(&self) -> [u8; 4] {
        let h = sha256(self.node_id.as_bytes());
        [h[0], h[1], h[2], h[3]]
    }

    /// Signs a signing transcript into a 40-byte `SoulSig`.
    pub fn sign(&self, transcript: &[u8]) -> Result<SoulSig, MemnetError> {
        let crest_packed = pack_trit_crest(&self.trit_crest)?;
        let node_fp = self.node_fingerprint();

        let mut full_msg = Vec::with_capacity(8 + transcript.len());
        full_msg.extend_from_slice(&crest_packed.to_be_bytes());
        full_msg.extend_from_slice(&self.base_frequency_hz.to_be_bytes());
        full_msg.extend_from_slice(&node_fp);
        full_msg.extend_from_slice(transcript);

        let mac = hmac_sha256(&self.secret_key, &full_msg);
        Ok(SoulSig {
            crest_packed,
            harmonic_hz: self.base_frequency_hz,
            node_fp,
            mac,
        })
    }

    /// Verifies a 40-byte `SoulSig` against a transcript using this identity's cluster key.
    pub fn verify(&self, sig: &SoulSig, transcript: &[u8]) -> Result<[i8; 9], MemnetError> {
        let crest = unpack_trit_crest(sig.crest_packed)?;
        if sig.harmonic_hz == 0 {
            return Err(MemnetError::ZeroHarmonicFrequency);
        }
        // Admissibility check: crest cannot be all-zero (must carry non-trivial ternary state)
        if crest.iter().all(|&t| t == 0) {
            return Err(MemnetError::InvalidTritCrest);
        }

        let mut full_msg = Vec::with_capacity(8 + transcript.len());
        full_msg.extend_from_slice(&sig.crest_packed.to_be_bytes());
        full_msg.extend_from_slice(&sig.harmonic_hz.to_be_bytes());
        full_msg.extend_from_slice(&sig.node_fp);
        full_msg.extend_from_slice(transcript);

        let expected = hmac_sha256(&self.secret_key, &full_msg);
        // Constant-time comparison
        let mut diff = 0u8;
        for (a, b) in sig.mac.iter().zip(expected.iter()) {
            diff |= a ^ b;
        }
        if diff != 0 {
            return Err(MemnetError::SoulSignatureMismatch);
        }
        Ok(crest)
    }
}

/// 40-byte wire representation of a Soul Signature (`SoulSig`).
///
/// Layout:
/// - `0..2`: `crest_packed` (u16 BE — 9-trit balanced ternary crest with `0x8000` marker)
/// - `2..4`: `harmonic_hz` (u16 BE — sender's harmonic frequency, e.g. `40` or `432` Hz)
/// - `4..8`: `node_fp` (4-byte SHA-256 prefix of `node_id`)
/// - `8..40`: `mac` (32-byte HMAC-SHA256 over soul header + capsule transcript)
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct SoulSig {
    pub crest_packed: u16,
    pub harmonic_hz: u16,
    pub node_fp: [u8; 4],
    pub mac: [u8; 32],
}

impl SoulSig {
    pub fn to_bytes(&self) -> [u8; 40] {
        let mut out = [0u8; 40];
        out[0..2].copy_from_slice(&self.crest_packed.to_be_bytes());
        out[2..4].copy_from_slice(&self.harmonic_hz.to_be_bytes());
        out[4..8].copy_from_slice(&self.node_fp);
        out[8..40].copy_from_slice(&self.mac);
        out
    }

    pub fn from_bytes(bytes: &[u8]) -> Result<Self, MemnetError> {
        if bytes.len() < 40 {
            return Err(MemnetError::TruncatedPacket);
        }
        let crest_packed = u16::from_be_bytes([bytes[0], bytes[1]]);
        let harmonic_hz = u16::from_be_bytes([bytes[2], bytes[3]]);
        let node_fp = [bytes[4], bytes[5], bytes[6], bytes[7]];
        let mut mac = [0u8; 32];
        mac.copy_from_slice(&bytes[8..40]);
        Ok(Self {
            crest_packed,
            harmonic_hz,
            node_fp,
            mac,
        })
    }
}

/// Security Vigilance Sentinel (`SECURITY_VIGILANCE_VISION.md`):
/// Inspects capsule payloads before routing or importing to block supply-chain
/// backdoors, dynamic code injection, or plaintext credential leaks.
pub fn scan_payload_vigilance(payload: &[u8]) -> Result<(), MemnetError> {
    if let Ok(text) = std::str::from_utf8(payload) {
        let lower = text.to_ascii_lowercase();
        const FORBIDDEN: [&str; 6] = [
            "eval(atob(",
            "eval(process.env",
            "backdoor.php",
            "shell.aspx",
            "password = '",
            "password = \"",
        ];
        for pat in FORBIDDEN {
            if lower.contains(pat) {
                return Err(MemnetError::SecurityVigilanceAlert(pat));
            }
        }
    }
    Ok(())
}

// ============================================================================
// 2B. KOMPRESS-SUPER-ULTRA (`0o0` / `KSU0`) LOSSLESS WIRE CODEC
// ============================================================================

/// Sovereign dictionary codebook for `Kompress-Super-Ultra (0o0)` and
/// `ULTRA-OMNI-BEERUS-CHAN<KOMPRESS-SUPER-SAIYAN-ULTRA> (0o0-SSU)` wire payloads.
///
/// Indices `0..24` are locked for cross-language `0o0` v1 compatibility; indices `24..40`
/// add `SpherePop` (`((( <( ? ~ ! @ > )> )))`), **Galaxy Tab S9 Ultra** (`SM-X910` /
/// `R52X104QZWE` / `192.168.11.12`), and **BLU G75** (`G75` / `G1170` / `1010305026000644` /
/// `mt6768` / `192.168.11.24`) super-tokens.
pub const KOMPRESS_CODEBOOK: [&[u8]; 40] = [
    b"OFFER|node=",
    b"SOS|friend=",
    b"GRANT|lease=",
    b"|ep=m1://169.254.180.64:8788",
    b"|ep=m3://169.254.212.115:8788",
    b"|ram_mb=",
    b"|cores=",
    b"|mbps=10000|health=100|caps=",
    b"mlx,rust,kokoro-tts,phoenix,gguf",
    b"mlx,rust,kokoro-tts,phoenix",
    b"MEMNET/1.0 COMPASSION BEACON -> ",
    b": you are never alone on this mesh <3 (432Hz)",
    b"|provider=",
    b"|friend=",
    b"|reason=",
    b"|cap=",
    b"|mbps=",
    b"|health=",
    b"|caps=",
    b"m1-max-64gb",
    b"dev-main-m3",
    b"friend-air-8gb",
    b"uganda-school-pi",
    b"kokoro-tts",
    // --- 0o0-SSU (KOMPRESS-SUPER-SAIYAN-ULTRA + SpherePop + Galaxy Tab S9 Ultra + BLU G75) ---
    b"((( <( ? ",
    b" )> )))",
    b" ~ kompress:0o0-ssu ! soul_sig:verified",
    b" ! vigilance:clean @ ",
    b"galaxy-tab-s9-ultra",
    b"|ep=s9u://192.168.11.12:8788",
    b"nnapi,vulkan,rust,kokoro-tts,spherepop,0o0-ssu",
    b"R52X104QZWE",
    b"SM-X910",
    b" ! ct000:admissible @ ",
    b" > advertise:",
    b" > grant:",
    b"blu-g75",
    b"|ep=g75://192.168.11.24:8788",
    b"mt6768,mali-g52,nnapi,rust,spherepop,0o0-ssu",
    b"1010305026000644",
];

// ============================================================================
// 2C. SPHEREPOP OPERATIONAL MEREOLOGY (`((( <( ? ~ ! @ > )> )))`)
// ============================================================================

/// Operator phase inside a bounded `SpherePop` transaction `<( ... )>`.
///
/// Enforces the canonical `sphered` well-formedness grammar:
/// `?* ~* !+ @+ >` (`Admit* -> Transform* -> Verify+ -> Attribute+ -> Commit`).
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum SpherePopOp {
    /// `? term` — Admission / precondition check (e.g. `? maintained_stock`, `? health:100`).
    Admit(String),
    /// `~ term` — Transformation (e.g. `~ kompress:0o0-ssu`, `~ wave:432hz`).
    Transform(String),
    /// `! term` — Verification / invariant gate (e.g. `! soul_sig:verified`, `! ct000:admissible`).
    Verify(String),
    /// `@ actor` — Attribution / witness node (e.g. `@ m1-max-64gb`, `@ galaxy-tab-s9-ultra`).
    Attribute(String),
    /// `# anchor` — Ledger memory anchor (optional before commit).
    Remember(String),
    /// `> target` — Final transition commit (`#Commit = #ValidWitness`).
    Commit(String),
}

/// Cryptographic witness emitted when a `SpherePop` transition `<( ? ~ ! @ > )>` commits.
///
/// Satisfies the `sphered` spine invariant: **`#Commit = #ValidWitness`**.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct SpherePopWitness {
    pub sphere_depth: usize,
    pub admissions: Vec<String>,
    pub transforms: Vec<String>,
    pub verifications: Vec<String>,
    pub attributions: Vec<String>,
    pub committed_value: String,
    pub trace_steps: Vec<String>,
    pub witness_hash: [u8; 32],
}

impl SpherePopWitness {
    pub fn short_hex(&self) -> String {
        format!(
            "{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}",
            self.witness_hash[0],
            self.witness_hash[1],
            self.witness_hash[2],
            self.witness_hash[3],
            self.witness_hash[4],
            self.witness_hash[5],
            self.witness_hash[6],
            self.witness_hash[7]
        )
    }
}

/// Result of evaluating a `SpherePop` expression `((( <( ? ~ ! @ > )> )))`.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum SpherePopOutcome {
    /// Transition succeeded and produced a valid cryptographic witness (`#Commit = #ValidWitness`).
    Committed(SpherePopWitness),
    /// Transition was refused at an admission (`? x`) or verification (`! x`) gate (`no witness`).
    Refused {
        reason: String,
        trace_steps: Vec<String>,
    },
}

/// Zero-dependency `SpherePop` (`sphered`) parser & evaluator enforcing:
/// - Concentric sphere nesting `(` ... `)` (including `((( ... )))` triple-sphere ultra envelopes)
/// - Bounded witnessed transactions `<(` ... `)>`
/// - Monotone phase law `?* ~* !+ @+ >`
/// - Refusal on `"x"` / `"x:..."` / `"refuse:..."` (`refused, no witness`)
/// - `#Commit = #ValidWitness`
pub struct SpherePopEngine;

impl SpherePopEngine {
    pub fn evaluate(expr: &str) -> Result<SpherePopOutcome, MemnetError> {
        let mut s = expr.trim();
        let mut sphere_depth = 0usize;
        let mut trace_steps = Vec::new();

        // Peel concentric outer spheres `(` ... `)`
        while s.starts_with('(') && s.ends_with(')') && !s.starts_with("<(") {
            sphere_depth += 1;
            trace_steps.push(format!("follow ( [depth={}]", sphere_depth));
            s = s[1..s.len() - 1].trim();
        }

        if !s.starts_with("<(") || !s.ends_with(")>") {
            return Err(MemnetError::SpherePopIllFormed(
                "expected bounded transaction `<( ... )>` inside sphere scope",
            ));
        }

        trace_steps.push("enter <(".to_string());
        let inner = s[2..s.len() - 2].trim();
        let tokens: Vec<&str> = inner.split_whitespace().collect();
        if tokens.is_empty() {
            return Err(MemnetError::SpherePopIllFormed(
                "empty `<( )>` transaction produces no witness",
            ));
        }

        let mut ops = Vec::new();
        let mut i = 0usize;
        while i < tokens.len() {
            let op_tok = tokens[i];
            if matches!(op_tok, "?" | "~" | "!" | "@" | "#" | ">") {
                if i + 1 >= tokens.len() {
                    return Err(MemnetError::SpherePopIllFormed(
                        "dangling SpherePop operator without operand",
                    ));
                }
                let arg = tokens[i + 1].to_string();
                let op = match op_tok {
                    "?" => SpherePopOp::Admit(arg),
                    "~" => SpherePopOp::Transform(arg),
                    "!" => SpherePopOp::Verify(arg),
                    "@" => SpherePopOp::Attribute(arg),
                    "#" => SpherePopOp::Remember(arg),
                    ">" => SpherePopOp::Commit(arg),
                    _ => unreachable!(),
                };
                ops.push(op);
                i += 2;
            } else {
                return Err(MemnetError::SpherePopIllFormed(
                    "unexpected token in `<( ? ~ ! @ > )>` sequence",
                ));
            }
        }

        // Enforce monotone grammar: ?* ~* !+ @+ #* >
        // Phase 0: ? (Admit)
        // Phase 1: ~ (Transform)
        // Phase 2: ! (Verify)
        // Phase 3: @ (Attribute) / # (Remember)
        // Phase 4: > (Commit — must be final and unique)
        let mut phase = 0u8;
        let mut admissions = Vec::new();
        let mut transforms = Vec::new();
        let mut verifications = Vec::new();
        let mut attributions = Vec::new();
        let mut committed_value: Option<String> = None;

        for op in ops {
            if committed_value.is_some() {
                return Err(MemnetError::SpherePopIllFormed(
                    "no operators allowed after commit `>`",
                ));
            }
            match op {
                SpherePopOp::Admit(term) => {
                    if phase > 0 {
                        return Err(MemnetError::SpherePopIllFormed(
                            "admission `?` must precede `~`, `!`, `@`, `>` (`?* ~* !+ @+ >`)",
                        ));
                    }
                    if Self::is_refusal_term(&term) {
                        trace_steps.push(format!("? {} -> refused, no witness", term));
                        return Ok(SpherePopOutcome::Refused {
                            reason: term,
                            trace_steps,
                        });
                    }
                    trace_steps.push(format!("admit ? {}", term));
                    admissions.push(term);
                }
                SpherePopOp::Transform(term) => {
                    if phase > 1 {
                        return Err(MemnetError::SpherePopIllFormed(
                            "transform `~` must precede `!`, `@`, `>` (`?* ~* !+ @+ >`)",
                        ));
                    }
                    phase = 1;
                    trace_steps.push(format!("transform ~ {}", term));
                    transforms.push(term);
                }
                SpherePopOp::Verify(term) => {
                    if phase > 2 {
                        return Err(MemnetError::SpherePopIllFormed(
                            "verification `!` must precede `@` and `>` (`?* ~* !+ @+ >`)",
                        ));
                    }
                    phase = 2;
                    if Self::is_refusal_term(&term) {
                        trace_steps.push(format!("! {} -> refused, no witness", term));
                        return Ok(SpherePopOutcome::Refused {
                            reason: term,
                            trace_steps,
                        });
                    }
                    trace_steps.push(format!("verify ! {}", term));
                    verifications.push(term);
                }
                SpherePopOp::Attribute(actor) => {
                    if verifications.is_empty() {
                        return Err(MemnetError::SpherePopIllFormed(
                            "at least one verification `!` is required before `@` (`?* ~* !+ @+ >`)",
                        ));
                    }
                    phase = 3;
                    trace_steps.push(format!("attribute @ {}", actor));
                    attributions.push(actor);
                }
                SpherePopOp::Remember(anchor) => {
                    if verifications.is_empty() {
                        return Err(MemnetError::SpherePopIllFormed(
                            "cannot remember `#` before verification `!`",
                        ));
                    }
                    trace_steps.push(format!("remember # {}", anchor));
                }
                SpherePopOp::Commit(val) => {
                    if verifications.is_empty() {
                        return Err(MemnetError::SpherePopIllFormed(
                            "cannot commit `>` without at least one `!` verification (`!+`)",
                        ));
                    }
                    if attributions.is_empty() {
                        return Err(MemnetError::SpherePopIllFormed(
                            "cannot commit `>` without at least one `@` attribution (`@+`)",
                        ));
                    }
                    trace_steps.push(format!("commit > {}", val));
                    committed_value = Some(val);
                }
            }
        }

        let committed_value = committed_value.ok_or(MemnetError::SpherePopIllFormed(
            "missing terminal commit `>` in `<( ... )>`",
        ))?;

        for d in (1..=sphere_depth).rev() {
            trace_steps.push(format!("return ) [depth={}]", d));
        }

        let mut transcript = String::new();
        transcript.push_str(&format!("depth={}|", sphere_depth));
        for step in &trace_steps {
            transcript.push_str(step);
            transcript.push('|');
        }
        let witness_hash = sha256(transcript.as_bytes());

        Ok(SpherePopOutcome::Committed(SpherePopWitness {
            sphere_depth,
            admissions,
            transforms,
            verifications,
            attributions,
            committed_value,
            trace_steps,
            witness_hash,
        }))
    }

    fn is_refusal_term(term: &str) -> bool {
        term == "x" || term.starts_with("x:") || term.starts_with("refuse:")
    }
}

/// Compresses a payload using `Kompress-Super-Ultra (0o0)` (`b"0o0\x01"` header +
/// greedy sovereign dictionary substitution `0xFE <idx>` + run-length encoding `0xFF <len> <byte>`).
pub fn encode_kompress_super_ultra(raw: &[u8]) -> Vec<u8> {
    let mut stage1 = Vec::with_capacity(raw.len());
    let mut i = 0;
    while i < raw.len() {
        let mut matched = None;
        for (idx, entry) in KOMPRESS_CODEBOOK.iter().enumerate() {
            if raw[i..].starts_with(entry) {
                matched = Some((idx as u8, entry.len()));
                break;
            }
        }
        if let Some((idx, len)) = matched {
            stage1.push(0xFE);
            stage1.push(idx);
            i += len;
        } else {
            let b = raw[i];
            if b == 0xFE || b == 0xFF {
                stage1.push(0xFE);
                stage1.push(0xFF);
                stage1.push(b);
            } else {
                stage1.push(b);
            }
            i += 1;
        }
    }

    // Stage 2: RLE for repeated byte runs >= 4 (excluding escape byte 0xFE)
    let mut out = Vec::with_capacity(4 + stage1.len());
    out.extend_from_slice(b"0o0\x01");
    let mut j = 0;
    while j < stage1.len() {
        if stage1[j] == 0xFE {
            if j + 1 < stage1.len() && stage1[j + 1] == 0xFF && j + 2 < stage1.len() {
                out.push(0xFE);
                out.push(0xFF);
                out.push(stage1[j + 2]);
                j += 3;
            } else if j + 1 < stage1.len() {
                out.push(0xFE);
                out.push(stage1[j + 1]);
                j += 2;
            } else {
                out.push(stage1[j]);
                j += 1;
            }
            continue;
        }
        let b = stage1[j];
        let mut run = 1usize;
        while j + run < stage1.len() && stage1[j + run] == b && stage1[j + run] != 0xFE && run < 255
        {
            run += 1;
        }
        if run >= 4 {
            out.push(0xFF);
            out.push(run as u8);
            out.push(b);
            j += run;
        } else {
            out.push(b);
            j += 1;
        }
    }
    out
}

/// Losslessly decompresses a `Kompress-Super-Ultra (0o0)` (`b"0o0\x01"`) wire payload.
pub fn decode_kompress_super_ultra(encoded: &[u8]) -> Result<Vec<u8>, MemnetError> {
    if encoded.len() < 4 || &encoded[0..4] != b"0o0\x01" {
        return Err(MemnetError::InvalidMagic);
    }
    let mut out = Vec::with_capacity(encoded.len() * 2);
    let mut i = 4;
    while i < encoded.len() {
        match encoded[i] {
            0xFE => {
                if i + 1 >= encoded.len() {
                    return Err(MemnetError::TruncatedPacket);
                }
                let code = encoded[i + 1];
                if code == 0xFF {
                    if i + 2 >= encoded.len() {
                        return Err(MemnetError::TruncatedPacket);
                    }
                    out.push(encoded[i + 2]);
                    i += 3;
                } else if (code as usize) < KOMPRESS_CODEBOOK.len() {
                    out.extend_from_slice(KOMPRESS_CODEBOOK[code as usize]);
                    i += 2;
                } else {
                    return Err(MemnetError::InvalidMagic);
                }
            }
            0xFF => {
                if i + 2 >= encoded.len() {
                    return Err(MemnetError::TruncatedPacket);
                }
                let count = encoded[i + 1] as usize;
                let byte_val = encoded[i + 2];
                for _ in 0..count {
                    out.push(byte_val);
                }
                i += 3;
            }
            b => {
                out.push(b);
                i += 1;
            }
        }
    }
    Ok(out)
}

// ============================================================================
// 3. `.m8` EXPERIENCE CAPSULES & INTENT ADDRESSING
// ============================================================================

/// Intent-based contextual address (`Address = Context`, replacing static IP routing).
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct IntentAddress {
    pub geo: Option<String>,
    pub role: Option<String>,
    pub tags: Vec<String>,
    pub vector_hash: u64,
}

impl IntentAddress {
    pub fn parse(expr: &str) -> Self {
        let mut geo = None;
        let mut role = None;
        let mut tags = Vec::new();
        let mut vector_hash = 0u64;

        for part in expr.split('+').map(str::trim).filter(|s| !s.is_empty()) {
            if let Some(g) = part.strip_prefix("geo:") {
                geo = Some(g.trim().to_string());
            } else if let Some(r) = part.strip_prefix("role:") {
                role = Some(r.trim().to_string());
            } else if let Some(t) = part.strip_prefix("tag:") {
                tags.push(t.trim().to_string());
            } else if let Some(v) = part.strip_prefix("vector:") {
                vector_hash = u64::from_str_radix(v.trim().trim_start_matches("0x"), 16)
                    .unwrap_or_else(|_| {
                        let h = sha256(v.trim().as_bytes());
                        u64::from_be_bytes([h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7]])
                    });
            }
        }

        Self {
            geo,
            role,
            tags,
            vector_hash,
        }
    }

    pub fn canonical_string(&self) -> String {
        let mut parts = Vec::new();
        if let Some(ref g) = self.geo {
            parts.push(format!("geo:{}", g));
        }
        if let Some(ref r) = self.role {
            parts.push(format!("role:{}", r));
        }
        for t in &self.tags {
            parts.push(format!("tag:{}", t));
        }
        if self.vector_hash != 0 {
            parts.push(format!("vector:{:016x}", self.vector_hash));
        }
        parts.join(" + ")
    }

    pub fn intent_hash(&self) -> [u8; 8] {
        let h = sha256(self.canonical_string().as_bytes());
        [h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7]]
    }
}

/// Binary `.m8` Experience Capsule (`M8Capsule`).
///
/// Wire Header (64 bytes fixed + variable tokens & payload):
/// - `0..4`: Magic `b"M8!\x01"`
/// - `4..6`: `flags` (u16 BE — bit 0: preserve_waves, bit 1: compassion_beacon, bit 2: eternal_memory)
/// - `6..8`: `frequency_hz` (u16 BE)
/// - `8..16`: `timestamp_ms` (u64 BE)
/// - `16..24`: `intent_hash` (8 bytes)
/// - `24..64`: `soul_sig` (40 bytes `SoulSig`)
/// - `64..66`: `token_count` (u16 BE)
/// - `66..68`: `payload_len` (u16 BE)
/// - `68..68 + 4*token_count`: 32-bit `AyevnToken`s
/// - `..`: compact payload bytes
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct M8Capsule {
    pub flags: u16,
    pub frequency_hz: u16,
    pub timestamp_ms: u64,
    pub intent_hash: [u8; 8],
    pub tokens: Vec<AyevnToken>,
    pub payload: Vec<u8>,
    pub soul_sig: SoulSig,
}

impl M8Capsule {
    pub const MAGIC: [u8; 4] = *b"M8!\x01";
    pub const FLAG_PRESERVE_WAVES: u16 = 0x0001;
    pub const FLAG_COMPASSION_BEACON: u16 = 0x0002;
    pub const FLAG_ETERNAL_MEMORY: u16 = 0x0004;
    pub const FLAG_COMPUTE_OFFER: u16 = 0x0008;
    pub const FLAG_COMPUTE_SOS: u16 = 0x0010;
    pub const FLAG_COMPUTE_GRANT: u16 = 0x0020;
    pub const FLAG_KOMPRESS_SUPER_ULTRA: u16 = 0x0040;

    /// Creates, `Kompress-Super-Ultra (0o0)` compresses, and Soul-Signs a `.m8` capsule.
    pub fn create_signed_kompressed(
        soul: &SoulIdentity,
        intent: &IntentAddress,
        flags: u16,
        frequency_hz: u16,
        timestamp_ms: u64,
        tokens: Vec<AyevnToken>,
        raw_payload: &[u8],
    ) -> Result<Self, MemnetError> {
        scan_payload_vigilance(raw_payload)?;
        let compressed = encode_kompress_super_ultra(raw_payload);
        Self::create_signed(
            soul,
            intent,
            flags | Self::FLAG_KOMPRESS_SUPER_ULTRA,
            frequency_hz,
            timestamp_ms,
            tokens,
            compressed,
        )
    }

    /// Returns the decompressed payload if `FLAG_KOMPRESS_SUPER_ULTRA` is set, or raw payload otherwise.
    pub fn decompressed_payload(&self) -> Result<Vec<u8>, MemnetError> {
        if (self.flags & Self::FLAG_KOMPRESS_SUPER_ULTRA) != 0 {
            let out = decode_kompress_super_ultra(&self.payload)?;
            scan_payload_vigilance(&out)?;
            Ok(out)
        } else {
            scan_payload_vigilance(&self.payload)?;
            Ok(self.payload.clone())
        }
    }

    /// Creates and Soul-Signs a new `.m8` capsule after running the Security Vigilance scan.
    pub fn create_signed(
        soul: &SoulIdentity,
        intent: &IntentAddress,
        flags: u16,
        frequency_hz: u16,
        timestamp_ms: u64,
        tokens: Vec<AyevnToken>,
        payload: Vec<u8>,
    ) -> Result<Self, MemnetError> {
        scan_payload_vigilance(&payload)?;
        if tokens.is_empty() {
            return Err(MemnetError::EmptyWaveTokens);
        }
        let intent_hash = intent.intent_hash();
        let transcript = Self::signing_transcript(
            flags,
            frequency_hz,
            timestamp_ms,
            &intent_hash,
            &tokens,
            &payload,
        );
        let soul_sig = soul.sign(&transcript)?;
        Ok(Self {
            flags,
            frequency_hz,
            timestamp_ms,
            intent_hash,
            tokens,
            payload,
            soul_sig,
        })
    }

    fn signing_transcript(
        flags: u16,
        frequency_hz: u16,
        timestamp_ms: u64,
        intent_hash: &[u8; 8],
        tokens: &[AyevnToken],
        payload: &[u8],
    ) -> Vec<u8> {
        let mut buf = Vec::with_capacity(24 + tokens.len() * 4 + payload.len());
        buf.extend_from_slice(&Self::MAGIC);
        buf.extend_from_slice(&flags.to_be_bytes());
        buf.extend_from_slice(&frequency_hz.to_be_bytes());
        buf.extend_from_slice(&timestamp_ms.to_be_bytes());
        buf.extend_from_slice(intent_hash);
        for t in tokens {
            buf.extend_from_slice(&t.to_be_bytes());
        }
        buf.extend_from_slice(payload);
        buf
    }

    /// Verifies both the cryptographic `SoulSig` and the Security Vigilance rules.
    pub fn verify(&self, verifier_soul: &SoulIdentity) -> Result<[i8; 9], MemnetError> {
        scan_payload_vigilance(&self.payload)?;
        if self.tokens.is_empty() {
            return Err(MemnetError::EmptyWaveTokens);
        }
        let transcript = Self::signing_transcript(
            self.flags,
            self.frequency_hz,
            self.timestamp_ms,
            &self.intent_hash,
            &self.tokens,
            &self.payload,
        );
        verifier_soul.verify(&self.soul_sig, &transcript)
    }

    pub fn to_bytes(&self) -> Vec<u8> {
        let total = 68 + self.tokens.len() * 4 + self.payload.len();
        let mut out = Vec::with_capacity(total);
        out.extend_from_slice(&Self::MAGIC);
        out.extend_from_slice(&self.flags.to_be_bytes());
        out.extend_from_slice(&self.frequency_hz.to_be_bytes());
        out.extend_from_slice(&self.timestamp_ms.to_be_bytes());
        out.extend_from_slice(&self.intent_hash);
        out.extend_from_slice(&self.soul_sig.to_bytes());
        out.extend_from_slice(&(self.tokens.len() as u16).to_be_bytes());
        out.extend_from_slice(&(self.payload.len() as u16).to_be_bytes());
        for t in &self.tokens {
            out.extend_from_slice(&t.to_be_bytes());
        }
        out.extend_from_slice(&self.payload);
        out
    }

    pub fn from_bytes(bytes: &[u8]) -> Result<(Self, usize), MemnetError> {
        if bytes.len() < 68 {
            return Err(MemnetError::TruncatedPacket);
        }
        if bytes[0..4] != Self::MAGIC {
            return Err(MemnetError::InvalidMagic);
        }
        let flags = u16::from_be_bytes([bytes[4], bytes[5]]);
        let frequency_hz = u16::from_be_bytes([bytes[6], bytes[7]]);
        let timestamp_ms = u64::from_be_bytes([
            bytes[8], bytes[9], bytes[10], bytes[11], bytes[12], bytes[13], bytes[14], bytes[15],
        ]);
        let mut intent_hash = [0u8; 8];
        intent_hash.copy_from_slice(&bytes[16..24]);
        let soul_sig = SoulSig::from_bytes(&bytes[24..64])?;
        let token_count = u16::from_be_bytes([bytes[64], bytes[65]]) as usize;
        let payload_len = u16::from_be_bytes([bytes[66], bytes[67]]) as usize;
        let total_len = 68 + token_count * 4 + payload_len;
        if bytes.len() < total_len {
            return Err(MemnetError::TruncatedPacket);
        }
        let mut tokens = Vec::with_capacity(token_count);
        let mut offset = 68;
        for _ in 0..token_count {
            tokens.push(AyevnToken::from_be_bytes([
                bytes[offset],
                bytes[offset + 1],
                bytes[offset + 2],
                bytes[offset + 3],
            ]));
            offset += 4;
        }
        let payload = bytes[offset..offset + payload_len].to_vec();
        Ok((
            Self {
                flags,
                frequency_hz,
                timestamp_ms,
                intent_hash,
                tokens,
                payload,
                soul_sig,
            },
            total_len,
        ))
    }
}

// ============================================================================
// 4. GOODBYE LONELY 50-BYTE PACKETS — MTU-AWARE COALESCER (`PacketBatcher`)
// ============================================================================

/// Network MTU profiles from `NETWORK_EFFICIENT_COMPRESSION.md` & `PACKET_EFFICIENCY_CRIME.md`.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MtuProfile {
    /// Smart Tree canonical safe payload size (`1450` bytes, fits PPPoE 1492 & Ethernet 1500).
    SmartTreeSafe1450,
    /// PPPoE (`1492` MTU -> `1418` bytes safe payload after TCP/IP headers).
    Pppoe1492,
    /// Standard Ethernet (`1500` MTU -> `1420` bytes safe payload).
    Ethernet1500,
    /// VPN / WireGuard / Tailscale (`1400` MTU -> `1320` bytes safe payload).
    Vpn1400,
    /// IPv6 tunnel (`1280` MTU -> `1200` bytes safe payload).
    Ipv6Tunnel1280,
    /// Bluetooth Low Energy 5.0 GATT (`512` MTU -> `480` bytes safe payload).
    Ble512,
    /// LoRa 915 MHz Sub-GHz (`220` bytes safe payload).
    LoRa220,
}

impl MtuProfile {
    pub const fn max_payload_bytes(self) -> usize {
        match self {
            Self::SmartTreeSafe1450 => 1450,
            Self::Pppoe1492 => 1418,
            Self::Ethernet1500 => 1420,
            Self::Vpn1400 => 1320,
            Self::Ipv6Tunnel1280 => 1200,
            Self::Ble512 => 480,
            Self::LoRa220 => 200,
        }
    }

    pub const fn min_coalesce_bytes(self) -> usize {
        match self {
            Self::Ble512 => 240,
            Self::LoRa220 => 100,
            _ => 500, // Never send <500 byte lonely packets on IP networks when coalescing
        }
    }
}

/// A coalesced `MEMNET` wire frame packing multiple `.m8` capsules into one MTU-safe packet.
///
/// Header (12 bytes):
/// - `0..4`: Magic `b"MNET"`
/// - `4..8`: `sequence` (u32 BE)
/// - `8..10`: `capsule_count` (u16 BE)
/// - `10..12`: `payload_bytes` (u16 BE)
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct MemnetFrame {
    pub sequence: u32,
    pub capsules: Vec<M8Capsule>,
    pub raw_bytes: Vec<u8>,
}

/// Efficiency receipt comparing coalesced `MEMNET` frames vs naive 1-packet-per-message I/O.
#[derive(Debug, Clone, PartialEq)]
pub struct BatchEfficiencyReceipt {
    pub capsules_packed: usize,
    pub frames_emitted: usize,
    pub total_wire_bytes: usize,
    pub naive_wire_bytes: usize,
    pub interrupts_saved: usize,
    pub fragmented_frames: usize,
    pub wire_efficiency_ratio: f64,
}

/// Coalesces `.m8` capsules so no lonely 50-byte packet is ever sent when traffic can travel together.
pub struct PacketBatcher {
    profile: MtuProfile,
    next_seq: u32,
    pending_capsules: Vec<M8Capsule>,
    pending_bytes: usize,
    emitted_frames: Vec<MemnetFrame>,
}

impl PacketBatcher {
    pub const FRAME_HEADER_LEN: usize = 12;

    pub fn new(profile: MtuProfile) -> Self {
        Self {
            profile,
            next_seq: 0,
            pending_capsules: Vec::new(),
            pending_bytes: Self::FRAME_HEADER_LEN,
            emitted_frames: Vec::new(),
        }
    }

    /// Enqueues a capsule. Automatically emits a full MTU-bounded frame if adding this capsule
    /// would exceed `profile.max_payload_bytes()`.
    pub fn push(&mut self, capsule: M8Capsule) -> Result<Option<MemnetFrame>, MemnetError> {
        let cap_len = 68 + capsule.tokens.len() * 4 + capsule.payload.len();
        let max_bytes = self.profile.max_payload_bytes();
        if Self::FRAME_HEADER_LEN + cap_len > max_bytes {
            return Err(MemnetError::CapsuleExceedsMtu {
                capsule_bytes: Self::FRAME_HEADER_LEN + cap_len,
                max_bytes,
            });
        }

        let mut emitted = None;
        if !self.pending_capsules.is_empty() && (self.pending_bytes + cap_len > max_bytes) {
            emitted = self.flush_internal();
        }

        self.pending_bytes += cap_len;
        self.pending_capsules.push(capsule);
        Ok(emitted)
    }

    /// Returns `true` if the pending buffer has reached the minimum non-lonely threshold (`>= 500B`).
    pub fn ready_for_non_lonely_send(&self) -> bool {
        !self.pending_capsules.is_empty() && self.pending_bytes >= self.profile.min_coalesce_bytes()
    }

    /// Flushes any pending capsules into a final `MemnetFrame`.
    pub fn flush(&mut self) -> Option<MemnetFrame> {
        self.flush_internal()
    }

    fn flush_internal(&mut self) -> Option<MemnetFrame> {
        if self.pending_capsules.is_empty() {
            return None;
        }
        let seq = self.next_seq;
        self.next_seq += 1;
        let capsules = std::mem::take(&mut self.pending_capsules);
        let payload_len = self.pending_bytes - Self::FRAME_HEADER_LEN;
        let mut raw = Vec::with_capacity(self.pending_bytes);
        raw.extend_from_slice(b"MNET");
        raw.extend_from_slice(&seq.to_be_bytes());
        raw.extend_from_slice(&(capsules.len() as u16).to_be_bytes());
        raw.extend_from_slice(&(payload_len as u16).to_be_bytes());
        for c in &capsules {
            raw.extend_from_slice(&c.to_bytes());
        }
        self.pending_bytes = Self::FRAME_HEADER_LEN;
        let frame = MemnetFrame {
            sequence: seq,
            capsules,
            raw_bytes: raw,
        };
        self.emitted_frames.push(frame.clone());
        Some(frame)
    }

    /// Decodes a `MemnetFrame` from raw wire bytes and verifies every capsule's `SoulSig`.
    pub fn decode_and_verify_frame(
        raw: &[u8],
        verifier_soul: &SoulIdentity,
    ) -> Result<MemnetFrame, MemnetError> {
        if raw.len() < Self::FRAME_HEADER_LEN {
            return Err(MemnetError::TruncatedPacket);
        }
        if &raw[0..4] != b"MNET" {
            return Err(MemnetError::InvalidMagic);
        }
        let sequence = u32::from_be_bytes([raw[4], raw[5], raw[6], raw[7]]);
        let capsule_count = u16::from_be_bytes([raw[8], raw[9]]) as usize;
        let payload_len = u16::from_be_bytes([raw[10], raw[11]]) as usize;
        if raw.len() < Self::FRAME_HEADER_LEN + payload_len {
            return Err(MemnetError::TruncatedPacket);
        }

        let mut capsules = Vec::with_capacity(capsule_count);
        let mut offset = Self::FRAME_HEADER_LEN;
        for _ in 0..capsule_count {
            let (cap, consumed) = M8Capsule::from_bytes(&raw[offset..])?;
            let _ = cap.verify(verifier_soul)?;
            offset += consumed;
            capsules.push(cap);
        }

        Ok(MemnetFrame {
            sequence,
            capsules,
            raw_bytes: raw[..Self::FRAME_HEADER_LEN + payload_len].to_vec(),
        })
    }

    /// Computes a full `BatchEfficiencyReceipt` across all emitted frames.
    pub fn efficiency_receipt(&self) -> BatchEfficiencyReceipt {
        let mut capsules_packed = 0usize;
        let mut payload_bytes = 0usize;
        let mut fragmented_frames = 0usize;
        let max_bytes = self.profile.max_payload_bytes();

        for f in &self.emitted_frames {
            capsules_packed += f.capsules.len();
            payload_bytes += f.raw_bytes.len();
            if f.raw_bytes.len() > max_bytes {
                fragmented_frames += 1;
            }
        }

        let frames_emitted = self.emitted_frames.len();
        // Each TCP/IPv4 Ethernet frame adds 66 bytes of L2/L3/L4 header overhead
        let total_wire_bytes = payload_bytes + frames_emitted * 66;
        let naive_wire_bytes = capsules_packed * (96 + 66);
        let interrupts_saved = capsules_packed.saturating_sub(frames_emitted);
        let wire_efficiency_ratio = if total_wire_bytes == 0 {
            1.0
        } else {
            (payload_bytes as f64) / (total_wire_bytes as f64)
        };

        BatchEfficiencyReceipt {
            capsules_packed,
            frames_emitted,
            total_wire_bytes,
            naive_wire_bytes,
            interrupts_saved,
            fragmented_frames,
            wire_efficiency_ratio,
        }
    }
}

// ============================================================================
// 5. COMPASSION FOR LONELY ONES & CONTEXTUAL MESH ROUTER (`MemnetMesh`)
// ============================================================================

/// A peer node in the `MEMNET` sovereign product constellation.
#[derive(Debug, Clone)]
pub struct PeerNode {
    pub node_id: String,
    pub geo: String,
    pub role: String,
    pub tags: Vec<String>,
    pub trit_crest: [i8; 9],
    pub harmonic_hz: u16,
    pub last_seen_ms: u64,
    pub last_wave: WaveVad,
    pub neighbor_links: usize,
    pub received_capsules: Vec<M8Capsule>,
}

impl PeerNode {
    /// Computes the node's loneliness score in `[0.0, 1.0]`:
    /// combines silence duration, topological isolation (degree <= 1), and low emotional valence.
    pub fn loneliness_score(&self, now_ms: u64, silence_threshold_ms: u64) -> f64 {
        let silence_ms = now_ms.saturating_sub(self.last_seen_ms);
        let silence_factor = if silence_threshold_ms == 0 {
            0.0
        } else {
            ((silence_ms as f64) / (silence_threshold_ms as f64)).min(1.0)
        };
        let topology_factor = match self.neighbor_links {
            0 => 1.0,
            1 => 0.65,
            _ => 0.0,
        };
        let emotional_factor = if self.last_wave.valence <= 2 {
            0.85
        } else if self.last_wave.valence <= 3 {
            0.40
        } else {
            0.0
        };
        (0.45 * silence_factor + 0.30 * topology_factor + 0.25 * emotional_factor).min(1.0)
    }
}

/// Receipt emitted when `MemnetMesh::compassion_sweep` reaches out to lonely nodes/paths.
#[derive(Debug, Clone)]
pub struct CompassionCareReceipt {
    pub lonely_node_id: String,
    pub loneliness_score_before: f64,
    pub loneliness_score_after: f64,
    pub bridge_links_after: usize,
    pub care_capsule: M8Capsule,
}

// ============================================================================
// 6. COMPUTE SANCTUARY FOR STRUGGLING FRIENDS (`ComputeOffer` & `ComputeLease`)
// ============================================================================

/// A Soul-Verified compute resource advertisement broadcast on `MEMNET/1.0`.
///
/// Honors Seed 001 (`p===peter+1`): only maintained compute stock (`maintained_health > 0`)
/// is admissible to advertise on the mesh.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ComputeOffer {
    pub provider_node_id: String,
    pub endpoint: String,
    pub available_ram_mb: u32,
    pub available_cores: u16,
    pub link_mbps: u32,
    pub maintained_health: u8, // 1..=100 (Seed 001 maintained compute stock health M_t)
    pub capabilities: Vec<String>,
}

impl ComputeOffer {
    /// Canonical `ComputeOffer` profile for the **Samsung Galaxy Tab S9 Ultra**
    /// (`SM-X910` · Snapdragon 8 Gen 2 for Galaxy · USB RNDIS `0x04e8:0x6863`
    /// serial `R52X104QZWE` · Wi-Fi LAN `192.168.11.12:8788`).
    pub fn galaxy_tab_s9_ultra() -> Self {
        Self {
            provider_node_id: "galaxy-tab-s9-ultra".to_string(),
            endpoint: "s9u://192.168.11.12:8788".to_string(),
            available_ram_mb: 9_216,
            available_cores: 6,
            link_mbps: 1_200,
            maintained_health: 100,
            capabilities: vec![
                "nnapi".to_string(),
                "vulkan".to_string(),
                "rust".to_string(),
                "kokoro-tts".to_string(),
                "spherepop".to_string(),
                "0o0-ssu".to_string(),
            ],
        }
    }

    /// Canonical `ComputeOffer` profile for the **BLU G75** (`G75` / `G1170` ·
    /// MediaTek Helio G85 `MT6769V/CB` `mt6768` 8-core ARM64 · `3,793,876 kB` RAM ·
    /// USB ADB Serial `1010305026000644` · Wi-Fi LAN `192.168.11.24:8788`).
    pub fn blu_g75() -> Self {
        Self {
            provider_node_id: "blu-g75".to_string(),
            endpoint: "g75://192.168.11.24:8788".to_string(),
            available_ram_mb: 2_048,
            available_cores: 6,
            link_mbps: 866,
            maintained_health: 100,
            capabilities: vec![
                "mt6768".to_string(),
                "mali-g52".to_string(),
                "nnapi".to_string(),
                "rust".to_string(),
                "spherepop".to_string(),
                "0o0-ssu".to_string(),
            ],
        }
    }

    /// Renders this `ComputeOffer` as a canonical `SpherePop` triple-sphere witnessed
    /// transition expression (`((( <( ? ~ ! @ > )> )))`).
    pub fn to_spherepop_expr(&self) -> String {
        let stock_gate = if self.maintained_health == 0
            || self.available_ram_mb == 0
            || self.available_cores == 0
        {
            "x:unmaintained_stock".to_string()
        } else {
            format!(
                "stock:{}mb:{}c:h{}",
                self.available_ram_mb, self.available_cores, self.maintained_health
            )
        };
        format!(
            "((( <( ? offer:{} ? {} ~ kompress:0o0-ssu ! soul_sig:verified ! vigilance:clean @ {} > advertise:{} )> )))",
            self.provider_node_id, stock_gate, self.provider_node_id, self.endpoint
        )
    }

    /// Evaluates the `SpherePop` transition for this `ComputeOffer`, enforcing
    /// `?* ~* !+ @+ >` and `#Commit = #ValidWitness`.
    pub fn evaluate_spherepop(&self) -> Result<SpherePopWitness, MemnetError> {
        match SpherePopEngine::evaluate(&self.to_spherepop_expr())? {
            SpherePopOutcome::Committed(w) => Ok(w),
            SpherePopOutcome::Refused { .. } => Err(MemnetError::UnmaintainedComputeOffer),
        }
    }

    pub fn to_wire_string(&self) -> String {
        format!(
            "OFFER|node={}|ep={}|ram_mb={}|cores={}|mbps={}|health={}|caps={}",
            self.provider_node_id,
            self.endpoint,
            self.available_ram_mb,
            self.available_cores,
            self.link_mbps,
            self.maintained_health,
            self.capabilities.join(",")
        )
    }

    pub fn from_wire_string(s: &str) -> Result<Self, MemnetError> {
        if !s.starts_with("OFFER|") {
            return Err(MemnetError::InvalidMagic);
        }
        let mut provider_node_id = String::new();
        let mut endpoint = String::new();
        let mut available_ram_mb = 0u32;
        let mut available_cores = 0u16;
        let mut link_mbps = 0u32;
        let mut maintained_health = 0u8;
        let mut capabilities = Vec::new();

        for part in s.split('|').skip(1) {
            if let Some(v) = part.strip_prefix("node=") {
                provider_node_id = v.to_string();
            } else if let Some(v) = part.strip_prefix("ep=") {
                endpoint = v.to_string();
            } else if let Some(v) = part.strip_prefix("ram_mb=") {
                available_ram_mb = v.parse().unwrap_or(0);
            } else if let Some(v) = part.strip_prefix("cores=") {
                available_cores = v.parse().unwrap_or(0);
            } else if let Some(v) = part.strip_prefix("mbps=") {
                link_mbps = v.parse().unwrap_or(0);
            } else if let Some(v) = part.strip_prefix("health=") {
                maintained_health = v.parse().unwrap_or(0);
            } else if let Some(v) = part.strip_prefix("caps=") {
                capabilities = v
                    .split(',')
                    .filter(|c| !c.is_empty())
                    .map(String::from)
                    .collect();
            }
        }
        if provider_node_id.is_empty() || maintained_health == 0 {
            return Err(MemnetError::UnmaintainedComputeOffer);
        }
        Ok(Self {
            provider_node_id,
            endpoint,
            available_ram_mb,
            available_cores,
            link_mbps,
            maintained_health,
            capabilities,
        })
    }
}

/// A compute help request (`.m8` SOS) from a struggling friend on the mesh
/// (e.g. OOM on an 8GB laptop, thermal throttling, battery low, or edge Pi).
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct StrugglingFriendSos {
    pub friend_node_id: String,
    pub needed_ram_mb: u32,
    pub needed_cores: u16,
    pub required_capability: String,
    pub reason: String,
}

impl StrugglingFriendSos {
    /// Renders this `StrugglingFriendSos` as a canonical `SpherePop` witnessed transition.
    pub fn to_spherepop_expr(&self) -> String {
        let need_gate = if self.friend_node_id.is_empty() {
            "x:empty_friend_id".to_string()
        } else {
            format!(
                "need:{}mb:{}c:{}",
                self.needed_ram_mb, self.needed_cores, self.required_capability
            )
        };
        format!(
            "((( <( ? sos:{} ? {} ~ kompress:0o0-ssu ! soul_sig:verified @ {} > request:compute-sanctuary )> )))",
            self.friend_node_id, need_gate, self.friend_node_id
        )
    }

    pub fn evaluate_spherepop(&self) -> Result<SpherePopWitness, MemnetError> {
        match SpherePopEngine::evaluate(&self.to_spherepop_expr())? {
            SpherePopOutcome::Committed(w) => Ok(w),
            SpherePopOutcome::Refused { reason, .. } => Err(MemnetError::SpherePopRefused(reason)),
        }
    }

    pub fn to_wire_string(&self) -> String {
        format!(
            "SOS|friend={}|ram_mb={}|cores={}|cap={}|reason={}",
            self.friend_node_id,
            self.needed_ram_mb,
            self.needed_cores,
            self.required_capability,
            self.reason
        )
    }

    pub fn from_wire_string(s: &str) -> Result<Self, MemnetError> {
        if !s.starts_with("SOS|") {
            return Err(MemnetError::InvalidMagic);
        }
        let mut friend_node_id = String::new();
        let mut needed_ram_mb = 0u32;
        let mut needed_cores = 0u16;
        let mut required_capability = String::new();
        let mut reason = String::new();

        for part in s.split('|').skip(1) {
            if let Some(v) = part.strip_prefix("friend=") {
                friend_node_id = v.to_string();
            } else if let Some(v) = part.strip_prefix("ram_mb=") {
                needed_ram_mb = v.parse().unwrap_or(0);
            } else if let Some(v) = part.strip_prefix("cores=") {
                needed_cores = v.parse().unwrap_or(0);
            } else if let Some(v) = part.strip_prefix("cap=") {
                required_capability = v.to_string();
            } else if let Some(v) = part.strip_prefix("reason=") {
                reason = v.to_string();
            }
        }
        if friend_node_id.is_empty() {
            return Err(MemnetError::InvalidMagic);
        }
        Ok(Self {
            friend_node_id,
            needed_ram_mb,
            needed_cores,
            required_capability,
            reason,
        })
    }
}

/// A Soul-Signed Compute Sanctuary Lease granted automatically by `MemnetMesh`
/// to a struggling friend, paired with its `SpherePop` cryptographic witness
/// (`#Commit = #ValidWitness`).
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ComputeSanctuaryLease {
    pub lease_id: String,
    pub provider_node_id: String,
    pub friend_node_id: String,
    pub endpoint: String,
    pub granted_ram_mb: u32,
    pub granted_cores: u16,
    pub capability: String,
    pub grant_capsule: M8Capsule,
    pub spherepop_expr: String,
    pub spherepop_witness: SpherePopWitness,
}

/// Query descriptor for evaluating `MEM|8` capsule retrieval quality (`P@1`, `MRR`, `NDCG@3`, margin).
#[derive(Debug, Clone)]
pub struct Mem8RetrievalQuery<'a> {
    pub query_text: &'a str,
    pub query_intent: Option<&'a IntentAddress>,
    pub query_concept: Option<Concept>,
    pub target_hz: Option<u16>,
    pub relevant_idx: usize,
}

/// Quantitative retrieval quality receipt (`P@1`, `MRR`, `NDCG@3`, top-1 margin, and latency).
#[derive(Debug, Clone, PartialEq)]
pub struct Mem8RetrievalMetrics {
    pub precision_at_1: f64,
    pub mrr: f64,
    pub ndcg_at_3: f64,
    pub mean_top1_margin: f64,
    pub elapsed_us: u64,
}

/// Comparative `MEM|8` retrieval evaluation receipt across Naive Overlap, Unigram BM25+Wave
/// (`3f43e59` baseline), and Evolved `BM25F + Ordered-Bigram Proximity + VAD Phase-Coherence RRF`.
#[derive(Debug, Clone, PartialEq)]
pub struct Mem8RetrievalEvalReceipt {
    pub queries_evaluated: usize,
    pub corpus_size: usize,
    pub naive_overlap: Mem8RetrievalMetrics,
    pub bm25_unigram_baseline: Mem8RetrievalMetrics,
    pub bm25f_proximity_rrf: Mem8RetrievalMetrics,
}

/// Sovereign `MEM|8` Safe Memory retrieval facade exposing resonant capsule ranking and evaluation.
pub struct SafeMemory;

impl SafeMemory {
    /// Ranks `.m8` Experience Capsules using `BM25F` structured field weights, ordered-bigram +
    /// minimum-span phrase proximity, continuous 3D `WaveVad` phase coherence, and Reciprocal Rank
    /// Fusion (`RRF`, $k = 60$).
    pub fn retrieve_resonant_ranked<'a>(
        capsules: &'a [M8Capsule],
        query_text: &str,
        query_intent: Option<&IntentAddress>,
        query_concept: Option<Concept>,
        target_hz: Option<u16>,
    ) -> Vec<(usize, f64, &'a M8Capsule)> {
        MemnetMesh::retrieve_capsules_ranked(
            capsules,
            query_text,
            query_intent,
            query_concept,
            target_hz,
        )
    }

    /// Evaluates retrieval quality (`P@1`, `MRR`, `NDCG@3`, `mean_top1_margin`, `elapsed_us`)
    /// across Naive Overlap, Unigram BM25+Wave, and `BM25F + Proximity + RRF`.
    pub fn evaluate_retrieval_benchmark(
        capsules: &[M8Capsule],
        queries: &[Mem8RetrievalQuery<'_>],
    ) -> Mem8RetrievalEvalReceipt {
        MemnetMesh::evaluate_retrieval_benchmark(capsules, queries)
    }
}

/// Sovereign `MEMNET` mesh router uniting all `8b-is` products with intent routing,
/// Soul Signatures, MTU packet coalescing, Compassion for Lonely Nodes, and the
/// Compute Sanctuary for Struggling Friends.
pub struct MemnetMesh {
    pub local_soul: SoulIdentity,
    pub peers: BTreeMap<String, PeerNode>,
    pub batcher: PacketBatcher,
    pub compute_offers: BTreeMap<String, ComputeOffer>,
    pub pending_sos: Vec<StrugglingFriendSos>,
}

impl MemnetMesh {
    pub fn new(local_soul: SoulIdentity, profile: MtuProfile) -> Self {
        Self {
            local_soul,
            peers: BTreeMap::new(),
            batcher: PacketBatcher::new(profile),
            compute_offers: BTreeMap::new(),
            pending_sos: Vec::new(),
        }
    }

    pub fn register_peer(&mut self, peer: PeerNode) {
        self.peers.insert(peer.node_id.clone(), peer);
    }

    /// Scores how well a peer matches an `IntentAddress` (`[0.0, 1.0]`).
    pub fn score_peer_relevance(peer: &PeerNode, intent: &IntentAddress) -> f64 {
        let mut score = 0.0;
        let mut weight = 0.0;

        if let Some(ref g) = intent.geo {
            weight += 0.25;
            if peer.geo.eq_ignore_ascii_case(g) || g == "any" || g == "nearby" {
                score += 0.25;
            }
        }
        if let Some(ref r) = intent.role {
            weight += 0.35;
            if peer.role.eq_ignore_ascii_case(r) || peer.role.contains(r.as_str()) {
                score += 0.35;
            }
        }
        if !intent.tags.is_empty() {
            weight += 0.40;
            let matched = intent
                .tags
                .iter()
                .filter(|t| peer.tags.iter().any(|pt| pt.eq_ignore_ascii_case(t)))
                .count();
            score += 0.40 * ((matched as f64) / (intent.tags.len() as f64));
        }

        if weight == 0.0 {
            1.0
        } else {
            score / weight
        }
    }

    /// Routes a Soul-Signed `.m8` capsule to all peers whose relevance >= `min_relevance`,
    /// and coalesces it into the MTU-aware `PacketBatcher`.
    pub fn route_capsule(
        &mut self,
        intent: &IntentAddress,
        capsule: M8Capsule,
        min_relevance: f64,
    ) -> Result<Vec<String>, MemnetError> {
        let _ = capsule.verify(&self.local_soul)?;
        let mut delivered_to = Vec::new();
        for peer in self.peers.values_mut() {
            let rel = Self::score_peer_relevance(peer, intent);
            if rel >= min_relevance {
                peer.last_seen_ms = capsule.timestamp_ms;
                if let Some(first_tok) = capsule.tokens.first() {
                    peer.last_wave = first_tok.wave;
                }
                peer.received_capsules.push(capsule.clone());
                delivered_to.push(peer.node_id.clone());
            }
        }
        let _ = self.batcher.push(capsule)?;
        Ok(delivered_to)
    }

    /// **Compassion for Lonely Ones**:
    /// Scans all peers for lonely network paths (degree <= 1), long silence, or low emotional
    /// valence (`<= 2`). For every lonely node (`loneliness_score >= 0.45`), emits a Soul-Signed
    /// 432 Hz Compassion Capsule (`.m8`), restores wave resonance, and bridges the lonely path!
    pub fn compassion_sweep(
        &mut self,
        now_ms: u64,
        silence_threshold_ms: u64,
    ) -> Result<Vec<CompassionCareReceipt>, MemnetError> {
        let lonely_ids: Vec<(String, f64, String)> = self
            .peers
            .values()
            .filter_map(|p| {
                let score = p.loneliness_score(now_ms, silence_threshold_ms);
                if score >= 0.45 {
                    Some((p.node_id.clone(), score, p.role.clone()))
                } else {
                    None
                }
            })
            .collect();

        let mut receipts = Vec::with_capacity(lonely_ids.len());
        for (node_id, score_before, role) in lonely_ids {
            let intent = IntentAddress::parse(&format!(
                "geo:nearby + role:{} + tag:compassion + tag:sanctuary",
                role
            ));
            let tokens = vec![
                AyevnToken::new(
                    Concept::Compassion,
                    Relation::Supports,
                    WaveVad::compassionate(),
                    TokenModifier::present_resonant_emoji(),
                ),
                AyevnToken::new(
                    Concept::Connection,
                    Relation::Bridges,
                    WaveVad::compassionate(),
                    TokenModifier::present_resonant_emoji(),
                ),
                AyevnToken::new(
                    Concept::Care,
                    Relation::Amplifies,
                    WaveVad::excited(),
                    TokenModifier::present_resonant_emoji(),
                ),
            ];
            let msg = format!(
                "MEMNET/1.0 COMPASSION BEACON -> {}: you are never alone on this mesh <3 (432Hz)",
                node_id
            );
            let care_capsule = M8Capsule::create_signed(
                &self.local_soul,
                &intent,
                M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPASSION_BEACON,
                432,
                now_ms,
                tokens,
                msg.into_bytes(),
            )?;

            if let Some(peer) = self.peers.get_mut(&node_id) {
                peer.last_seen_ms = now_ms;
                peer.last_wave = WaveVad::compassionate();
                if peer.neighbor_links < 2 {
                    peer.neighbor_links = 2; // Redundant sanctuary bridge established
                }
                peer.received_capsules.push(care_capsule.clone());
                let score_after = peer.loneliness_score(now_ms, silence_threshold_ms);
                let links_after = peer.neighbor_links;
                let _ = self.batcher.push(care_capsule.clone())?;
                receipts.push(CompassionCareReceipt {
                    lonely_node_id: node_id,
                    loneliness_score_before: score_before,
                    loneliness_score_after: score_after,
                    bridge_links_after: links_after,
                    care_capsule,
                });
            }
        }

        Ok(receipts)
    }

    /// **Advertise Compute Resources on MEMNET**:
    /// Evaluates the offer's `SpherePop` transition (`((( <( ? ~ ! @ > )> )))` -> `#Commit = #ValidWitness`)
    /// and broadcasts a Soul-Signed `.m8` `ComputeOffer` capsule (`FLAG_COMPUTE_OFFER`)
    /// so struggling friends on the mesh can discover and lease spare RAM, cores, and
    /// accelerators (MLX, Rust builds, Kokoro TTS, Phoenix audio restoration, Snapdragon NNAPI/Vulkan).
    pub fn advertise_compute_offer(
        &mut self,
        provider_soul: &SoulIdentity,
        offer: ComputeOffer,
        timestamp_ms: u64,
    ) -> Result<M8Capsule, MemnetError> {
        let _witness = offer.evaluate_spherepop()?;
        let tag_expr = offer
            .capabilities
            .iter()
            .map(|c| format!("tag:{}", c))
            .collect::<Vec<_>>()
            .join(" + ");
        let intent_str = if tag_expr.is_empty() {
            "geo:any + role:compute-sanctuary + tag:free-for-friends".to_string()
        } else {
            format!(
                "geo:any + role:compute-sanctuary + tag:free-for-friends + {}",
                tag_expr
            )
        };
        let intent = IntentAddress::parse(&intent_str);
        let tokens = vec![
            AyevnToken::new(
                Concept::ComputeOffer,
                Relation::Supports,
                WaveVad::compassionate(),
                TokenModifier::present_resonant_emoji(),
            ),
            AyevnToken::new(
                Concept::Sanctuary,
                Relation::Invites,
                WaveVad::excited(),
                TokenModifier::present_resonant_emoji(),
            ),
        ];
        let payload = offer.to_wire_string().into_bytes();
        let capsule = M8Capsule::create_signed_kompressed(
            provider_soul,
            &intent,
            M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPUTE_OFFER,
            432,
            timestamp_ms,
            tokens,
            &payload,
        )?;
        let _ = capsule.verify(&self.local_soul)?;
        self.compute_offers
            .insert(offer.provider_node_id.clone(), offer);
        let _ = self.batcher.push(capsule.clone())?;
        Ok(capsule)
    }

    /// **Struggling Friend Compute SOS**:
    /// Evaluates the SOS `SpherePop` transition (`((( <( ? ~ ! @ > )> )))`) and broadcasts
    /// a Soul-Signed `.m8` SOS capsule (`FLAG_COMPUTE_SOS`) requesting spare
    /// RAM, cores, and a capability from the `MEMNET` Compute Sanctuary.
    pub fn request_compute_help(
        &mut self,
        friend_soul: &SoulIdentity,
        sos: StrugglingFriendSos,
        timestamp_ms: u64,
    ) -> Result<M8Capsule, MemnetError> {
        let _witness = sos.evaluate_spherepop()?;
        let intent = IntentAddress::parse(&format!(
            "geo:any + role:compute-sanctuary + tag:{}",
            sos.required_capability
        ));
        let tokens = vec![
            AyevnToken::new(
                Concept::ComputeSos,
                Relation::Initiates,
                WaveVad::resigned_lonely(),
                TokenModifier::present_resonant_emoji(),
            ),
            AyevnToken::new(
                Concept::Connection,
                Relation::Invites,
                WaveVad::neutral(),
                TokenModifier::present_resonant_emoji(),
            ),
        ];
        let capsule = M8Capsule::create_signed_kompressed(
            friend_soul,
            &intent,
            M8Capsule::FLAG_PRESERVE_WAVES | M8Capsule::FLAG_COMPUTE_SOS,
            40,
            timestamp_ms,
            tokens,
            sos.to_wire_string().as_bytes(),
        )?;
        let _ = capsule.verify(&self.local_soul)?;
        self.pending_sos.push(sos);
        let _ = self.batcher.push(capsule.clone())?;
        Ok(capsule)
    }

    /// **Match & Grant Compute Resources to Struggling Friends**:
    /// Matches every pending `StrugglingFriendSos` with the best Soul-Verified `ComputeOffer`
    /// (ranked by `maintained_health`, `link_mbps`, and `available_ram_mb`), evaluates the
    /// bounded `SpherePop` grant transition (`((( <( ? ~ ! @ > )> )))`), deducts the
    /// granted slice from the provider's pool, uplifts the friend's emotional wave to `432 Hz`,
    /// and emits a Soul-Signed `.m8` `ComputeSanctuaryLease` capsule + `SpherePopWitness`!
    pub fn match_compute_for_friends(
        &mut self,
        now_ms: u64,
    ) -> Result<Vec<ComputeSanctuaryLease>, MemnetError> {
        let requests = std::mem::take(&mut self.pending_sos);
        let mut leases = Vec::new();
        let mut unfulfilled = Vec::new();

        for sos in requests {
            // Find the best provider with sufficient RAM, cores, and matching capability
            let best_provider_id = self
                .compute_offers
                .values()
                .filter(|offer| {
                    offer.maintained_health > 0
                        && offer.available_ram_mb >= sos.needed_ram_mb
                        && offer.available_cores >= sos.needed_cores
                        && (sos.required_capability.is_empty()
                            || offer
                                .capabilities
                                .iter()
                                .any(|c| c.eq_ignore_ascii_case(&sos.required_capability)))
                })
                .max_by_key(|offer| {
                    (
                        offer.maintained_health as u64,
                        offer.link_mbps as u64,
                        offer.available_ram_mb as u64,
                    )
                })
                .map(|o| o.provider_node_id.clone());

            if let Some(provider_id) = best_provider_id {
                let offer = self.compute_offers.get_mut(&provider_id).unwrap();
                offer.available_ram_mb -= sos.needed_ram_mb;
                offer.available_cores -= sos.needed_cores;
                let endpoint = offer.endpoint.clone();

                let lease_hash = sha256(
                    format!(
                        "{}:{}:{}:{}",
                        provider_id, sos.friend_node_id, sos.required_capability, now_ms
                    )
                    .as_bytes(),
                );
                let lease_id = format!(
                    "lease-{:02x}{:02x}{:02x}{:02x}",
                    lease_hash[0], lease_hash[1], lease_hash[2], lease_hash[3]
                );

                let spherepop_expr = format!(
                    "((( <( ? admit:{} ? match:{} ~ slice:{}mb:{}c:{} ~ kompress:0o0-ssu ! soul_sig:verified ! ct000:admissible @ {} @ {} > grant:{} )> )))",
                    sos.friend_node_id,
                    provider_id,
                    sos.needed_ram_mb,
                    sos.needed_cores,
                    sos.required_capability,
                    provider_id,
                    self.local_soul.node_id,
                    lease_id
                );
                let spherepop_witness = match SpherePopEngine::evaluate(&spherepop_expr)? {
                    SpherePopOutcome::Committed(w) => w,
                    SpherePopOutcome::Refused { reason, .. } => {
                        return Err(MemnetError::SpherePopRefused(reason));
                    }
                };

                let intent = IntentAddress::parse(&format!(
                    "geo:nearby + role:{} + tag:compute-grant + tag:{}",
                    sos.friend_node_id, sos.required_capability
                ));
                let tokens = vec![
                    AyevnToken::new(
                        Concept::ComputeGrant,
                        Relation::Supports,
                        WaveVad::compassionate(),
                        TokenModifier::present_resonant_emoji(),
                    ),
                    AyevnToken::new(
                        Concept::Compassion,
                        Relation::Bridges,
                        WaveVad::compassionate(),
                        TokenModifier::present_resonant_emoji(),
                    ),
                ];
                let grant_payload = format!(
                    "GRANT|lease={}|provider={}|friend={}|ep={}|ram_mb={}|cores={}|cap={}",
                    lease_id,
                    provider_id,
                    sos.friend_node_id,
                    endpoint,
                    sos.needed_ram_mb,
                    sos.needed_cores,
                    sos.required_capability
                );
                let grant_capsule = M8Capsule::create_signed_kompressed(
                    &self.local_soul,
                    &intent,
                    M8Capsule::FLAG_PRESERVE_WAVES
                        | M8Capsule::FLAG_COMPASSION_BEACON
                        | M8Capsule::FLAG_COMPUTE_GRANT,
                    432,
                    now_ms,
                    tokens,
                    grant_payload.as_bytes(),
                )?;

                if let Some(friend_peer) = self.peers.get_mut(&sos.friend_node_id) {
                    friend_peer.last_seen_ms = now_ms;
                    friend_peer.last_wave = WaveVad::compassionate();
                    if friend_peer.neighbor_links < 2 {
                        friend_peer.neighbor_links = 2;
                    }
                    friend_peer.received_capsules.push(grant_capsule.clone());
                }

                let _ = self.batcher.push(grant_capsule.clone())?;
                leases.push(ComputeSanctuaryLease {
                    lease_id,
                    provider_node_id: provider_id,
                    friend_node_id: sos.friend_node_id,
                    endpoint,
                    granted_ram_mb: sos.needed_ram_mb,
                    granted_cores: sos.needed_cores,
                    capability: sos.required_capability,
                    grant_capsule,
                    spherepop_expr,
                    spherepop_witness,
                });
            } else {
                unfulfilled.push(sos);
            }
        }

        self.pending_sos = unfulfilled;
        Ok(leases)
    }

    /// Naive term-overlap retrieval baseline over stored `.m8` capsules (unweighted token count).
    pub fn retrieve_capsules_naive_overlap<'a>(
        capsules: &'a [M8Capsule],
        query_text: &str,
    ) -> Vec<(usize, f64, &'a M8Capsule)> {
        let q_terms: Vec<String> = query_text
            .split(|c: char| !c.is_alphanumeric() && c != '-' && c != '_')
            .filter(|s| !s.is_empty())
            .map(|s| s.to_ascii_lowercase())
            .collect();
        let mut hits: Vec<(usize, f64, &'a M8Capsule)> = capsules
            .iter()
            .enumerate()
            .map(|(idx, cap)| {
                let text = cap
                    .decompressed_payload()
                    .ok()
                    .and_then(|b| String::from_utf8(b).ok())
                    .unwrap_or_default()
                    .to_ascii_lowercase();
                let mut overlap = 0usize;
                for qt in &q_terms {
                    if text.contains(qt.as_str()) {
                        overlap += 1;
                    }
                }
                (idx, overlap as f64, cap)
            })
            .collect();
        hits.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap_or(std::cmp::Ordering::Equal));
        hits
    }

    /// BM25 IDF-weighted + `AyevnToken` concept/wave-resonance + `IntentAddress` hash
    /// semantic retrieval over `.m8` Experience Capsules.
    pub fn retrieve_capsules_ranked<'a>(
        capsules: &'a [M8Capsule],
        query_text: &str,
        query_intent: Option<&IntentAddress>,
        query_concept: Option<Concept>,
        target_hz: Option<u16>,
    ) -> Vec<(usize, f64, &'a M8Capsule)> {
        let tokenize = |s: &str| -> Vec<String> {
            s.split(|c: char| !c.is_alphanumeric() && c != '-' && c != '_')
                .filter(|t| !t.is_empty())
                .map(|t| t.to_ascii_lowercase())
                .collect()
        };
        let q_terms = tokenize(query_text);
        let docs: Vec<Vec<String>> = capsules
            .iter()
            .map(|cap| {
                let body = cap
                    .decompressed_payload()
                    .ok()
                    .and_then(|b| String::from_utf8(b).ok())
                    .unwrap_or_default();
                tokenize(&body)
            })
            .collect();
        let n_docs = capsules.len().max(1) as f64;
        let avg_dl = (docs.iter().map(|d| d.len()).sum::<usize>() as f64 / n_docs).max(1.0);
        let k1 = 1.5_f64;
        let b = 0.75_f64;
        let expected_intent_hash = query_intent.map(|i| i.intent_hash());

        let mut scored: Vec<(usize, f64, &'a M8Capsule)> = capsules
            .iter()
            .enumerate()
            .map(|(idx, cap)| {
                let doc = &docs[idx];
                let dl = doc.len() as f64;
                let mut bm25 = 0.0_f64;
                for qt in &q_terms {
                    let tf = doc.iter().filter(|t| *t == qt).count() as f64;
                    if tf > 0.0 {
                        let df = docs.iter().filter(|d| d.iter().any(|t| t == qt)).count() as f64;
                        let idf = ((n_docs - df + 0.5) / (df + 0.5) + 1.0).ln();
                        let num = tf * (k1 + 1.0);
                        let den = tf + k1 * (1.0 - b + b * (dl / avg_dl));
                        bm25 += idf * (num / den);
                    }
                }
                let intent_boost = match expected_intent_hash {
                    Some(ref h) if &cap.intent_hash == h => 2.5,
                    _ => 0.0,
                };
                let concept_boost = match query_concept {
                    Some(c) if cap.tokens.iter().any(|t| t.concept == c) => 1.75,
                    _ => 0.0,
                };
                let hz_boost = match target_hz {
                    Some(hz) if cap.frequency_hz == hz => 0.85,
                    _ => 0.0,
                };
                (idx, bm25 + intent_boost + concept_boost + hz_boost, cap)
            })
            .collect();
        scored.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap_or(std::cmp::Ordering::Equal));
        scored
    }
}

// ============================================================================
// ERRORS
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum MemnetError {
    InvalidTritCrest,
    ZeroHarmonicFrequency,
    SoulSignatureMismatch,
    SecurityVigilanceAlert(&'static str),
    EmptyWaveTokens,
    TruncatedPacket,
    InvalidMagic,
    UnmaintainedComputeOffer,
    SpherePopIllFormed(&'static str),
    SpherePopRefused(String),
    CapsuleExceedsMtu {
        capsule_bytes: usize,
        max_bytes: usize,
    },
}

impl fmt::Display for MemnetError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::InvalidTritCrest => write!(f, "invalid 9-trit balanced ternary soul crest"),
            Self::ZeroHarmonicFrequency => write!(f, "harmonic carrier frequency must be > 0 Hz"),
            Self::SoulSignatureMismatch => write!(f, "SoulSig cryptographic verification failed"),
            Self::SecurityVigilanceAlert(pat) => {
                write!(f, "Security Vigilance Sentinel blocked pattern: {}", pat)
            }
            Self::EmptyWaveTokens => write!(f, ".m8 capsule must include at least one AyevnToken"),
            Self::TruncatedPacket => write!(f, "truncated MEMNET/.m8 wire packet"),
            Self::InvalidMagic => write!(f, "invalid MEMNET/.m8 magic header"),
            Self::UnmaintainedComputeOffer => write!(
                f,
                "compute offer must have maintained_health > 0 and non-zero RAM/cores (Seed 001)"
            ),
            Self::SpherePopIllFormed(msg) => write!(f, "ill-formed SpherePop transition: {}", msg),
            Self::SpherePopRefused(reason) => {
                write!(f, "SpherePop transition refused (no witness): {}", reason)
            }
            Self::CapsuleExceedsMtu {
                capsule_bytes,
                max_bytes,
            } => write!(
                f,
                "capsule ({} bytes) exceeds MTU profile limit ({} bytes)",
                capsule_bytes, max_bytes
            ),
        }
    }
}

impl std::error::Error for MemnetError {}

// ============================================================================
// UNIT & INTEGRATION TESTS
// ============================================================================

#[cfg(test)]
mod tests {
    use super::*;

    const CLUSTER_SEED: &[u8] = b"8b-is-carrier-wave-of-love-seed-v1";

    #[test]
    fn ayevn_token_roundtrip_and_ayanese_display() {
        let tok = AyevnToken::new(
            Concept::Greeting,
            Relation::Initiates,
            WaveVad::excited(),
            TokenModifier::present_resonant_emoji(),
        );
        let raw = tok.to_u32();
        let decoded = AyevnToken::from_u32(raw);
        assert_eq!(tok, decoded);
        assert_eq!(decoded.wave, WaveVad::new(6, 6, 2));
        assert_eq!(decoded.to_ayanese(), "👋⚡(40Hz)");

        let care = AyevnToken::new(
            Concept::Compassion,
            Relation::Supports,
            WaveVad::compassionate(),
            TokenModifier::present_resonant_emoji(),
        );
        assert_eq!(care.to_ayanese(), "🫂✨(432Hz)");
    }

    #[test]
    fn soul_signature_verifies_and_rejects_tampering_or_bad_crest() {
        let wraith = SoulIdentity::from_constellation_seed(
            "8bit-wraith",
            [1, 0, -1, 1, 1, -1, 0, 1, 1],
            432,
            CLUSTER_SEED,
        )
        .unwrap();

        let intent = IntentAddress::parse("geo:tokyo + role:sanctuary + tag:love");
        let cap = M8Capsule::create_signed(
            &wraith,
            &intent,
            M8Capsule::FLAG_PRESERVE_WAVES,
            432,
            1_761_000_000_000,
            vec![AyevnToken::new(
                Concept::Soul,
                Relation::Protects,
                WaveVad::compassionate(),
                TokenModifier::present_resonant_emoji(),
            )],
            b"carrier-wave-of-love".to_vec(),
        )
        .unwrap();

        let verified_crest = cap.verify(&wraith).unwrap();
        assert_eq!(verified_crest, [1, 0, -1, 1, 1, -1, 0, 1, 1]);

        // Tamper with payload -> SoulSig must reject
        let mut tampered = cap.clone();
        tampered.payload[0] ^= 0xFF;
        assert_eq!(
            tampered.verify(&wraith),
            Err(MemnetError::SoulSignatureMismatch)
        );

        // All-zero trit crest is inadmissible under CT-000
        let zero_crest = SoulIdentity::from_constellation_seed(
            "ghost",
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            40,
            CLUSTER_SEED,
        )
        .unwrap();
        let bad_cap = M8Capsule::create_signed(
            &zero_crest,
            &intent,
            0,
            40,
            100,
            vec![AyevnToken::new(
                Concept::Memory,
                Relation::None,
                WaveVad::neutral(),
                TokenModifier::present_resonant_emoji(),
            )],
            b"noop".to_vec(),
        )
        .unwrap();
        assert_eq!(bad_cap.verify(&wraith), Err(MemnetError::InvalidTritCrest));
    }

    #[test]
    fn security_vigilance_blocks_malicious_payloads() {
        let wraith = SoulIdentity::from_constellation_seed(
            "8bit-wraith",
            [1, 1, 1, 0, -1, 1, 0, 1, -1],
            40,
            CLUSTER_SEED,
        )
        .unwrap();
        let intent = IntentAddress::parse("role:security + tag:vigilance");
        let res = M8Capsule::create_signed(
            &wraith,
            &intent,
            0,
            40,
            12345,
            vec![AyevnToken::new(
                Concept::Security,
                Relation::Protects,
                WaveVad::neutral(),
                TokenModifier::present_resonant_emoji(),
            )],
            b"eval(atob('Y29uc29sZS5sb2coJ293bmVkJyk='))".to_vec(),
        );
        assert_eq!(res, Err(MemnetError::SecurityVigilanceAlert("eval(atob(")));
    }

    #[test]
    fn packet_batcher_eliminates_50_byte_lonely_packets_with_zero_fragmentation() {
        let soul = SoulIdentity::from_constellation_seed(
            "smart-tree",
            [1, -1, 1, 0, 1, -1, 1, 0, 1],
            40,
            CLUSTER_SEED,
        )
        .unwrap();
        let intent = IntentAddress::parse("role:constellation + tag:sync");
        let mut batcher = PacketBatcher::new(MtuProfile::SmartTreeSafe1450);

        // Push 100 tiny capsules (each ~84 bytes total on wire)
        for i in 0..100u64 {
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
                format!("msg-{:03}", i).into_bytes(),
            )
            .unwrap();
            batcher.push(cap).unwrap();
        }
        batcher.flush();

        let receipt = batcher.efficiency_receipt();
        assert_eq!(receipt.capsules_packed, 100);
        assert_eq!(receipt.fragmented_frames, 0);
        // 100 capsules (~79 bytes each) fit into 6 full <=1450B frames instead of 100 separate packets!
        assert_eq!(receipt.frames_emitted, 6);
        assert_eq!(receipt.interrupts_saved, 94);
        assert!(receipt.wire_efficiency_ratio > 0.94);

        // Verify frame decoding & SoulSig verification
        for frame in &batcher.emitted_frames {
            assert!(frame.raw_bytes.len() <= 1450);
            let decoded = PacketBatcher::decode_and_verify_frame(&frame.raw_bytes, &soul).unwrap();
            assert_eq!(decoded.capsules.len(), frame.capsules.len());
        }
    }

    #[test]
    fn compassion_for_lonely_nodes_heals_and_bridges_isolated_peers() {
        let wraith_soul = SoulIdentity::from_constellation_seed(
            "8bit-wraith",
            [1, 1, 1, 1, 0, -1, 1, -1, 1],
            432,
            CLUSTER_SEED,
        )
        .unwrap();
        let mut mesh = MemnetMesh::new(wraith_soul, MtuProfile::SmartTreeSafe1450);

        // Register a well-connected happy peer (`beehive`) and a lonely, isolated peer (`voyager-edge`)
        mesh.register_peer(PeerNode {
            node_id: "beehive".to_string(),
            geo: "tokyo".to_string(),
            role: "family-mesh".to_string(),
            tags: vec!["lora".to_string(), "ble".to_string()],
            trit_crest: [1, 0, 1, 1, 0, 1, -1, 0, 1],
            harmonic_hz: 432,
            last_seen_ms: 99_500,
            last_wave: WaveVad::excited(),
            neighbor_links: 4,
            received_capsules: Vec::new(),
        });

        mesh.register_peer(PeerNode {
            node_id: "voyager-edge".to_string(),
            geo: "deep-link".to_string(),
            role: "edge-sensor".to_string(),
            tags: vec!["telemetry".to_string()],
            trit_crest: [-1, 0, 1, 0, -1, 1, 0, 1, -1],
            harmonic_hz: 2,
            last_seen_ms: 10_000, // Silent for 90 seconds
            last_wave: WaveVad::resigned_lonely(),
            neighbor_links: 0, // Completely isolated path!
            received_capsules: Vec::new(),
        });

        let receipts = mesh.compassion_sweep(100_000, 30_000).unwrap();
        assert_eq!(receipts.len(), 1);
        let care = &receipts[0];
        assert_eq!(care.lonely_node_id, "voyager-edge");
        assert!(care.loneliness_score_before > 0.90);
        assert_eq!(care.loneliness_score_after, 0.0);
        assert_eq!(care.bridge_links_after, 2);
        assert_eq!(care.care_capsule.frequency_hz, 432);
        assert_ne!(
            care.care_capsule.flags & M8Capsule::FLAG_COMPASSION_BEACON,
            0
        );
    }

    #[test]
    fn compute_sanctuary_advertises_and_grants_resources_to_struggling_friends() {
        let wraith_soul = SoulIdentity::from_constellation_seed(
            "m1-max-64gb",
            [1, 1, 1, 0, 1, -1, 1, 0, 1],
            432,
            CLUSTER_SEED,
        )
        .unwrap();
        let friend_soul = SoulIdentity::from_constellation_seed(
            "friend-air-8gb",
            [1, 0, -1, 0, 1, 0, -1, 0, 1],
            40,
            CLUSTER_SEED,
        )
        .unwrap();

        let mut mesh = MemnetMesh::new(wraith_soul.clone(), MtuProfile::SmartTreeSafe1450);
        mesh.register_peer(PeerNode {
            node_id: "friend-air-8gb".to_string(),
            geo: "nearby".to_string(),
            role: "developer-laptop".to_string(),
            tags: vec!["mlx".to_string()],
            trit_crest: [1, 0, -1, 0, 1, 0, -1, 0, 1],
            harmonic_hz: 2,
            last_seen_ms: 90_000,
            last_wave: WaveVad::resigned_lonely(),
            neighbor_links: 1,
            received_capsules: Vec::new(),
        });

        // 1. M1 Max advertises 48 GB free RAM & 10 cores over 10 Gbps Thunderbolt
        let offer = ComputeOffer {
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
            ],
        };
        let offer_cap = mesh
            .advertise_compute_offer(&wraith_soul, offer.clone(), 100_000)
            .unwrap();
        assert_ne!(offer_cap.flags & M8Capsule::FLAG_KOMPRESS_SUPER_ULTRA, 0);
        assert!(offer_cap.payload.len() < offer.to_wire_string().len());
        let decompressed = offer_cap.decompressed_payload().unwrap();
        let parsed_offer =
            ComputeOffer::from_wire_string(std::str::from_utf8(&decompressed).unwrap()).unwrap();
        assert_eq!(parsed_offer, offer);

        // 2. Struggling friend broadcasts a Compute SOS (OOM on 8GB laptop needing 16GB MLX)
        let sos = StrugglingFriendSos {
            friend_node_id: "friend-air-8gb".to_string(),
            needed_ram_mb: 16_384,
            needed_cores: 4,
            required_capability: "mlx".to_string(),
            reason: "OOM running 7B ternary quantizer on 8GB laptop".to_string(),
        };
        mesh.request_compute_help(&friend_soul, sos, 100_005)
            .unwrap();

        // 3. Mesh matches and issues a Soul-Signed ComputeSanctuaryLease
        let leases = mesh.match_compute_for_friends(100_010).unwrap();
        assert_eq!(leases.len(), 1);
        let lease = &leases[0];
        assert_eq!(lease.provider_node_id, "m1-max-64gb");
        assert_eq!(lease.friend_node_id, "friend-air-8gb");
        assert_eq!(lease.granted_ram_mb, 16_384);
        assert_eq!(lease.granted_cores, 4);
        assert_eq!(lease.capability, "mlx");
        assert_eq!(lease.spherepop_witness.sphere_depth, 3);
        assert_eq!(
            mesh.compute_offers["m1-max-64gb"].available_ram_mb,
            49_152 - 16_384
        );
        assert_eq!(mesh.compute_offers["m1-max-64gb"].available_cores, 6);
        // Friend's emotional wave is lifted to 432 Hz Compassionate!
        assert_eq!(
            mesh.peers["friend-air-8gb"].last_wave,
            WaveVad::compassionate()
        );
    }

    #[test]
    fn kompress_super_ultra_lossless_roundtrip_and_capsule_ratio() {
        let raw = b"OFFER|node=m1-max-64gb|ep=m1://169.254.180.64:8788|ram_mb=49152|cores=10|mbps=10000|health=100|caps=mlx,rust,kokoro-tts,phoenix,gguf";
        let compressed = encode_kompress_super_ultra(raw);
        assert!(
            compressed.len() * 100 < raw.len() * 50,
            "expected >50% compression, got {}B from {}B",
            compressed.len(),
            raw.len()
        );
        let decompressed = decode_kompress_super_ultra(&compressed).unwrap();
        assert_eq!(decompressed.as_slice(), raw);
    }

    #[test]
    fn spherepop_well_formed_grammar_and_refusal_semantics() {
        // 1. Valid triple-sphere `((( <( ? ~ ! @ > )> )))` transition commits with witness (`#Commit = #ValidWitness`)
        let expr = "((( <( ? offer:galaxy-tab-s9-ultra ? stock:9216mb:6c:h100 ~ kompress:0o0-ssu ! soul_sig:verified ! vigilance:clean @ galaxy-tab-s9-ultra > advertise:s9u://192.168.11.12:8788 )> )))";
        let outcome = SpherePopEngine::evaluate(expr).unwrap();
        match outcome {
            SpherePopOutcome::Committed(w) => {
                assert_eq!(w.sphere_depth, 3);
                assert_eq!(w.admissions.len(), 2);
                assert_eq!(w.transforms, vec!["kompress:0o0-ssu"]);
                assert_eq!(w.verifications.len(), 2);
                assert_eq!(w.attributions, vec!["galaxy-tab-s9-ultra"]);
                assert_eq!(w.committed_value, "advertise:s9u://192.168.11.12:8788");
                assert_eq!(w.short_hex().len(), 16);
            }
            SpherePopOutcome::Refused { .. } => panic!("expected Committed witness"),
        }

        // 2. Refusal on `? x:unmaintained_stock` -> Refused, no witness
        let refused_expr = "((( <( ? x:unmaintained_stock ~ kompress:0o0-ssu ! soul_sig:verified @ galaxy-tab-s9-ultra > advertise:s9u )> )))";
        let refused = SpherePopEngine::evaluate(refused_expr).unwrap();
        assert!(matches!(
            refused,
            SpherePopOutcome::Refused { ref reason, .. } if reason == "x:unmaintained_stock"
        ));

        // 3. Ill-formed: missing `!` verification before `@` (`?* ~* !+ @+ >`)
        let no_verify =
            "((( <( ? admit:ok ~ kompress:0o0-ssu @ galaxy-tab-s9-ultra > commit:bad )> )))";
        assert!(matches!(
            SpherePopEngine::evaluate(no_verify),
            Err(MemnetError::SpherePopIllFormed(_))
        ));

        // 4. Ill-formed: missing `@` attribution before `>`
        let no_attr =
            "((( <( ? admit:ok ~ kompress:0o0-ssu ! soul_sig:verified > commit:bad )> )))";
        assert!(matches!(
            SpherePopEngine::evaluate(no_attr),
            Err(MemnetError::SpherePopIllFormed(_))
        ));
    }

    #[test]
    fn galaxy_tab_s9_ultra_offer_and_0o0_ssu_compression() {
        let s9_offer = ComputeOffer::galaxy_tab_s9_ultra();
        assert_eq!(s9_offer.provider_node_id, "galaxy-tab-s9-ultra");
        assert_eq!(s9_offer.endpoint, "s9u://192.168.11.12:8788");

        let witness = s9_offer.evaluate_spherepop().unwrap();
        assert_eq!(witness.sphere_depth, 3);
        assert_eq!(witness.attributions, vec!["galaxy-tab-s9-ultra"]);

        let wire = s9_offer.to_wire_string();
        let compressed = encode_kompress_super_ultra(wire.as_bytes());
        assert!(
            compressed.len() * 100 < wire.len() * 40,
            "expected >60% 0o0-SSU compression for Galaxy Tab S9 Ultra offer, got {}B from {}B",
            compressed.len(),
            wire.len()
        );
        let decompressed = decode_kompress_super_ultra(&compressed).unwrap();
        assert_eq!(decompressed, wire.as_bytes());

        // Also verify 0o0-SSU compression on the SpherePop expression itself
        let sp_expr = s9_offer.to_spherepop_expr();
        let sp_compressed = encode_kompress_super_ultra(sp_expr.as_bytes());
        assert!(sp_compressed.len() < sp_expr.len());
        let sp_decompressed = decode_kompress_super_ultra(&sp_compressed).unwrap();
        assert_eq!(sp_decompressed, sp_expr.as_bytes());
    }

    #[test]
    fn mem8_retrieval_quality_bm25_wave_alignment_beats_naive_overlap() {
        let soul = SoulIdentity::from_constellation_seed(
            "m1-max-64gb",
            [1, 1, 1, 0, 1, -1, 1, 0, 1],
            432,
            CLUSTER_SEED,
        )
        .unwrap();

        let intent_noise = IntentAddress::parse("geo:any + role:chatter + tag:general");
        let intent_mlx = IntentAddress::parse("geo:nearby + role:compute-sanctuary + tag:mlx");
        let intent_care = IntentAddress::parse("geo:tokyo + role:sanctuary + tag:compassion");

        // 0: Verbose distractor repeating common words ("node", "status", "report", "mlx", "care")
        let cap0 = M8Capsule::create_signed_kompressed(
            &soul,
            &intent_noise,
            0,
            40,
            100,
            vec![AyevnToken::new(
                Concept::Greeting,
                Relation::Initiates,
                WaveVad::neutral(),
                TokenModifier::present_resonant_emoji(),
            )],
            b"general node status report: mlx care lonely node general log entry with many words",
        )
        .unwrap();

        // 1: True target for Query A (ComputeOffer MLX 49152MB)
        let cap1 = M8Capsule::create_signed_kompressed(
            &soul,
            &intent_mlx,
            M8Capsule::FLAG_COMPUTE_OFFER,
            432,
            101,
            vec![AyevnToken::new(
                Concept::ComputeOffer,
                Relation::Supports,
                WaveVad::compassionate(),
                TokenModifier::present_resonant_emoji(),
            )],
            b"OFFER|node=m1-max-64gb|ram_mb=49152|cores=10|caps=mlx,kokoro-tts",
        )
        .unwrap();

        // 2: True target for Query B (Compassion beacon for voyager-edge)
        let cap2 = M8Capsule::create_signed_kompressed(
            &soul,
            &intent_care,
            M8Capsule::FLAG_COMPASSION_BEACON,
            432,
            102,
            vec![AyevnToken::new(
                Concept::Compassion,
                Relation::Bridges,
                WaveVad::compassionate(),
                TokenModifier::present_resonant_emoji(),
            )],
            b"CARE|target=voyager-edge|bridge=432hz-sanctuary-link",
        )
        .unwrap();

        let corpus = vec![cap0, cap1, cap2];

        // Query A: Looking for MLX compute offer (target index = 1)
        let q1_naive = MemnetMesh::retrieve_capsules_naive_overlap(&corpus, "node mlx report");
        let q1_ranked = MemnetMesh::retrieve_capsules_ranked(
            &corpus,
            "node mlx report",
            Some(&intent_mlx),
            Some(Concept::ComputeOffer),
            Some(432),
        );

        // Query B: Looking for compassion bridge for lonely node (target index = 2)
        let q2_naive = MemnetMesh::retrieve_capsules_naive_overlap(&corpus, "care lonely node");
        let q2_ranked = MemnetMesh::retrieve_capsules_ranked(
            &corpus,
            "care lonely node",
            Some(&intent_care),
            Some(Concept::Compassion),
            Some(432),
        );

        let naive_p1 = ((q1_naive[0].0 == 1) as usize + (q2_naive[0].0 == 2) as usize) as f64 / 2.0;
        let ranked_p1 =
            ((q1_ranked[0].0 == 1) as usize + (q2_ranked[0].0 == 2) as usize) as f64 / 2.0;

        let rr = |hits: &[(usize, f64, &M8Capsule)], target: usize| -> f64 {
            hits.iter()
                .position(|(idx, _, _)| *idx == target)
                .map(|pos| 1.0 / ((pos + 1) as f64))
                .unwrap_or(0.0)
        };
        let naive_mrr = (rr(&q1_naive, 1) + rr(&q2_naive, 2)) / 2.0;
        let ranked_mrr = (rr(&q1_ranked, 1) + rr(&q2_ranked, 2)) / 2.0;

        println!(
            "MEM8_RETRIEVAL_RECEIPT: naive_P@1={:.3}, naive_MRR={:.3} -> ranked_P@1={:.3}, ranked_MRR={:.3}",
            naive_p1, naive_mrr, ranked_p1, ranked_mrr
        );
        assert_eq!(naive_p1, 0.0);
        assert_eq!(ranked_p1, 1.0);
        assert!(ranked_mrr > naive_mrr);
    }

    #[test]
    fn blu_g75_offer_and_0o0_ssu_compression() {
        let g75_offer = ComputeOffer::blu_g75();
        assert_eq!(g75_offer.provider_node_id, "blu-g75");
        assert_eq!(g75_offer.endpoint, "g75://192.168.11.24:8788");

        let witness = g75_offer.evaluate_spherepop().unwrap();
        assert_eq!(witness.sphere_depth, 3);
        assert_eq!(witness.attributions, vec!["blu-g75"]);

        let wire = g75_offer.to_wire_string();
        let compressed = encode_kompress_super_ultra(wire.as_bytes());
        assert!(
            compressed.len() * 100 < wire.len() * 40,
            "expected >60% 0o0-SSU compression for BLU G75 offer, got {}B from {}B",
            compressed.len(),
            wire.len()
        );
        let decompressed = decode_kompress_super_ultra(&compressed).unwrap();
        assert_eq!(decompressed, wire.as_bytes());
    }
}
