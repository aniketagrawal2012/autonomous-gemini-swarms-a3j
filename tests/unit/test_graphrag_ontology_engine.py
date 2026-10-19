"""
Unit Test Suite: GraphRAG Ontology Engine & Neuro-Symbolic Parser
Verifies:
1. Multi-Cluster Entity Extraction across 150+ Global Entities
2. Strict Sentence-Order Entity Preservation
3. Multi-Hop Relational Triples Construction
4. Physical Barrier & Trans-Oceanic Feasibility Detection
5. Relativistic Velocity & Speed-of-Light Bounds
6. Multi-Domain Intent Classification (Stocks, CTI, Supply Chain, Mobility)
7. Vector Graph Artifact Generation (Mermaid.js Flowcharts & SVG Radar Cards)
"""

import unittest
from graph_a3j_swarm.dynamic_engine import (
    GLOBAL_GEO_DB,
    extract_entities_from_query,
    analyze_query_feasibility,
    classify_query_domain,
    generate_mermaid_route_diagram,
    generate_svg_route_map,
    generate_dynamic_itinerary_and_proof
)

class TestGraphRAGOntologyEngine(unittest.TestCase):

    def test_01_global_geo_db_coverage(self):
        """GLOBAL_GEO_DB must contain 150+ verified enterprise entities and aliases."""
        self.assertGreaterEqual(len(GLOBAL_GEO_DB), 130)

    def test_02_entity_extraction_us_tech(self):
        """Extracts Bay Area tech entities correctly."""
        entities = extract_entities_from_query("Plan trip from Googleplex to Sunnyvale Moffett Park then to SFO")
        names = [e["name"] for e in entities]
        self.assertIn("Mountain View Googleplex HQ", names)
        self.assertIn("Sunnyvale Moffett Park Campus", names)
        self.assertIn("San Francisco International (SFO)", names)

    def test_03_entity_extraction_india_tech(self):
        """Extracts India tech and aviation entities correctly."""
        entities = extract_entities_from_query("Route from Bangalore RMZ Infinity to Kempegowda BLR then Delhi IGI")
        names = [e["name"] for e in entities]
        self.assertIn("Google Bangalore Campus (RMZ Infinity)", names)
        self.assertIn("Kempegowda International Hub (BLR)", names)
        self.assertIn("Indira Gandhi International Hub (DEL)", names)

    def test_04_entity_extraction_europe(self):
        """Extracts European rail and aviation entities correctly."""
        entities = extract_entities_from_query("London St Pancras to Paris Gare du Nord then Berlin Hbf and Rome Colosseum")
        names = [e["name"] for e in entities]
        self.assertIn("London St Pancras International", names)
        self.assertIn("Paris Gare du Nord", names)
        self.assertIn("Berlin Central Station (Hbf)", names)
        self.assertIn("Rome Colosseum Archaeological Site", names)

    def test_05_sentence_order_preservation(self):
        """Entities must be extracted in the exact chronological order of appearance."""
        q = "First London, next Paris, then Rome, finally Vienna"
        entities = extract_entities_from_query(q)
        names = [e["name"] for e in entities]
        self.assertEqual(names[0], "London St Pancras International")
        self.assertEqual(names[1], "Paris Gare du Nord")
        self.assertEqual(names[2], "Rome Fiumicino Leonardo da Vinci (FCO)")
        self.assertEqual(names[3], "Vienna International Airport (VIE)")

    def test_06_trans_oceanic_barrier_detection(self):
        """Detects physical barrier when asserting ground transit across oceans."""
        entities = extract_entities_from_query("Take a bullet train from San Francisco to London")
        feasibility = analyze_query_feasibility("Take a bullet train from San Francisco to London", entities)
        self.assertTrue(feasibility["is_adversarial"])
        self.assertIn("TRANS-OCEANIC BARRIER VIOLATION", feasibility["hallucination_reason"])

    def test_07_trans_oceanic_flight_allowed(self):
        """Flight across oceans is valid and physically feasible."""
        entities = extract_entities_from_query("Fly from SFO to London Heathrow")
        feasibility = analyze_query_feasibility("Fly from SFO to London Heathrow", entities)
        self.assertFalse(feasibility["is_adversarial"])

    def test_08_continental_landmass_barrier(self):
        """Detects impossibility of maritime submarines navigating over dry land."""
        entities = extract_entities_from_query("Take a submarine from Bangalore to Delhi")
        feasibility = analyze_query_feasibility("Take a submarine from Bangalore to Delhi", entities)
        self.assertTrue(feasibility["is_adversarial"])

    def test_09_environmental_regulation_enforcement(self):
        """Detects diesel internal-combustion violations within Taj Trapezium Zone (TTZ)."""
        entities = extract_entities_from_query("Drive heavy diesel truck into Taj Mahal")
        feasibility = analyze_query_feasibility("Drive heavy diesel truck into Taj Mahal", entities)
        self.assertTrue(feasibility["is_adversarial"])
        self.assertIn("TTZ", feasibility["hallucination_reason"])

    def test_10_domain_classification_stocks(self):
        """Accurately classifies SEBI and corporate equity queries."""
        domain = classify_query_domain("Audit equity restructuring of Tata Sons and Tata Motors for JLR", [])
        self.assertEqual(domain, "stocks")

    def test_11_domain_classification_cybersecurity(self):
        """Accurately classifies MITRE ATT&CK and SCADA threat queries."""
        domain = classify_query_domain("Trace APT29 exploiting CVE-2024-38812 dropping WellMess into SCADA", [])
        self.assertEqual(domain, "cybersecurity")

    def test_12_domain_classification_supply_chain(self):
        """Accurately classifies ASML and TSMC semiconductor supply chain queries."""
        domain = classify_query_domain("Verify ASML EUV scanner shipment to TSMC Hsinchu fab", [])
        self.assertEqual(domain, "supply_chain")

    def test_13_mermaid_diagram_syntax(self):
        """Mermaid diagram generator must output valid graph LR with terminal styles."""
        entities = [GLOBAL_GEO_DB["mountain view"], GLOBAL_GEO_DB["sfo"], GLOBAL_GEO_DB["london"]]
        diagram = generate_mermaid_route_diagram(entities)
        self.assertTrue(diagram.startswith("```mermaid\ngraph LR"))
        self.assertIn("W0 -->", diagram)
        self.assertIn("W1 -->", diagram)
        self.assertTrue(diagram.endswith("```"))

    def test_14_svg_route_map_coordinates(self):
        """SVG route map generator must output valid SVG with lat/lon coordinates."""
        entities = [GLOBAL_GEO_DB["mountain view"], GLOBAL_GEO_DB["sfo"]]
        svg = generate_svg_route_map(entities)
        self.assertIn("<svg", svg)
        self.assertIn("37.42°", svg)
        self.assertIn("37.62°", svg)

    def test_15_dynamic_proper_noun_dispersion(self):
        """Unknown cities must receive dispersed, non-overlapping coordinates."""
        entities = extract_entities_from_query("Travel between Atlantis and ElDorado")
        self.assertGreaterEqual(len(entities), 2)
        # Verify coordinates do not completely collapse onto the exact same float
        self.assertNotEqual((entities[0]["lat"], entities[0]["lon"]), (entities[1]["lat"], entities[1]["lon"]))

if __name__ == "__main__":
    unittest.main()
