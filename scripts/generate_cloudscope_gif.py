import math
import os
import sys
import time
import random
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# CONFIGURATION & HIGH-DPI PARAMETERS
# ==========================================
WIDTH_2X, HEIGHT_2X = 1920, 1080
TARGET_WIDTH, TARGET_HEIGHT = 960, 540
TOTAL_FRAMES = 84
FPS = 12

OUTPUT_DIR = "static"
OUTPUT_GIF = os.path.join(OUTPUT_DIR, "cloudscope_gold_standard_swarm.gif")
BRAIN_ARTIFACT_PATH = "/Users/aniketagrawal/.gemini/antigravity/brain/324fb70a-83ef-46dd-9f17-132b9efb6128/cloudscope_gold_standard_swarm.gif"
ARTIFACTS_DIR_PATH = "artifacts/cloudscope_gold_standard_swarm.gif"

# Google Sans TrueType Fonts
FONTS = {
    "display_bold": ImageFont.truetype("/Library/Fonts/GoogleSansDisplay-Bold.ttf", 44),
    "gate_title": ImageFont.truetype("/Library/Fonts/GoogleSansDisplay-Bold.ttf", 32),
    "hud_score": ImageFont.truetype("/Library/Fonts/GoogleSansDisplay-Bold.ttf", 38),
    "header_brand": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 32),
    "header_sub": ImageFont.truetype("/Library/Fonts/GoogleSans-Medium.ttf", 28),
    "presenter_name": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 22),
    "presenter_role": ImageFont.truetype("/Library/Fonts/GoogleSans-Medium.ttf", 17),
    "node_title": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 21),
    "node_sub": ImageFont.truetype("/Library/Fonts/GoogleSans-Regular.ttf", 15),
    "hud_header": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 24),
    "hud_sub": ImageFont.truetype("/Library/Fonts/GoogleSans-Regular.ttf", 17),
    "math_formula": ImageFont.truetype("/Library/Fonts/GoogleSans-Medium.ttf", 16),
    "metric_title": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 18),
    "metric_badge": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 15),
    "metric_desc": ImageFont.truetype("/Library/Fonts/GoogleSans-Regular.ttf", 14),
    "claim_title": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 16),
    "claim_text": ImageFont.truetype("/Library/Fonts/GoogleSans-Regular.ttf", 15),
    "gate_bullet": ImageFont.truetype("/Library/Fonts/GoogleSans-Medium.ttf", 17),
    "pill_text": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 18),
    "bottom_brand": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 21),
    "bottom_name": ImageFont.truetype("/Library/Fonts/GoogleSans-Bold.ttf", 21),
    "bottom_sub": ImageFont.truetype("/Library/Fonts/GoogleSans-Medium.ttf", 18),
}

# Official Google Cloud Palette & Neon Accents
C_GOOGLE_BLUE   = (66, 133, 244)
C_GOOGLE_RED    = (234, 67, 53)
C_GOOGLE_YELLOW = (251, 188, 4)
C_GOOGLE_GREEN  = (52, 168, 83)
C_CYAN          = (0, 229, 255)
C_EMERALD       = (0, 230, 118)
C_GOLD          = (255, 215, 0)
C_WHITE         = (255, 255, 255)
C_PLATINUM      = (226, 232, 240)
C_SLATE         = (148, 163, 184)
C_DARK_SLATE    = (71, 85, 105)
C_BG_DEEP       = (8, 12, 24)

# Fixed Starfield Seeds for Consistent Cyclic Parallax
random.seed(42)
STARFIELD = [
    (random.randint(40, WIDTH_2X - 40), random.randint(30, HEIGHT_2X - 30), random.uniform(0.5, 2.0), random.uniform(0.0, 2.0 * math.pi))
    for _ in range(40)
]

# Graph Topology Definition
NODES = [
    {
        "id": "hub",
        "label": "A3J VERIFIER",
        "sub": "Mathematical Proof Kernel",
        "x": 520, "y": 485,
        "radius": 68,
        "color": C_GOOGLE_BLUE,
    },
    {
        "id": "transit",
        "label": "Silicon Valley Transit",
        "sub": "Multimodal (Waymo/Caltrain)",
        "x": 230, "y": 265,
        "radius": 46,
        "color": C_GOOGLE_YELLOW,
    },
    {
        "id": "heritage",
        "label": "Heritage Concierge",
        "sub": "Cultural Knowledge Subgraph",
        "x": 810, "y": 265,
        "radius": 46,
        "color": C_GOOGLE_RED,
    },
    {
        "id": "nature",
        "label": "Nature & Wine Specialist",
        "sub": "Scenic & Winery Subgraph",
        "x": 810, "y": 705,
        "radius": 46,
        "color": C_GOOGLE_GREEN,
    },
    {
        "id": "ontology",
        "label": "GraphRAG Engine",
        "sub": "231 Verified Entities & Hops",
        "x": 230, "y": 705,
        "radius": 46,
        "color": C_CYAN,
    }
]

# Swarm Connections: Hub Spokes and Perimeter
EDGES = [
    (0, 1), (0, 2), (0, 3), (0, 4), # Hub spokes
    (1, 2), (2, 3), (3, 4), (4, 1), # Ring perimeter
]

# Dijkstra Verified Ground-Truth Path for Dynamic Laser Highlighting
DIJKSTRA_PATH = [1, 0, 2, 3] # Transit -> A3J Hub -> Heritage -> Nature

# Live Verification Ticker Claims
CLAIMS_TICKER = [
    ("CLAIM [1/3] Silicon Valley Mobility Corridor", "Waymo SFO Intercampus -> Caltrain EMU #156 -> Googleplex | Dijkstra: OPTIMAL | THD: 0.00"),
    ("CLAIM [2/3] India Tech & Aviation Subgraph", "BLR Kempegowda T2 -> Air India Express Corridor -> RMZ Ecoworld | SE: 0.98 | PASSED"),
    ("CLAIM [3/3] Heritage & Ecological Buffer", "NDLS Vande Bharat 20172 -> Agra Cantt -> TTZ Eco Zone | Zero Diesel | 100% COMPLIANT"),
]

def draw_rounded_box(draw, bbox, radius, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = bbox
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline, width=width)

def draw_progress_bar(draw, bbox, progress, fill_color, bg_color=(20, 30, 50)):
    x0, y0, x1, y1 = bbox
    draw.rounded_rectangle([x0, y0, x1, y1], radius=6, fill=bg_color)
    bar_width = int((x1 - x0) * max(0.0, min(1.0, progress)))
    if bar_width > 8:
        draw.rounded_rectangle([x0, y0, x0 + bar_width, y1], radius=6, fill=fill_color)

def draw_google_dots(draw, x, y, size=16, spacing=22):
    colors = [C_GOOGLE_BLUE, C_GOOGLE_RED, C_GOOGLE_YELLOW, C_GOOGLE_GREEN]
    for i, color in enumerate(colors):
        cx = x + i * spacing
        draw.ellipse([cx - size//2, y - size//2, cx + size//2, y + size//2], fill=color)

def draw_sparkle(draw, cx, cy, size, color=C_WHITE):
    # 4-point diamond sparkle star
    draw.polygon([(cx, cy - size), (cx + size*0.25, cy), (cx, cy + size), (cx - size*0.25, cy)], fill=color)
    draw.polygon([(cx - size, cy), (cx, cy + size*0.25), (cx + size, cy), (cx, cy - size*0.25)], fill=color)
    draw.ellipse([cx - size*0.3, cy - size*0.3, cx + size*0.3, cy + size*0.3], fill=C_WHITE)

# ==========================================
# FRAME RENDER PIPELINE
# ==========================================
def render_frame(frame_idx):
    progress = frame_idx / float(TOTAL_FRAMES)
    cycle_angle = progress * 2.0 * math.pi

    # Base Canvas (Deep Space Google Navy)
    img = Image.new("RGBA", (WIDTH_2X, HEIGHT_2X), (9, 14, 28, 255))
    draw = ImageDraw.Draw(img)

    # 1. Subtle High-Tech Grid & Background Starfield
    grid_spacing = 80
    for gx in range(0, WIDTH_2X, grid_spacing):
        draw.line([(gx, 0), (gx, HEIGHT_2X)], fill=(18, 30, 52, 40), width=1)
    for gy in range(0, HEIGHT_2X, grid_spacing):
        draw.line([(0, gy), (WIDTH_2X, gy)], fill=(18, 30, 52, 40), width=1)

    # Twinkling Stars
    for sx, sy, s_rad, s_phase in STARFIELD:
        star_twinkle = (math.sin(cycle_angle + s_phase) + 1.0) / 2.0
        s_alpha = int(70 + 130 * star_twinkle)
        r = s_rad * (0.8 + 0.4 * star_twinkle)
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(200, 220, 255, s_alpha))

    # 2. Google 4-Color Glowing Top Accent Rail (Widescreen Brand Bar)
    rail_seg = WIDTH_2X // 4
    draw.line([(0, 2), (rail_seg, 2)], fill=C_GOOGLE_BLUE, width=4)
    draw.line([(rail_seg, 2), (rail_seg*2, 2)], fill=C_GOOGLE_RED, width=4)
    draw.line([(rail_seg*2, 2), (rail_seg*3, 2)], fill=C_GOOGLE_YELLOW, width=4)
    draw.line([(rail_seg*3, 2), (WIDTH_2X, 2)], fill=C_GOOGLE_GREEN, width=4)
    # Scanning Light Glint across top rail
    glint_x = int(progress * WIDTH_2X)
    draw.ellipse([glint_x - 40, 0, glint_x + 40, 4], fill=(255, 255, 255, 220))

    # ==========================================
    # 3. KEYNOTE HEADER & EXECUTIVE PRESENTER
    # ==========================================
    # Google 4-Color Emblem
    draw_google_dots(draw, 65, 68, size=18, spacing=24)

    # Header Titles
    brand_text = "Google Cloud"
    draw.text((165, 48), brand_text, font=FONTS["header_brand"], fill=C_WHITE)
    sep_x = 165 + draw.textlength(brand_text, font=FONTS["header_brand"]) + 12
    draw.text((sep_x, 50), "|", font=FONTS["header_brand"], fill=C_SLATE)
    keynote_x = sep_x + 18
    draw.text((keynote_x, 51), "CloudScope 2026 Keynote", font=FONTS["header_sub"], fill=C_CYAN)

    sub_title = "Vertex AI Autonomous Swarms • Zero-Hallucination GraphRAG • Agent-as-a-Judge (A3J)"
    draw.text((165, 92), sub_title, font=FONTS["metric_desc"], fill=C_SLATE)

    # Center/Right Executive Presenter Pill: ANIKET AGRAWAL
    pres_pulse = (math.sin(cycle_angle * 2.0) + 1.0) / 2.0
    pres_border = (int(66 + 30 * pres_pulse), int(133 + 40 * pres_pulse), 244)
    draw_rounded_box(draw, (860, 40, 1420, 105), radius=28, fill=(14, 25, 50, 240), outline=pres_border, width=2)
    # Presenter Icon & Full Name
    draw.text((885, 55), "👤", font=FONTS["presenter_name"], fill=C_GOLD)
    draw.text((922, 53), "Aniket Agrawal", font=FONTS["presenter_name"], fill=C_GOLD)
    draw.text((1095, 56), "|", font=FONTS["presenter_role"], fill=C_SLATE)
    draw.text((1115, 56), "Lead AI Architect & Presenter", font=FONTS["presenter_role"], fill=C_CYAN)
    draw.text((922, 80), "Google Cloud AI • DeepMind Autonomous Systems", font=FONTS["metric_desc"], fill=C_PLATINUM)

    # Right Status Pill: 100% PROD-READY
    badge_pulse = (math.sin(cycle_angle * 3.0) + 1.0) / 2.0
    pill_border = (int(0 + 30 * badge_pulse), 230, int(118 + 50 * badge_pulse))
    draw_rounded_box(draw, (1450, 40, 1865, 105), radius=28, fill=(10, 36, 26, 240), outline=pill_border, width=2)
    dot_radius = 6 + int(3 * badge_pulse)
    draw.ellipse([1482 - dot_radius, 68 - dot_radius, 1482 + dot_radius, 68 + dot_radius], fill=C_EMERALD)
    draw.text((1502, 53), "100% PRODUCTION VERIFIED", font=FONTS["pill_text"], fill=C_WHITE)
    draw.text((1502, 78), "231 / 231 Automated Benchmarks Pass", font=FONTS["metric_desc"], fill=C_EMERALD)

    # ==========================================
    # 4. LEFT PANEL: MULTI-AGENT SWARM GRAPH
    # ==========================================
    draw_rounded_box(draw, (55, 130, 985, 945), radius=20, fill=(13, 20, 38, 230), outline=(40, 65, 105, 180), width=2)
    
    # Graph Card Header
    draw.text((85, 150), "KNOWLEDGE GRAPH SWARM TOPOLOGY", font=FONTS["hud_header"], fill=C_WHITE)
    draw.text((85, 182), "Real-Time Multi-Agent Orchestration & Relational Graph Hops", font=FONTS["metric_desc"], fill=C_CYAN)

    # Active Dijkstra Path Laser Highlighting (Gold/Emerald Tracer)
    dijkstra_pulse = (math.sin(cycle_angle * 4.0) + 1.0) / 2.0
    for idx in range(len(DIJKSTRA_PATH) - 1):
        u = NODES[DIJKSTRA_PATH[idx]]
        v = NODES[DIJKSTRA_PATH[idx+1]]
        # Glowing Dijkstra Gold Path
        draw.line([(u["x"], u["y"]), (v["x"], v["y"])], fill=(255, 215, 0, int(90 + 80 * dijkstra_pulse)), width=7)

    # Render All Base Graph Edges
    for u_idx, v_idx in EDGES:
        u = NODES[u_idx]
        v = NODES[v_idx]
        draw.line([(u["x"], u["y"]), (v["x"], v["y"])], fill=(35, 65, 115, 160), width=3)

        # Traveling Data Energy Packets
        num_packets = 2
        for p in range(num_packets):
            packet_t = (progress * 2.0 + p / float(num_packets) + (u_idx * 0.17)) % 1.0
            px = u["x"] + (v["x"] - u["x"]) * packet_t
            py = u["y"] + (v["y"] - u["y"]) * packet_t
            
            packet_color = C_CYAN if (u_idx == 0 or v_idx == 0) else C_GOOGLE_YELLOW
            draw.ellipse([px - 7, py - 7, px + 7, py + 7], fill=(packet_color[0], packet_color[1], packet_color[2], 100))
            draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=C_WHITE)

    # Render Hub Concentric Radar Waves
    hub = NODES[0]
    for wave_offset in [0.0, 0.5]:
        wave_t = (progress + wave_offset) % 1.0
        wave_r = hub["radius"] + int(115 * wave_t)
        wave_alpha = int(180 * (1.0 - wave_t))
        if wave_alpha > 0:
            draw.ellipse([hub["x"] - wave_r, hub["y"] - wave_r, hub["x"] + wave_r, hub["y"] + wave_r],
                         outline=(66, 133, 244, wave_alpha), width=2)

    # Render Agent Nodes
    for i, node in enumerate(NODES):
        nx, ny, nr = node["x"], node["y"], node["radius"]
        ncol = node["color"]

        # Outer Glow Ring
        glow_r = nr + 8
        draw.ellipse([nx - glow_r, ny - glow_r, nx + glow_r, ny + glow_r], outline=(ncol[0], ncol[1], ncol[2], 120), width=3)
        # Node Body
        draw.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], fill=(16, 26, 48), outline=ncol, width=3)

        if i == 0:
            # Hub Core
            draw.text((nx - 62, ny - 24), "A3J CORE", font=FONTS["node_title"], fill=C_WHITE)
            draw.text((nx - 48, ny + 4), "VERIFIER", font=FONTS["node_title"], fill=C_CYAN)
            draw.text((nx - 105, ny + 76), node["sub"], font=FONTS["metric_desc"], fill=C_PLATINUM)
        else:
            # Subagent nodes
            draw.ellipse([nx - 10, ny - 10, nx + 10, ny + 10], fill=ncol)
            t_w = draw.textlength(node["label"], font=FONTS["node_title"])
            draw.text((nx - t_w // 2, ny + nr + 12), node["label"], font=FONTS["node_title"], fill=C_WHITE)
            s_w = draw.textlength(node["sub"], font=FONTS["node_sub"])
            draw.text((nx - s_w // 2, ny + nr + 36), node["sub"], font=FONTS["node_sub"], fill=C_SLATE)

    # Live Neuro-Symbolic Latency Waveform & Inference Sparkline (Bottom of Left Card)
    draw_rounded_box(draw, (80, 810, 960, 925), radius=14, fill=(16, 26, 50, 240), outline=(45, 75, 125, 160))
    # Waveform drawing across width
    wave_x0, wave_x1 = 105, 935
    wave_y_mid = 848
    pts = []
    for wx in range(wave_x0, wave_x1, 8):
        dx = (wx - wave_x0) / float(wave_x1 - wave_x0)
        wy = wave_y_mid + int(10 * math.sin(dx * 12.0 + cycle_angle * 3.0) + 6 * math.cos(dx * 6.0 - cycle_angle * 2.0))
        pts.append((wx, wy))
    for p_idx in range(len(pts) - 1):
        draw.line([pts[p_idx], pts[p_idx+1]], fill=C_CYAN, width=2)
    # Animated packet on the wave
    wave_cursor_x = wave_x0 + int(progress * (wave_x1 - wave_x0))
    wave_cursor_y = wave_y_mid + int(10 * math.sin(((wave_cursor_x - wave_x0)/float(wave_x1 - wave_x0)) * 12.0 + cycle_angle * 3.0))
    draw.ellipse([wave_cursor_x - 5, wave_cursor_y - 5, wave_cursor_x + 5, wave_cursor_y + 5], fill=C_WHITE)

    # Waveform Caption & Stats
    draw.text((105, 872), "🧠 Live Neuro-Symbolic Latency: 18.4ms", font=FONTS["gate_bullet"], fill=C_PLATINUM)
    draw.text((435, 874), "• Closed-World Ground Truth Bound", font=FONTS["metric_desc"], fill=C_EMERALD)
    draw.text((105, 898), "• 4 Active Swarms   • 231 Verified Entities   • 0 Hallucinations Detected", font=FONTS["metric_desc"], fill=C_SLATE)

    # ==========================================
    # 5. RIGHT PANEL: A3J TELEMETRY & GATE
    # ==========================================
    draw_rounded_box(draw, (1020, 130, 1865, 945), radius=20, fill=(13, 20, 38, 230), outline=(40, 65, 105, 180), width=2)
    
    # Header & Mathematical Formula Badge
    draw.text((1050, 150), "A3J MATHEMATICAL AUDIT TELEMETRY", font=FONTS["hud_header"], fill=C_WHITE)
    draw.text((1050, 182), "Rigorous Dijkstra Proof: S_comp = exp(-THD) * SE >= 0.85  ──>  1.00 * 0.96 = 0.96", font=FONTS["math_formula"], fill=C_CYAN)

    # Metric Card 1: THD (Topological Hallucination Distance)
    draw_rounded_box(draw, (1050, 215, 1835, 335), radius=14, fill=(18, 28, 52), outline=(35, 60, 100), width=1)
    draw.text((1075, 228), "TOPOLOGICAL HALLUCINATION DISTANCE (THD)", font=FONTS["metric_title"], fill=C_SLATE)
    draw.text((1075, 255), "0.00", font=FONTS["hud_score"], fill=C_EMERALD)
    draw_rounded_box(draw, (1205, 258, 1475, 298), radius=16, fill=(10, 48, 30), outline=C_EMERALD)
    draw.text((1221, 268), "100% ZERO DRIFT", font=FONTS["metric_badge"], fill=C_EMERALD)
    draw_progress_bar(draw, (1075, 308, 1810, 320), 1.0, C_EMERALD)

    # Metric Card 2: SE (Semantic Entailment)
    draw_rounded_box(draw, (1050, 350, 1835, 470), radius=14, fill=(18, 28, 52), outline=(35, 60, 100), width=1)
    draw.text((1075, 363), "SEMANTIC NLI ENTAILMENT (SE)", font=FONTS["metric_title"], fill=C_SLATE)
    draw.text((1075, 390), "0.96", font=FONTS["hud_score"], fill=C_CYAN)
    draw_rounded_box(draw, (1205, 393, 1475, 433), radius=16, fill=(10, 40, 56), outline=C_CYAN)
    draw.text((1221, 403), "HIGH NLI CONFIDENCE", font=FONTS["metric_badge"], fill=C_CYAN)
    draw_progress_bar(draw, (1075, 443, 1810, 455), 0.96, C_CYAN)

    # Metric Card 3: S_comp (Composite Safety Score)
    draw_rounded_box(draw, (1050, 485, 1835, 605), radius=14, fill=(18, 28, 52), outline=(35, 60, 100), width=1)
    draw.text((1075, 498), "COMPOSITE SAFETY SCORE (S_comp)", font=FONTS["metric_title"], fill=C_SLATE)
    draw.text((1075, 525), "1.00", font=FONTS["hud_score"], fill=C_GOOGLE_YELLOW)
    draw_rounded_box(draw, (1205, 528, 1475, 568), radius=16, fill=(45, 38, 12), outline=C_GOOGLE_YELLOW)
    draw.text((1221, 538), "OPTIMAL PROOF", font=FONTS["metric_badge"], fill=C_GOOGLE_YELLOW)
    draw_progress_bar(draw, (1075, 578, 1810, 590), 1.0, C_GOOGLE_YELLOW)

    # Dynamic Live Claim Ticker Console (Cycles across 3 scenarios)
    draw_rounded_box(draw, (1050, 620, 1835, 715), radius=14, fill=(12, 22, 42), outline=(40, 75, 120), width=1)
    claim_idx = int(progress * len(CLAIMS_TICKER)) % len(CLAIMS_TICKER)
    c_title, c_text = CLAIMS_TICKER[claim_idx]
    
    # Pulsing Live Dot + Claim Header
    draw.ellipse([1075, 638, 1087, 650], fill=C_EMERALD)
    draw.text((1097, 635), c_title, font=FONTS["claim_title"], fill=C_CYAN)
    draw.text((1075, 668), c_text, font=FONTS["claim_text"], fill=C_PLATINUM)

    # Gate Deployment Card
    gate_pulse = (math.sin(cycle_angle * 3.0) + 1.0) / 2.0
    gate_border = (int(0 + 40 * gate_pulse), 230, int(118 + 60 * gate_pulse))
    draw_rounded_box(draw, (1050, 730, 1835, 925), radius=16, fill=(8, 38, 25, 230), outline=gate_border, width=3)
    
    # Gate Header & Sparkle Star
    draw.text((1080, 748), "🛡️  A3J GATE: ALLOW_DEPLOYMENT", font=FONTS["gate_title"], fill=C_EMERALD)
    draw_sparkle(draw, 1795, 768, size=14 + int(6 * gate_pulse), color=C_GOLD)
    
    # Checklist Bullets
    bullets = [
        "✓ 231 / 231 Automated E2E Benchmark Test Cases Passed (100.0%)",
        "✓ Zero-Hallucination GraphRAG Grounded in Closed-World Ontology",
        "✓ Keynote Ready for CloudScope 2026 Presentation by Aniket Agrawal",
    ]
    for b_idx, bullet in enumerate(bullets):
        draw.text((1080, 800 + b_idx * 36), bullet, font=FONTS["gate_bullet"], fill=C_PLATINUM)

    # ==========================================
    # 6. BOTTOM RIBBON / DIAMOND PRESENTATION BAR
    # ==========================================
    draw_rounded_box(draw, (55, 960, 1865, 1050), radius=16, fill=(12, 18, 34, 240), outline=(45, 70, 115, 180), width=2)
    
    # Shimmer sweep effect
    shimmer_center = -300 + int(progress * (WIDTH_2X + 600))
    shimmer_width = 280
    sx0 = max(60, shimmer_center - shimmer_width)
    sx1 = min(1860, shimmer_center + shimmer_width)
    if sx1 > sx0:
        draw.rectangle([sx0, 962, sx1, 1048], fill=(255, 255, 255, 20))

    # Diamond text elements featuring Aniket Agrawal
    draw.text((85, 988), "💎  DIAMOND QUALITY GOLD STANDARD", font=FONTS["bottom_brand"], fill=C_WHITE)
    draw.text((585, 990), "•", font=FONTS["bottom_brand"], fill=C_GOOGLE_BLUE)
    draw.text((610, 988), "Engineered & Presented by Aniket Agrawal", font=FONTS["bottom_name"], fill=C_GOLD)
    draw.text((1150, 990), "•", font=FONTS["bottom_brand"], fill=C_GOOGLE_RED)
    draw.text((1175, 989), "Google Cloud Vertex AI & DeepMind Swarms", font=FONTS["bottom_sub"], fill=C_CYAN)
    draw.text((1630, 990), "•", font=FONTS["bottom_brand"], fill=C_GOOGLE_GREEN)
    draw.text((1655, 989), "231/231 Verified Clean", font=FONTS["bottom_sub"], fill=C_EMERALD)

    # 7. High-Quality 2x Supersampling Downsample
    final_frame = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
    return final_frame.convert("RGB")

# ==========================================
# MAIN EXECUTION
# ==========================================
def main():
    start_time = time.time()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(BRAIN_ARTIFACT_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(ARTIFACTS_DIR_PATH), exist_ok=True)

    print(f"🎬 Starting render of {TOTAL_FRAMES} frames ({WIDTH_2X}x{HEIGHT_2X} -> {TARGET_WIDTH}x{TARGET_HEIGHT})...")
    frames = []
    
    for i in range(TOTAL_FRAMES):
        f_start = time.time()
        frame = render_frame(i)
        frames.append(frame)
        f_elapsed = (time.time() - f_start) * 1000.0
        if (i + 1) % 12 == 0 or i == 0:
            print(f"  Frame [{i+1:2d}/{TOTAL_FRAMES}] rendered in {f_elapsed:.1f}ms")

    render_elapsed = time.time() - start_time
    print(f"✅ All {TOTAL_FRAMES} frames rendered in {render_elapsed:.2f}s.")

    print(f"💾 Saving GIF with palette quantization (colors=256, duration={1000//FPS}ms, loop=0)...")
    save_start = time.time()
    
    frames[0].save(
        OUTPUT_GIF,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000.0 / FPS),
        loop=0,
        optimize=True,
    )
    save_elapsed = time.time() - save_start
    gif_size_mb = os.path.getsize(OUTPUT_GIF) / (1024 * 1024)
    print(f"🎉 Generated {OUTPUT_GIF} ({gif_size_mb:.2f} MB) in {save_elapsed:.2f}s!")

    import shutil
    shutil.copy2(OUTPUT_GIF, BRAIN_ARTIFACT_PATH)
    shutil.copy2(OUTPUT_GIF, ARTIFACTS_DIR_PATH)
    print(f"📋 Copied to:\n  -> {BRAIN_ARTIFACT_PATH}\n  -> {ARTIFACTS_DIR_PATH}")

if __name__ == "__main__":
    main()
