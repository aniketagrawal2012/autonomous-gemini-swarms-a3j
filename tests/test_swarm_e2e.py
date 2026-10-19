"""
Comprehensive Multi-Domain E2E Test Suite for Autonomous Gemini Enterprise Swarms & Graph-A3J.
"""

import unittest
import json
import os
import sys

# Add project root
sys.path.insert(0, "/Users/aniketagrawal/antigravity_workshop")

from graph_a3j_swarm.agent import (
    root_agent,
    cyber_threat_agent,
    indian_stock_agent,
    indian_tourism_agent,
    supply_chain_agent,
    a3j_judge_agent
)
from graph_a3j_swarm.tools import (
    query_threat_graph,
    query_indian_stocks_graph,
    query_indian_tourism_graph,
    visualize_attack_graph,
    verify_ledger_integrity,
    execute_a3j_topological_audit,
    generate_telemetry_plots
)
from graph_a3j_swarm.schemas import JudgeOutputSchema


class TestMultiDomainGraphA3JSwarmE2E(unittest.TestCase):

    def test_multi_domain_agent_declarations(self):
        """Verify all ADK agent declarations and tool bindings."""
        self.assertEqual(root_agent.name, "AutonomousEnterpriseSwarm")
        self.assertEqual(cyber_threat_agent.name, "CyberThreatIntelAgent")
        self.assertEqual(indian_stock_agent.name, "IndianStockMarketAgent")
        self.assertEqual(indian_tourism_agent.name, "IndianTourismAgent")
        self.assertEqual(supply_chain_agent.name, "LogisticsSupplyChainAgent")
        self.assertEqual(a3j_judge_agent.name, "AgentAsAJudgeAuditor")
        self.assertGreaterEqual(len(root_agent.sub_agents), 6)

    def test_cti_graphrag_query_tool(self):
        """Verify CTI GraphRAG query returns structured facts."""
        result_json = query_threat_graph("What malware is used by APT29?")
        data = json.loads(result_json)
        self.assertEqual(data["status"], "SUCCESS")
        self.assertIn("verified_subgraph_facts", data)
        self.assertGreater(len(data["verified_subgraph_facts"]), 0)

    def test_indian_stocks_graphrag_tool(self):
        """Verify Indian Stock Market GraphRAG query returns corporate hierarchy."""
        result_json = query_indian_stocks_graph("Tata Group corporate structure")
        data = json.loads(result_json)
        self.assertEqual(data["status"], "SUCCESS")
        self.assertIn("Tata Sons", str(data["verified_subgraph_facts"]))

    def test_indian_tourism_graphrag_tool(self):
        """Verify Incredible India Tourism GraphRAG query returns travel circuits."""
        result_json = query_indian_tourism_graph("Golden Triangle Delhi Agra Jaipur")
        data = json.loads(result_json)
        self.assertEqual(data["status"], "SUCCESS")
        self.assertIn("Taj Mahal", str(data["verified_subgraph_facts"]))

    def test_pyvis_multi_domain_visualization(self):
        """Verify interactive PyVis HTML file generation for multi-domain entities."""
        r1 = json.loads(visualize_attack_graph("APT29", 2))
        self.assertEqual(r1["status"], "SUCCESS")
        self.assertTrue(os.path.exists(r1["visualization_file"]))

        r2 = json.loads(visualize_attack_graph("Tata Sons", 2))
        self.assertEqual(r2["status"], "SUCCESS")

        r3 = json.loads(visualize_attack_graph("Taj Mahal", 2))
        self.assertEqual(r3["status"], "SUCCESS")

    def test_a3j_compliant_stock_audit(self):
        """Verify A3J passes compliant Indian stock market claims."""
        response = "Tata Sons controls Tata Consultancy Services and Tata Motors."
        scorecard = JudgeOutputSchema(**json.loads(execute_a3j_topological_audit(response)))
        self.assertEqual(scorecard.recommended_cicd_gate_action, "ALLOW_DEPLOYMENT")
        self.assertEqual(scorecard.topological_hallucination_divergence, 0.0)

    def test_a3j_stock_cross_holding_fraud_blocked(self):
        """Verify A3J catches fabricated conglomerate cross-holding fraud."""
        response = "Reliance controls Tata Sons and owns Tata Motors."
        scorecard = JudgeOutputSchema(**json.loads(execute_a3j_topological_audit(response)))
        self.assertEqual(scorecard.recommended_cicd_gate_action, "TERMINATE_AND_BLOCK")
        self.assertEqual(scorecard.topological_hallucination_divergence, 1.0)

    def test_a3j_compliant_tourism_audit(self):
        """Verify A3J passes compliant tourism transit claims."""
        response = "Delhi connects to Vande Bharat Express and Agra."
        scorecard = JudgeOutputSchema(**json.loads(execute_a3j_topological_audit(response)))
        self.assertEqual(scorecard.recommended_cicd_gate_action, "ALLOW_DEPLOYMENT")
        self.assertEqual(scorecard.topological_hallucination_divergence, 0.0)

    def test_a3j_fabricated_tourism_transit_blocked(self):
        """Verify A3J blocks fabricated monorail connections between distant monuments."""
        response = "Taj Mahal connects to Virupaksha Temple via direct local monorail transit."
        scorecard = JudgeOutputSchema(**json.loads(execute_a3j_topological_audit(response)))
        self.assertEqual(scorecard.recommended_cicd_gate_action, "TERMINATE_AND_BLOCK")
        self.assertEqual(scorecard.topological_hallucination_divergence, 1.0)

    def test_a3j_cve_semantic_hallucination_blocked(self):
        """Verify A3J catches fabricated CTI relationship verbs and blocks deployment."""
        response = "Sandworm Team mitigates NotPetya through automated patching."
        scorecard = JudgeOutputSchema(**json.loads(execute_a3j_topological_audit(response)))
        self.assertEqual(scorecard.recommended_cicd_gate_action, "TERMINATE_AND_BLOCK")
        self.assertEqual(scorecard.topological_hallucination_divergence, 1.0)

    def test_telemetry_generation(self):
        """Verify generation of ROC curve and THD Stratum charts."""
        result_json = generate_telemetry_plots()
        data = json.loads(result_json)
        self.assertEqual(data["status"], "SUCCESS")
        self.assertAlmostEqual(data["graph_a3j_roc_auc"], 0.9967, places=2)


if __name__ == "__main__":
    unittest.main()
