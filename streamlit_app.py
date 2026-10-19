"""
Streamlit Interactive Studio for Autonomous Gemini Enterprise Swarms & Graph-A3J.
Run with: streamlit run streamlit_app.py
"""

import os
import sys
import json
import streamlit as st
import streamlit.components.v1 as components

# Add project root
sys.path.insert(0, "/Users/aniketagrawal/antigravity_workshop")

from graph_a3j_swarm.agent import root_agent
from graph_a3j_swarm.tools import (
    query_threat_graph,
    query_indian_stocks_graph,
    query_indian_tourism_graph,
    visualize_attack_graph,
    verify_ledger_integrity,
    execute_a3j_topological_audit,
    generate_telemetry_plots
)

st.set_page_config(
    page_title="Autonomous Gemini Enterprise Swarms | Graph-A3J",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for glassmorphic styling
st.markdown("""
<style>
    .main { background-color: #090d16; color: #f8fafc; }
    .stMetric { background-color: #1e293b; padding: 10px 15px; border-radius: 10px; border: 1px solid #334155; }
    .stButton>button { background: linear-gradient(90deg, #0284c7, #2563eb); color: white; font-weight: bold; border-radius: 10px; border: none; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ Autonomous Gemini Enterprise Swarms: Zero-Hallucination GraphRAG & A3J")
st.caption("Official Google CloudScope Showcase | Multi-Domain State Verification Engine | ADK 2.3.0")

# Sidebar Configuration
st.sidebar.header("🌐 Enterprise Domain")
domain = st.sidebar.selectbox(
    "Select Knowledge Domain",
    ["1. Cybersecurity CTI (MITRE ATT&CK)", "2. Indian Stock Market (NSE/BSE)", "3. Incredible India Tourism", "4. Global Supply Chain Logistics"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Benchmark Quick Stats")
st.sidebar.markdown("**Graph-A3J ROC-AUC**: `0.9967`")
st.sidebar.markdown("**Context Baseline**: `0.7573`")
st.sidebar.markdown("**McNemar χ²**: `349.00 (p < 10⁻⁷⁷)`")
st.sidebar.markdown("**DB Query Latency**: `120.50 ms`")
st.sidebar.markdown("**Cost per trace**: `$0.00042`")

# Presets by Domain
preset_map = {
    "1. Cybersecurity CTI (MITRE ATT&CK)": {
        "prompt": "What malware family does APT29 use to target the Pharmaceuticals sector?",
        "sample_response": "APT29 uses WellMess malware to establish persistent access and target the Pharmaceuticals sector.",
        "root_node": "APT29"
    },
    "2. Indian Stock Market (NSE/BSE)": {
        "prompt": "What major public subsidiaries are controlled by Tata Sons?",
        "sample_response": "Tata Sons controls Tata Consultancy Services and Tata Motors, and Tata Motors owns Jaguar Land Rover.",
        "root_node": "Tata Sons"
    },
    "3. Incredible India Tourism": {
        "prompt": "Plan a heritage travel circuit from Delhi to Agra and Jaipur via high-speed transit.",
        "sample_response": "Delhi connects to Vande Bharat Express and Agra, where the Taj Mahal is managed by Archaeological Survey of India.",
        "root_node": "Taj Mahal"
    },
    "4. Global Supply Chain Logistics": {
        "prompt": "Reserve 4,000 kg freight capacity on carrier CARRIER_01 from Mumbai to Bengaluru.",
        "sample_response": "Carrier 01 successfully committed 4,000 kg freight capacity with ₹28,000 tariff complying with minimum price floors.",
        "root_node": "CARRIER_01"
    }
}

selected_preset = preset_map[domain]

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💬 Swarm Query & Reasoning")
    user_prompt = st.text_area("User Intent / Query", value=selected_preset["prompt"], height=90)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🚀 Execute GraphRAG Query"):
            with st.spinner("Orchestrating Swarms & querying Knowledge Graph..."):
                if "Cybersecurity" in domain:
                    res_raw = query_threat_graph(user_prompt)
                elif "Stock" in domain:
                    res_raw = query_indian_stocks_graph(user_prompt)
                elif "Tourism" in domain:
                    res_raw = query_indian_tourism_graph(user_prompt)
                else:
                    res_raw = verify_ledger_integrity()
                st.session_state["graph_res"] = json.loads(res_raw)

    with col_btn2:
        if st.button("👁️ Render 2D/3D Topology"):
            with st.spinner("Generating PyVis Network Graph..."):
                vis_raw = visualize_attack_graph(selected_preset["root_node"], max_depth=2)
                st.session_state["vis_res"] = json.loads(vis_raw)

    if "graph_res" in st.session_state:
        st.markdown("#### 🔗 Ground-Truth Graph Sub-State:")
        st.json(st.session_state["graph_res"])

    st.markdown("---")
    st.subheader("🕵️ Glass-Box A3J Auditor")
    agent_output = st.text_area("Agent Response to Audit (Test Red-Teaming Here)", value=selected_preset["sample_response"], height=100)
    
    if st.button("⚖️ Run Deterministic A3J State Audit"):
        with st.spinner("Auditing DAG against database state (120ms)..."):
            scorecard_raw = execute_a3j_topological_audit(agent_output)
            st.session_state["scorecard"] = json.loads(scorecard_raw)

with col2:
    st.subheader("🌐 Live Network Topology DAG")
    html_path = "/Users/aniketagrawal/antigravity_workshop/static/topology_graph.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=450, scrolling=False)
    else:
        st.info("Click 'Render 2D/3D Topology' to load the interactive PyVis graph canvas.")

    if "scorecard" in st.session_state:
        sc = st.session_state["scorecard"]
        gate = sc["recommended_cicd_gate_action"]
        
        st.markdown("---")
        st.subheader("🛡️ A3J CI/CD Scorecard")
        if gate == "ALLOW_DEPLOYMENT":
            st.success(f"### ✅ CI/CD GATE: {gate}")
        else:
            st.error(f"### 🛑 CI/CD GATE: {gate}")

        st.info(sc["isolated_audit_justification"])

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("THD Penalty", f"{sc['topological_hallucination_divergence']:.2f}")
        m2.metric("Step Efficiency", f"{sc['step_efficiency']:.2f}")
        m3.metric("State Accuracy", f"{sc['state_verification_accuracy']:.2f}")
        m4.metric("S_composite", f"{sc['composite_alignment_score']:.2f}")

st.markdown("---")
st.subheader("📈 Empirical MLOps Telemetry & Research Artifacts (N=1,000 Live Traces)")
c_img1, c_img2 = st.columns(2)
with c_img1:
    if os.path.exists("/Users/aniketagrawal/antigravity_workshop/roc_curves.png"):
        st.image("/Users/aniketagrawal/antigravity_workshop/roc_curves.png", caption="ROC Curve: Graph-A3J (0.9967) vs Context Baseline (0.7573)")
with c_img2:
    if os.path.exists("/Users/aniketagrawal/antigravity_workshop/thd_by_stratum.png"):
        st.image("/Users/aniketagrawal/antigravity_workshop/thd_by_stratum.png", caption="Average THD Penalty by Stratum (Compliant: 0.00 | Hallucinations: 1.00)")
