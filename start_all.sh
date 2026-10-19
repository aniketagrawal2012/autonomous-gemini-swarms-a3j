#!/usr/bin/env bash
# ==============================================================================
# Unified 1-Click Launcher for Google Cloud Vertex AI Enterprise Swarms Showcase
# Automatically cleans stale ports, boots ADK Web (:8001) and Mission Control (:8000)
# ==============================================================================
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${SCRIPT_DIR}/.venv_benchmark/bin/python3"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="/Users/aniketagrawal/antigravity_workshop/.venv_benchmark/bin/python3"
fi

export GOOGLE_GENAI_USE_VERTEXAI="true"
export GOOGLE_CLOUD_PROJECT="aniket-personal"
export GOOGLE_CLOUD_LOCATION="us-central1"
export VERTEX_AI_MODEL="gemini-2.0-flash-001"
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH:-}"

echo "=========================================================================="
echo "🚀 LAUNCHING GOOGLE CLOUD VERTEX AI ENTERPRISE SWARMS & A3J SHOWCASE"
echo "Project: aniket-personal | Region: us-central1 | Engine: Vertex AI ADK 2.3.0"
echo "=========================================================================="

# 0. Clean up any stale processes holding port 8000 or 8001
echo "🧹 Checking and clearing ports 8000 and 8001..."
lsof -ti :8000 -ti :8001 | xargs kill -9 2>/dev/null || true
sleep 0.5

# 1. Start Official Google ADK Web UI on Port 8001 pointing to single agent package
echo "🌐 Starting Official Google ADK Web UI on http://localhost:8001 ..."
"$PYTHON_BIN" -m google.adk.cli web --port 8001 --session_service_uri memory:// --artifact_service_uri "file://${SCRIPT_DIR}/artifacts" "${SCRIPT_DIR}/graph_a3j_swarm" > /tmp/adk_web.log 2>&1 &
ADK_PID=$!

# Trap Ctrl+C to clean up background ADK Web process
cleanup() {
    echo -e "\n🛑 Shutting down showcase servers..."
    kill $ADK_PID 2>/dev/null || true
    lsof -ti :8000 -ti :8001 | xargs kill -9 2>/dev/null || true
    exit 0
}
trap cleanup SIGINT SIGTERM EXIT

sleep 1.5

echo "✨ 1. ADK Web Dev Console:   👉 http://localhost:8001"
echo "✨ 2. Executive Mission UI:  👉 http://localhost:8000"
echo "--------------------------------------------------------------------------"
echo "💎 Starting Executive Showcase Dashboard on Port 8000..."
"$PYTHON_BIN" "${SCRIPT_DIR}/app_showcase.py"
