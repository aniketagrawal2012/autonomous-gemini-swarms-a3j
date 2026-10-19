#!/usr/bin/env bash
# ==============================================================================
# Publish ADK Swarm to Google Cloud Gemini Enterprise & Agent Registry
# Target Project: aniket-personal | Registration Mode: ADK / A2A
# ==============================================================================
set -euo pipefail

PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-aniket-personal}"
APP_ID="${GEMINI_ENTERPRISE_APP_ID:-projects/${PROJECT_ID}/locations/global/collections/default_collection/engines/a3j-swarm-app}"

echo "=============================================================================="
echo "🚀 PUBLISHING AGENT TO GOOGLE CLOUD GEMINI ENTERPRISE (AGENT REGISTRY)"
echo "Project: $PROJECT_ID | App ID: $APP_ID"
echo "=============================================================================="

if command -v agents-cli &> /dev/null; then
    echo "📦 Registering agent via agents-cli..."
    agents-cli publish gemini-enterprise \
      --gemini-enterprise-app-id="$APP_ID" \
      --display-name="Global Executive Transit & Governance Swarm" \
      --description="Autonomous Agent-as-a-Judge (A3J) & GraphRAG Swarm on Google Cloud Vertex AI" \
      --tool-description="Provides verified executive logistics, corporate governance, and threat intelligence with zero hallucination." \
      --registration-type=adk \
      --metadata-file="deployment_metadata.json" || {
        echo "⚠️ Note: Ensure Gemini Enterprise App '$APP_ID' is created in Cloud Console."
    }
else
    echo "💡 agents-cli not found. Install via: uv tool install google-agents-cli"
    echo "Run manually after deployment:"
    echo "  agents-cli publish gemini-enterprise --gemini-enterprise-app-id='$APP_ID'"
fi
