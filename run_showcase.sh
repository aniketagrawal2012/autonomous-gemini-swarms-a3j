#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${SCRIPT_DIR}/.venv_benchmark/bin/python3"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="/Users/aniketagrawal/antigravity_workshop/.venv_benchmark/bin/python3"
fi
lsof -ti :8000 | xargs kill -9 2>/dev/null || true
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH:-}"
echo "🚀 Launching Autonomous Gemini Enterprise Swarms Showcase on http://localhost:8000 ..."
exec "$PYTHON_BIN" "${SCRIPT_DIR}/app_showcase.py"
