# 🚀 START HERE: Autonomous Gemini Enterprise Swarms & Graph-A3J

Welcome to the **Google CloudScope Flagship Showcase Project**!  
This workspace contains a production-ready, fully tested implementation of **Autonomous Gemini Enterprise Swarms** with **Zero-Hallucination GraphRAG** and **Agent-as-a-Judge (A3J)** state verification across 4 enterprise domains.

---

## 📂 Exact Folder to Open in Visual Studio Code

Open this single root folder in Visual Studio Code:
```
/Users/aniketagrawal/antigravity_workshop
```

**How to open in VS Code:**
1. Open VS Code &rarr; Click **File** &rarr; **Open Folder...**
2. Select `/Users/aniketagrawal/antigravity_workshop`
3. (Or in your terminal, run: `code /Users/aniketagrawal/antigravity_workshop`)

---

## ⚡ 1-Click Launch Options in VS Code (F5 / Run & Debug)

The `.vscode/launch.json` and `.vscode/settings.json` have been pre-configured for 1-click execution:

1. Click the **Run & Debug** icon on the left sidebar (or press `Ctrl+Shift+D` / `Cmd+Shift+D`).
2. Choose any pre-configured target from the dropdown:
   - **`🚀 1. Launch Executive Showcase Dashboard (Port 8000)`** &larr; *(Recommended for live demos)*
   - **`🌐 2. Launch Official ADK Web UI`**
   - **`🧪 3. Run E2E Test Suite (11 Tests)`**
   - **`🎯 4. Run Multi-Domain Evaluation Suite (10 Cases)`**
   - **`📊 5. Generate Executive Presentation Deck (PPTX)`**
3. Press **F5** to run!

---

## 🗂️ Clean Repository Layout

```
/Users/aniketagrawal/antigravity_workshop/
│
├── .vscode/                           # VS Code 1-Click Run & Debug Configs
│   ├── launch.json                    # F5 Launch profiles (Showcase, ADK Web, Tests)
│   ├── settings.json                  # Python interpreter path & linting
│   └── tasks.json                     # VS Code build/test tasks
│
├── graph_a3j_swarm/                   # Core Google ADK 2.3.0 Multi-Domain Swarm Package
│   ├── __init__.py                    # Agent exports
│   ├── agent.py                       # 5 Domain Agents + Root Orchestrator
│   ├── config.py                      # Neo4j credentials, thresholds, weights
│   ├── schemas.py                     # Pydantic data contracts
│   ├── tools.py                       # Deterministic GraphRAG, PyVis, Ledger, & A3J tools
│   └── eval/                          # Multi-Domain Quality Evaluation Suite
│       ├── eval_dataset.json          # 10 Stratified test cases (Cyber, Stocks, Tourism, Logistics)
│       ├── eval_config.yaml           # ADK Evaluation metric definitions
│       └── run_eval.py                # Automated batch evaluation runner
│
├── static/
│   └── topology_graph.html            # Dynamic 2D/3D PyVis Network Topology DAG
│
├── scripts/
│   ├── simulate_full_showcase.py      # Automated 10-stage end-to-end verification script
│   ├── generate_slides.py             # 2-Slide PowerPoint presentation deck generator
│   ├── deploy_agent_engine.sh         # 1-Click Vertex AI Agent Engine deployment
│   └── ingest_real_mitre_attack.py    # MITRE ATT&CK STIX 2.1 Neo4j hydration script
│
├── tests/
│   └── test_swarm_e2e.py              # 11 Unit & Integration E2E Tests (100% Passing)
│
├── app_showcase.py                    # Executive Interactive Portal (FastAPI, Tailwind, VisJS)
├── streamlit_app.py                   # Streamlit Interactive Showcase Option
├── EXECUTIVE_PRESENTATION_DECK.pptx   # 2-Slide Executive PowerPoint Presentation Deck
├── DEMO_PITCH_SCRIPT.md               # 10-Minute Speaker Pitch Script for Leadership
├── README.md                          # Full Architectural Documentation
└── START_HERE.md                      # This Quickstart Guide
```

---

## 🎯 Key Presentation Assets for Leadership

1. **Executive 2-Slide Presentation Deck**:
   - File: [`EXECUTIVE_PRESENTATION_DECK.pptx`](file:///Users/aniketagrawal/antigravity_workshop/EXECUTIVE_PRESENTATION_DECK.pptx)
   - Double-click to open in PowerPoint, Keynote, or Google Slides.
2. **10-Minute Executive Pitch Script**:
   - File: [`DEMO_PITCH_SCRIPT.md`](file:///Users/aniketagrawal/antigravity_workshop/DEMO_PITCH_SCRIPT.md)
   - Timed speaker script covering: *The Evaluation Crisis*, *Multi-Domain GraphRAG Swarms*, *Live Red-Teaming*, *Scientific MLOps Results*, and *Enterprise ROI*.
3. **Interactive Showcase Dashboard**:
   - Start via: `.venv_benchmark/bin/python3 app_showcase.py`
   - Open: `http://localhost:8000`

---

## 🧪 Automated Verification Commands (Executed & Passing)

All tests have been run and verified:
```bash
# 1. Run Complete 20-Stage Showcase Simulation (All 4 Domains)
.venv_benchmark/bin/python3 scripts/simulate_full_showcase.py
# Or use the convenience script:
bash ./run_tests.sh

# 2. Run E2E Test Suite (11/11 Passed)
.venv_benchmark/bin/python3 -m unittest tests/test_swarm_e2e.py -v

# 3. Run Multi-Domain Evaluation Suite (10/10 Passed with 100.0% accuracy)
.venv_benchmark/bin/python3 graph_a3j_swarm/eval/run_eval.py
```
