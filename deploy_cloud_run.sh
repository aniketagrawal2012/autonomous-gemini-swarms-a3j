#!/usr/bin/env bash
# ==============================================================================
# Deploy Google Cloud Vertex AI Enterprise Swarms & Graph-A3J Showcase to Cloud Run
# Target Project: aniket-personal | Region: us-central1 | Access: Public HTTPS
# ==============================================================================
set -euo pipefail

PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-aniket-personal}"
REGION="${GOOGLE_CLOUD_LOCATION:-us-central1}"
SERVICE_NAME="a3j-enterprise-showcase"

echo "=============================================================================="
echo "🚀 DEPLOYING AGENT-AS-A-JUDGE & GRAPHRAG SHOWCASE TO GOOGLE CLOUD RUN"
echo "Project: $PROJECT_ID | Region: $REGION | Service: $SERVICE_NAME"
echo "=============================================================================="

# 1. Enable required GCP services
echo "🔧 Verifying and enabling required Google Cloud APIs..."
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  aiplatform.googleapis.com \
  cloudbuild.googleapis.com \
  compute.googleapis.com \
  --project="$PROJECT_ID" --quiet

# 2. Resolve or Provision Build & Runtime Service Account
echo "🔑 Verifying Build & Runtime service accounts..."
PROJECT_NUM=$(gcloud projects describe "$PROJECT_ID" --format="value(projectNumber)")
COMPUTE_SA="${PROJECT_NUM}-compute@developer.gserviceaccount.com"

BUILD_ARGS=()
RUNTIME_ARGS=()

# Check if Compute SA exists (enabling compute.googleapis.com usually creates it)
if gcloud iam service-accounts describe "${COMPUTE_SA}" --project="$PROJECT_ID" &>/dev/null; then
    echo "✅ Found default Compute Engine service account: ${COMPUTE_SA}"
    ACTIVE_SA="${COMPUTE_SA}"
else
    echo "⚠️ Default compute service account not available. Creating dedicated service account..."
    DEDICATED_SA_NAME="a3j-showcase-runner"
    DEDICATED_SA="${DEDICATED_SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
    
    if ! gcloud iam service-accounts describe "${DEDICATED_SA}" --project="$PROJECT_ID" &>/dev/null; then
        gcloud iam service-accounts create "${DEDICATED_SA_NAME}" \
          --display-name="A3J Showcase Service Account" \
          --project="$PROJECT_ID" --quiet
        echo "⏳ Waiting 5s for IAM propagation..."
        sleep 5
    fi
    ACTIVE_SA="${DEDICATED_SA}"
    BUILD_ARGS+=(--build-service-account="projects/${PROJECT_ID}/serviceAccounts/${ACTIVE_SA}")
    RUNTIME_ARGS+=(--service-account="${ACTIVE_SA}")
fi

echo "🛡️ Granting required IAM permissions to ${ACTIVE_SA}..."
REQUIRED_ROLES=(
  "roles/run.builder"
  "roles/artifactregistry.writer"
  "roles/logging.logWriter"
  "roles/storage.admin"
  "roles/aiplatform.user"
)

for role in "${REQUIRED_ROLES[@]}"; do
  gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:${ACTIVE_SA}" \
    --role="$role" \
    --condition=None \
    --quiet &>/dev/null || true
done

# Allow Cloud Build & Cloud Run service agents to impersonate/actAs the service account
gcloud iam service-accounts add-iam-policy-binding "${ACTIVE_SA}" \
  --member="serviceAccount:${PROJECT_NUM}@cloudbuild.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser" \
  --project="$PROJECT_ID" --quiet &>/dev/null || true

gcloud iam service-accounts add-iam-policy-binding "${ACTIVE_SA}" \
  --member="serviceAccount:service-${PROJECT_NUM}@serverless-robot-prod.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser" \
  --project="$PROJECT_ID" --quiet &>/dev/null || true


# 3. Deploy from source
echo "📦 Building and deploying Cloud Run service..."
gcloud run deploy "$SERVICE_NAME" \
  --project="$PROJECT_ID" \
  --region="$REGION" \
  --source=. \
  --allow-unauthenticated \
  --memory=4Gi \
  --cpu=2 \
  --min-instances=1 \
  --max-instances=5 \
  --concurrency=20 \
  --timeout=300 \
  ${BUILD_ARGS[@]+"${BUILD_ARGS[@]}"} \
  ${RUNTIME_ARGS[@]+"${RUNTIME_ARGS[@]}"} \
  --set-env-vars="GOOGLE_GENAI_USE_VERTEXAI=true,GOOGLE_CLOUD_PROJECT=$PROJECT_ID,GOOGLE_CLOUD_LOCATION=$REGION,VERTEX_AI_MODEL=gemini-2.0-flash-001" \
  --quiet

# Ensure unauthenticated public access is granted
echo "🌐 Ensuring public invoker access..."
gcloud run services add-iam-policy-binding "$SERVICE_NAME" \
  --project="$PROJECT_ID" \
  --region="$REGION" \
  --member="allUsers" \
  --role="roles/run.invoker" \
  --quiet &>/dev/null || true

# 4. Retrieve and display public service URL
SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" --project="$PROJECT_ID" --region="$REGION" --format="value(status.url)")


echo "=============================================================================="
echo "✨ DEPLOYMENT COMPLETE!"
echo "🌐 Public Live Showcase URL: $SERVICE_URL"
echo "📱 Booth QR Code URL:        https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=$SERVICE_URL"
echo "=============================================================================="
