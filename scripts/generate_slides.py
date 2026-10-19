"""
Executive 2-Slide Presentation Deck Generator for Google CloudScope Showcase.
Uses python-pptx to generate professional, executive-grade widescreen slides.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_executive_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette
    BG_COLOR = RGBColor(11, 17, 32)        # Deep Navy
    PANEL_BG = RGBColor(15, 23, 42)        # Slate Dark
    ACCENT_BLUE = RGBColor(56, 189, 248)   # Sky Blue
    ACCENT_GREEN = RGBColor(16, 185, 129)  # Emerald Green
    ACCENT_PURPLE = RGBColor(139, 92, 246) # Violet
    TEXT_WHITE = RGBColor(248, 250, 252)   # Bright White
    TEXT_MUTED = RGBColor(148, 163, 184)   # Slate Light

    blank_slide_layout = prs.slide_layouts[6]

    # ==============================================================================
    # SLIDE 1: VISION & MULTI-DOMAIN SWARM ARCHITECTURE
    # ==============================================================================
    slide1 = prs.slides.add_slide(blank_slide_layout)
    
    # Background
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_COLOR
    bg1.line.color.rgb = BG_COLOR

    # Header Box
    header_box = slide1.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
    tf1 = header_box.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "Autonomous Gemini Enterprise Swarms: Zero-Hallucination GraphRAG & A3J"
    p1.font.bold = True
    p1.font.size = Pt(26)
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Evolving Enterprise AI from Stochastic 'Vibes-Based' Chat to Deterministic, State-Verifying Swarms | Google CloudScope Showcase"
    p2.font.size = Pt(13)
    p2.font.color.rgb = ACCENT_BLUE

    # 3 Architecture Pillars (Cards)
    cards_data = [
        (
            "1. The Evaluation Crisis",
            "Why LLM-as-a-Judge Fails",
            "• Standard LLM evaluators suffer from Semantic Confirmation Bias: they grade solely on linguistic fluency and miss topological falsehoods.\n• Falsely validates fabricated threat links, invalid stock cross-holdings, and rejected database mutations.\n• Urgent need for 100% deterministic, state-grounded auditing.",
            ACCENT_BLUE
        ),
        (
            "2. Multi-Domain Swarm",
            "ADK 2.3.0 & Enterprise KGs",
            "• Cyber Threat Intel: MITRE ATT&CK STIX 2.1 (2,202 nodes, 20,565 edges in Neo4j AuraDB).\n• Indian Stock Market: NSE/BSE corporate holding trees (Tata, Reliance, HDFC, Infosys, SEBI).\n• Incredible India Tourism: Golden Triangle & Karnataka circuits via IRCTC Vande Bharat.\n• Live 2D/3D PyVis Topology DAGs rendered in real-time.",
            ACCENT_PURPLE
        ),
        (
            "3. Graph-A3J Engine",
            "Neuro-Symbolic Algorithm 1",
            "• Decouples semantic claim extraction from deterministic graph-path verification.\n• Computes Topological Hallucination Divergence (THD), Step Efficiency (SE), and S_composite.\n• Active database querying at 120.50 ms query latency with automated CI/CD gating (ALLOW vs BLOCK).",
            ACCENT_GREEN
        )
    ]

    card_width = Inches(3.64)
    card_height = Inches(4.8)
    card_top = Inches(1.9)

    for i, (title, subtitle, body, color) in enumerate(cards_data):
        card_left = Inches(0.8 + i * 4.0)
        shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card_left, card_top, card_width, card_height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = PANEL_BG
        shape.line.color.rgb = color
        shape.line.width = Pt(1.5)

        tb = slide1.shapes.add_textbox(card_left + Inches(0.2), card_top + Inches(0.2), card_width - Inches(0.4), card_height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        pt1 = tf.paragraphs[0]
        pt1.text = title
        pt1.font.bold = True
        pt1.font.size = Pt(16)
        pt1.font.color.rgb = color

        pt2 = tf.add_paragraph()
        pt2.text = subtitle
        pt2.font.bold = True
        pt2.font.size = Pt(12)
        pt2.font.color.rgb = TEXT_WHITE
        pt2.space_after = Pt(12)

        pt3 = tf.add_paragraph()
        pt3.text = body
        pt3.font.size = Pt(11)
        pt3.font.color.rgb = TEXT_MUTED
        pt3.line_spacing = 1.25


    # ==============================================================================
    # SLIDE 2: SCIENTIFIC RESULTS, CI/CD GATING & BUSINESS IMPACT
    # ==============================================================================
    slide2 = prs.slides.add_slide(blank_slide_layout)
    
    bg2 = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = BG_COLOR
    bg2.line.color.rgb = BG_COLOR

    # Header Box 2
    header_box2 = slide2.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
    tf2 = header_box2.text_frame
    tf2.word_wrap = True
    
    p2_1 = tf2.paragraphs[0]
    p2_1.text = "Empirical Benchmark Superiority, CI/CD Gating & Enterprise ROI"
    p2_1.font.bold = True
    p2_1.font.size = Pt(26)
    p2_1.font.color.rgb = TEXT_WHITE

    p2_2 = tf2.add_paragraph()
    p2_2.text = "Rigorous Live Verification (N = 1,000 Live Traces over Neo4j AuraDB STIX 2.1) | Production-Ready Governance"
    p2_2.font.size = Pt(13)
    p2_2.font.color.rgb = ACCENT_GREEN

    # Left Panel: Benchmark Table & McNemar Test
    left_panel = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    left_panel.fill.solid()
    left_panel.fill.fore_color.rgb = PANEL_BG
    left_panel.line.color.rgb = ACCENT_BLUE
    left_panel.line.width = Pt(1.5)

    tb_table = slide2.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.2), Inches(4.4))
    tft = tb_table.text_frame
    tft.word_wrap = True

    t1 = tft.paragraphs[0]
    t1.text = "📊 Live Empirical Benchmark (N=1,000)"
    t1.font.bold = True
    t1.font.size = Pt(16)
    t1.font.color.rgb = ACCENT_BLUE
    t1.space_after = Pt(8)

    table_rows = [
        "• ROC-AUC: Graph-A3J 0.9967 vs Baseline 0.7573 (+23.9%)",
        "• PR-AUC: 0.9980 | F1-Score: 0.9975 | Accuracy: 99.70%",
        "• False Negative Hallucinations: 0 missed (vs 351 baseline)",
        "• Statistical Significance: McNemar χ²(1) = 349.00 (p < 10⁻⁷⁷)",
        "• Live Cypher Query Latency: 120.50 ms per query",
        "• End-to-End P95 Latency: 641.18 ms (3.9x faster than LLM Judge)",
        "• Amortized Total Cost: $0.00042 / trace (8.3x cheaper)"
    ]
    for row in table_rows:
        pr = tft.add_paragraph()
        pr.text = row
        pr.font.size = Pt(11)
        pr.font.color.rgb = TEXT_WHITE
        pr.line_spacing = 1.3

    # Right Panel: CI/CD Gating & Customer Value
    right_panel = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.7), Inches(4.8))
    right_panel.fill.solid()
    right_panel.fill.fore_color.rgb = PANEL_BG
    right_panel.line.color.rgb = ACCENT_GREEN
    right_panel.line.width = Pt(1.5)

    tb_right = slide2.shapes.add_textbox(Inches(7.0), Inches(2.1), Inches(5.3), Inches(4.4))
    tfr = tb_right.text_frame
    tfr.word_wrap = True

    r1 = tfr.paragraphs[0]
    r1.text = "🛡️ CI/CD Safety Gating & Enterprise Impact"
    r1.font.bold = True
    r1.font.size = Pt(16)
    r1.font.color.rgb = ACCENT_GREEN
    r1.space_after = Pt(8)

    right_rows = [
        "1. Automated CI/CD Deployment Gates:",
        "   - Blocks rogue prompts in PRs before hitting production.",
        "   - Enforces THD ≤ 0.50 and Composite Score ≥ 0.85.",
        "   - Provides CISOs, CTOs & Risk teams complete fiduciary trust.",
        "",
        "2. Proven Global Customer Implementations:",
        "   - Menlo Security & Solenis LLC: Gemini Enterprise swarms.",
        "   - HSBC Bank (EMEA): Enterprise Knowledge Graph architectures.",
        "   - Box, Veritas & VaynerMedia: Strategic multi-agent advisory.",
        "",
        "3. Production Cloud Deployment:",
        "   - 1-Click Vertex AI Agent Engine (`adk deploy agent_engine`).",
        "   - Seamless integration with Gemini Enterprise & Agent Platform."
    ]
    for r in right_rows:
        pr = tfr.add_paragraph()
        pr.text = r
        pr.font.size = Pt(10.5)
        pr.font.color.rgb = TEXT_MUTED if r.startswith("   ") else TEXT_WHITE
        pr.font.bold = not r.startswith("   ") and len(r) > 0
        pr.line_spacing = 1.2

    output_pptx = "/Users/aniketagrawal/antigravity_workshop/EXECUTIVE_PRESENTATION_DECK.pptx"
    prs.save(output_pptx)
    print(f"✅ Executive Presentation Deck successfully generated: {output_pptx}")

if __name__ == "__main__":
    create_executive_deck()
