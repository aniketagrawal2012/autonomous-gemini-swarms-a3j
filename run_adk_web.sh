#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${SCRIPT_DIR}/.venv_benchmark/bin/python3"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="/Users/aniketagrawal/antigravity_workshop/.venv_benchmark/bin/python3"
fi

lsof -ti :8001 | xargs kill -9 2>/dev/null || true

# Google Cloud Vertex AI SDK Environment (Zero API Key Reliance)
export GOOGLE_GENAI_USE_VERTEXAI="true"
export GOOGLE_CLOUD_PROJECT="aniket-personal"
export GOOGLE_CLOUD_LOCATION="us-central1"
export VERTEX_AI_MODEL="gemini-2.0-flash-001"
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH:-}"

unset GOOGLE_API_KEY
unset GEMINI_API_KEY

echo "🌐 Starting Official Google ADK Web UI on Vertex AI Agent Engine (http://localhost:8001) ..."
exec "$PYTHON_BIN" -m google.adk.cli web --port 8001 --session_service_uri memory:// --artifact_service_uri "file://${SCRIPT_DIR}/artifacts" "${SCRIPT_DIR}/graph_a3j_swarm"
