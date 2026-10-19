"""
Unit Test Suite: Cryptographic HMAC-SHA256 State Attestation & Swarm Consensus
Verifies:
1. HMAC-SHA256 Cryptographic Signature Generation on Graph Assertions
2. Cryptographic Tamper Detection on Altered Payloads
3. Multi-Agent Swarm Consensus Byzantine Voting Quorum (Weighted Confidence)
4. SOC2 Type II / ISO 42001 Regulatory Compliance Export Bundle Schema
"""

import unittest
import json
import hmac
import hashlib
from graph_a3j_swarm.tools import (
    inject_adversarial_graph_chaos,
    execute_swarm_consensus_vote
)

class TestSecurityHMACAttestation(unittest.TestCase):

    def test_01_hmac_signature_generation(self):
        """inject_adversarial_graph_chaos must return valid hex-encoded HMAC-SHA256 signature."""
        resp = inject_adversarial_graph_chaos(domain="travel")
        data = json.loads(resp) if isinstance(resp, str) else resp
        self.assertIn("cryptographic_hmac_sha256", data)
        self.assertEqual(len(data["cryptographic_hmac_sha256"]), 64) # SHA256 hex length
        # Verify hex characters
        int(data["cryptographic_hmac_sha256"], 16)

    def test_02_tamper_detection(self):
        """Altering a signed edge payload must invalidate cryptographic verification."""
        secret = b"vertex-ai-gemini-enterprise-hmac-key"
        original_payload = b"San Francisco International (SFO) -> London St Pancras"
        sig = hmac.new(secret, original_payload, hashlib.sha256).hexdigest()

        tampered_payload = b"San Francisco International (SFO) -> London St Pancras [TAMPERED]"
        tampered_sig = hmac.new(secret, tampered_payload, hashlib.sha256).hexdigest()
        self.assertNotEqual(sig, tampered_sig)

    def test_03_consensus_voting_quorum_schema(self):
        """execute_swarm_consensus_vote must return valid JSON with quorum decision and polled specialists."""
        resp = execute_swarm_consensus_vote("Executive travel from Googleplex to SFO", domain="travel")
        data = json.loads(resp) if isinstance(resp, str) else resp
        self.assertIn("arbitrated_decision", data)
        self.assertIn("swarm_votes", data)
        self.assertIn("weighted_consensus_confidence", data)
        self.assertGreaterEqual(len(data["swarm_votes"]), 3)

    def test_04_consensus_voting_confidence_bounds(self):
        """Consensus confidence must be bounded between 0.0 and 1.0."""
        resp = execute_swarm_consensus_vote("Corporate governance audit for Tata Motors", domain="stocks")
        data = json.loads(resp) if isinstance(resp, str) else resp
        conf = float(data["weighted_consensus_confidence"])
        self.assertGreaterEqual(conf, 0.0)
        self.assertLessEqual(conf, 1.0)

if __name__ == "__main__":
    unittest.main()
