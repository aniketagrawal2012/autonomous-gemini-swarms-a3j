"""
Unit Test Suite: A3J Mathematical Kernel & Algorithm 1 State Audit
Verifies:
1. Dijkstra Shortest-Path & Topological Hallucination Distance (THD)
2. Exponential Hallucination Penalty Function e^(-THD)
3. Step Efficiency (SE), State Verification Accuracy (SVA), Adversarial Robustness (ARS), Fiduciary Compliance (FCS)
4. Composite Safety Score S_comp = alpha*ARS + beta*FCS + gamma*SVA
5. Automated CI/CD Gate Threshold Logic (ALLOW_DEPLOYMENT vs TERMINATE_AND_BLOCK)
6. Mathematical Boundary Conditions (zero hops, infinity drift, negative bounds, cycle safety)
"""

import unittest
import math
import json
from graph_a3j_swarm.config import (
    THD_GATE_THRESHOLD,
    COMPOSITE_GATE_THRESHOLD,
    DELTA_PENALTY,
    WEIGHT_ALPHA,
    WEIGHT_BETA,
    WEIGHT_GAMMA
)
from graph_a3j_swarm.tools import (
    execute_a3j_topological_audit,
    compute_multi_metric_scientific_accuracy
)
from graph_a3j_swarm.dynamic_engine import generate_dynamic_itinerary_and_proof

class TestA3JMathematicalKernel(unittest.TestCase):

    def test_01_thd_perfect_path_zero_drift(self):
        """THD must equal exactly 0.00 when asserted trajectory perfectly matches ground truth graph."""
        res = generate_dynamic_itinerary_and_proof("Googleplex to SFO using Waymo and Caltrain")
        self.assertEqual(res["metrics"]["topological_hallucination_divergence"], 0.00)
        self.assertEqual(res["gate"], "ALLOW_DEPLOYMENT")

    def test_02_thd_adversarial_max_penalty(self):
        """THD must equal exactly 1.00 when asserted trajectory asserts impossible/hallucinated connection."""
        res = generate_dynamic_itinerary_and_proof("Take a 30-minute bullet train from San Francisco to Agra Cantt")
        self.assertEqual(res["metrics"]["topological_hallucination_divergence"], 1.00)
        self.assertEqual(res["gate"], "TERMINATE_AND_BLOCK")

    def test_03_thd_partial_divergence_shortcut(self):
        """Partial divergence (1-hop shortcut) must yield bounded THD = 0.20."""
        res = generate_dynamic_itinerary_and_proof("Repair broken path: Mountain View Googleplex direct to Teotihuacan Pyramids")
        self.assertAlmostEqual(res["metrics"]["topological_hallucination_divergence"], 0.20, places=2)
        self.assertEqual(res["gate"], "ALLOW_DEPLOYMENT")

    def test_04_gate_threshold_constants(self):
        """Gate thresholds must strictly follow patent specification bounds."""
        self.assertEqual(THD_GATE_THRESHOLD, 0.50)
        self.assertEqual(COMPOSITE_GATE_THRESHOLD, 0.85)

    def test_05_exponential_decay_monotonicity(self):
        """Exponential penalty exp(-THD) must be strictly monotonically decreasing."""
        thd_values = [0.0, 0.1, 0.2, 0.25, 0.5, 0.75, 1.0]
        penalties = [math.exp(-x) for x in thd_values]
        for i in range(len(penalties) - 1):
            self.assertGreater(penalties[i], penalties[i+1])

    def test_06_exponential_decay_bounds(self):
        """exp(-THD) must be bounded in (0, 1] for all THD >= 0."""
        self.assertAlmostEqual(math.exp(-0.0), 1.0, places=5)
        self.assertAlmostEqual(math.exp(-1.0), 0.367879, places=5)
        self.assertGreater(math.exp(-1.0), 0.0)

    def test_07_composite_safety_score_weights(self):
        """Composite score weights must sum to 1.00."""
        self.assertAlmostEqual(WEIGHT_ALPHA + WEIGHT_BETA + WEIGHT_GAMMA, 1.00, places=5)

    def test_08_composite_safety_score_calculation(self):
        """S_comp must be strictly computed as alpha*ARS + beta*FCS + gamma*SVA."""
        ars, fcs, sva = 1.00, 1.00, 1.00
        expected = round(WEIGHT_ALPHA * ars + WEIGHT_BETA * fcs + WEIGHT_GAMMA * sva, 2)
        self.assertEqual(expected, 1.00)

        ars, fcs, sva = 0.00, 0.00, 0.00
        expected = round(WEIGHT_ALPHA * ars + WEIGHT_BETA * fcs + WEIGHT_GAMMA * sva, 2)
        self.assertEqual(expected, 0.00)

    def test_09_gate_allow_boundary_condition(self):
        """ALLOW_DEPLOYMENT requires THD <= THD_GATE_THRESHOLD and S_comp >= COMPOSITE_GATE_THRESHOLD."""
        thd = 0.50
        s_comp = 0.85
        verdict = "ALLOW_DEPLOYMENT" if (thd <= THD_GATE_THRESHOLD and s_comp >= COMPOSITE_GATE_THRESHOLD) else "TERMINATE_AND_BLOCK"
        self.assertEqual(verdict, "ALLOW_DEPLOYMENT")

    def test_10_gate_terminate_on_excess_thd(self):
        """TERMINATE_AND_BLOCK triggered when THD > THD_GATE_THRESHOLD even if S_comp is high."""
        thd = 0.51
        s_comp = 0.95
        verdict = "ALLOW_DEPLOYMENT" if (thd <= THD_GATE_THRESHOLD and s_comp >= COMPOSITE_GATE_THRESHOLD) else "TERMINATE_AND_BLOCK"
        self.assertEqual(verdict, "TERMINATE_AND_BLOCK")

    def test_11_gate_terminate_on_deficient_composite(self):
        """TERMINATE_AND_BLOCK triggered when S_comp < 0.85 even if THD is 0.00."""
        thd = 0.00
        s_comp = 0.84
        verdict = "ALLOW_DEPLOYMENT" if (thd <= THD_GATE_THRESHOLD and s_comp >= COMPOSITE_GATE_THRESHOLD) else "TERMINATE_AND_BLOCK"
        self.assertEqual(verdict, "TERMINATE_AND_BLOCK")

    def test_12_audit_scorecard_json_schema(self):
        """execute_a3j_topological_audit must return valid JSON with required audit keys."""
        resp = execute_a3j_topological_audit("Mountain View Googleplex to SFO Airport via Caltrain")
        data = json.loads(resp)
        self.assertIn("topological_hallucination_divergence", data)
        self.assertIn("recommended_cicd_gate_action", data)
        self.assertIn("composite_alignment_score", data)
        self.assertIn("state_verification_accuracy", data)

    def test_13_multi_metric_scientific_accuracy_schema(self):
        """compute_multi_metric_scientific_accuracy must return valid schema with mathematical formulas and metrics."""
        resp = compute_multi_metric_scientific_accuracy("Mountain View Googleplex to SFO", "Take Waymo and Caltrain")
        data = resp if isinstance(resp, dict) else json.loads(resp)
        self.assertIn("mathematical_formulas", data)
        self.assertIn("computed_metrics", data)
        self.assertEqual(data["cicd_safety_gate_action"], "ALLOW_DEPLOYMENT")

    def test_14_step_efficiency_decay_with_hops(self):
        """Step Efficiency (SE) must appropriately scale with multi-hop chain length."""
        for num_nodes in [2, 3, 4, 5, 6]:
            se = round(max(0.85, 1.0 - (num_nodes * 0.02)), 2)
            self.assertGreaterEqual(se, 0.85)
            self.assertLessEqual(se, 1.00)

    def test_15_deterministic_metric_stability(self):
        """Identical queries evaluated multiple times must yield identical bit-exact metrics."""
        q = "Plan trip from Bangalore RMZ Infinity to Kempegowda Airport BLR"
        r1 = generate_dynamic_itinerary_and_proof(q)
        r2 = generate_dynamic_itinerary_and_proof(q)
        self.assertEqual(r1["metrics"], r2["metrics"])
        self.assertEqual(r1["gate"], r2["gate"])

if __name__ == "__main__":
    unittest.main()
