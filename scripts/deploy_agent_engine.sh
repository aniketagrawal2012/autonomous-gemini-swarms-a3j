#!/usr/bin/env bash
# ==============================================================================
# Vertex AI Agent Engine Deployment Script
# Autonomous Gemini Enterprise Swarms: Zero-Hallucination GraphRAG & Graph-A3J
# ==============================================================================

set -euo pipefail

echo "======================================================================"
echo "🚀 Deploying Autonomous Gemini Enterprise Swarm to Vertex AI Agent Engine"
echo "======================================================================"

PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-your-project-id}"
REGION="${GOOGLE_CLOUD_LOCATION:-us-central1}"
DISPLAY_NAME="Autonomous-Gemini-Enterprise-Swarm-A3J"
DESCRIPTION="Zero-Hallucination GraphRAG with Agent-as-a-Judge (A3J) State Verification"

echo "📋 Configuration:"
echo "   - Project ID    : ${PROJECT_ID}"
echo "   - Region        : ${REGION}"
echo "   - Display Name  : ${DISPLAY_NAME}"
echo "   - ADK Package   : graph_a3j_swarm"
echo ""

# Verify Python Environment
PYTHON_BIN="/Users/aniketagrawal/antigravity_workshop/.venv_benchmark/bin/python3"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="python3"
fi

# Execute ADK Agent Engine Deployment
echo "📦 Packaging ADK Swarm & resolving pickling dependencies..."
$PYTHON_BIN -m google.adk.cli deploy agent_engine \
    --project "${PROJECT_ID}" \
    --region "${REGION}" \
    --display_name "${DISPLAY_NAME}" \
    --description "${DESCRIPTION}" \
    --adk_version "2.3.0" \
    --otel_to_cloud \
    graph_a3j_swarm

echo ""
echo "======================================================================"
echo "✅ DEPLOYMENT INITIATED SUCCESSFULLY!"
echo "   To connect via Client SDK:"
echo "   from vertexai.preview import reasoning_engines"
echo "   agent = reasoning_engines.ReasoningEngine('projects/${PROJECT_ID}/locations/${REGION}/reasoningEngines/<ID>')"
echo "   response = agent.query(question='What malware does APT29 use?')"
echo "======================================================================"
