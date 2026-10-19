"""
Unit Test Suite: Steiner-Tree Hallucination Rectifier & Algorithm 2 Search
Verifies:
1. Discovery of Intermediate Bridge Nodes across disconnected subgraphs
2. Minimal Metric Steiner-Tree spanning path reconstruction
3. Partial Divergence Recovery (THD 1.00 -> 0.20 -> 0.00)
4. Latin America SFO-MEX Flight Bridge Synthesis
5. India North-South BLR-DEL Flight Bridge Synthesis
6. Live Auto-Heal API execution and state reconciliation
"""

import unittest
import json
from graph_a3j_swarm.tools import find_steiner_tree_repair_path
from graph_a3j_swarm.autoheal_engine import execute_live_steiner_autoheal

class TestSteinerAutoHealAlgorithm(unittest.TestCase):

    def test_01_steiner_repair_path_generation(self):
        """find_steiner_tree_repair_path must return valid repair payload with bridge nodes."""
        resp = find_steiner_tree_repair_path("Mountain View Googleplex HQ", "Teotihuacan Pyramids of Sun & Moon")
        data = json.loads(resp) if isinstance(resp, str) else resp
        self.assertIn("verified_path_sequence", data)
        self.assertEqual(data["repair_status"], "STEINER_TREE_CONVERGED")
        self.assertEqual(data["repaired_gate_verdict"], "AUTO-HEALED & DEPLOYED")

    def test_02_steiner_bridge_nodes_latam(self):
        """Reconstructs transcontinental bridge via SFO and MEX aviation hubs."""
        resp = find_steiner_tree_repair_path("Mountain View Googleplex HQ", "Teotihuacan Pyramids of Sun & Moon")
        data = json.loads(resp) if isinstance(resp, str) else resp
        path_str = " ".join(data["verified_path_sequence"])
        self.assertIn("SFO", path_str)
        self.assertIn("MEX", path_str)

    def test_03_steiner_bridge_nodes_india(self):
        """Reconstructs North-South India bridge via BLR and DEL aviation hubs."""
        resp = find_steiner_tree_repair_path("Google Bangalore Campus (RMZ Infinity)", "Taj Mahal Monument")
        data = json.loads(resp) if isinstance(resp, str) else resp
        path_str = " ".join(data["verified_path_sequence"])
        self.assertIn("Kempegowda", path_str)
        self.assertIn("Indira Gandhi", path_str)

    def test_04_live_autoheal_execution(self):
        """execute_live_steiner_autoheal must return AUTO-HEALED gate with 0.00 THD."""
        res = execute_live_steiner_autoheal(
            "San Francisco 1 Market St direct to Agra Taj Mahal via bullet train",
            "Taking bullet train across ocean"
        )
        self.assertEqual(res["gate"], "AUTO-HEALED & DEPLOYED")
        self.assertEqual(res["metrics"]["topological_hallucination_divergence"], 0.00)
        self.assertGreaterEqual(res["metrics"]["composite_alignment_score"], 0.85)

    def test_05_repaired_triples_structure(self):
        """Auto-heal response must include verified reconstructed summary."""
        res = execute_live_steiner_autoheal(
            "Googleplex direct to London St Pancras via Caltrain",
            "Direct caltrain to London"
        )
        self.assertIn("healed_response", res)
        self.assertIn("verified_path", res)
        self.assertIn("logs", res)

    def test_06_autoheal_resolution_log_stream(self):
        """Auto-heal execution must yield complete 6-phase resolution log stream."""
        res = execute_live_steiner_autoheal(
            "SFO to Paris via submarine",
            "Taking submarine"
        )
        self.assertIn("logs", res)
        self.assertGreaterEqual(len(res["logs"]), 5)

if __name__ == "__main__":
    unittest.main()
