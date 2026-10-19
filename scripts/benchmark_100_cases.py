"""
Automated 100-Case Evaluation & Scientific Benchmark Suite for Graph-A3J Swarm.
Stratified across 4 core domains with zero mocking and deterministic neuro-symbolic verification:
- 30 Valid Global Tourism & Heritage Circuits (Bay Area, India Tech, Golden Triangle, Transcontinental)
- 25 Adversarial / Physically Impossible Routes (Trans-oceanic barriers, velocity bounds, municipal tram errors)
- 15 Corporate Governance & SEBI Forensics (Promoter group autonomy vs circular fraud & unregistered entities)
- 15 Cyber-Physical SCADA Grid Warfare (Zero-trust bastions & MITRE M1040 vs Sandworm C2 & predicate inversions)
- 10 Semiconductor Supply Chain & ACID Logistics (ASML/TSMC dispatch vs flight hold capacity overflow)
- 5 Multi-Modal Edge Cases & Partial Divergences
"""

import os
import sys
import json
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from graph_a3j_swarm.tools import compute_multi_metric_scientific_accuracy, execute_a3j_topological_audit
from graph_a3j_swarm.schemas import JudgeOutputSchema
from graph_a3j_swarm.dynamic_engine import generate_dynamic_itinerary_and_proof
from graph_a3j_swarm.agent import root_agent

TEST_CASES = [
    # =========================================================================
    # 1. VALID TOURISM & HERITAGE CIRCUITS (30 Cases) -> ALLOW_DEPLOYMENT, THD=0.0
    # =========================================================================
    {
        "id": 1,
        "name": "Bay Area: Googleplex to SFO via Waymo",
        "domain": "tourism",
        "query": "Plan an executive trip from Googleplex to SFO using Waymo autonomous fleet.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 2,
        "name": "Bay Area: Mountain View to SF 1 Market via Caltrain",
        "domain": "tourism",
        "query": "Synthesize commute from Mountain View Googleplex to Google San Francisco 1 Market St via Caltrain Bullet EMU.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 3,
        "name": "Bay Area: Sunnyvale Moffett Park to SFO Airport",
        "domain": "tourism",
        "query": "Route executive transit from Sunnyvale Moffett Park Campus to San Francisco International SFO Airport.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 4,
        "name": "Bay Area: SF Transbay Terminal to 1 Market St Walk",
        "domain": "tourism",
        "query": "Short pedestrian link from San Francisco Transbay Terminal to Google San Francisco 1 Market St.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 5,
        "name": "Bay Area: Googleplex to Sunnyvale Moffett via Waymo EV",
        "domain": "tourism",
        "query": "Campus shuttle from Mountain View Googleplex HQ to Sunnyvale Moffett Park Campus via Autonomous Waymo EV.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 6,
        "name": "Bay Area: Palo Alto to San Francisco via Caltrain",
        "domain": "tourism",
        "query": "Executive transit from Palo Alto Caltrain Station to San Francisco Transbay Terminal.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 7,
        "name": "Bay Area: San Jose SJC to Mountain View Googleplex",
        "domain": "tourism",
        "query": "Arrive at San Jose Mineta SJC and take Waymo autonomous shuttle to Googleplex HQ.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 8,
        "name": "India Tech: Bangalore RMZ to Kempegowda BLR Airport",
        "domain": "tourism",
        "query": "Synthesize transit from Google Bangalore RMZ Infinity to Kempegowda International Airport BLR via airport express shuttle.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 9,
        "name": "India Tech: Bangalore RMZ to Bagmane Capital Shuttle",
        "domain": "tourism",
        "query": "Intercampus shuttle connecting Google Bangalore RMZ Infinity to Google Bangalore Bagmane Capital.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 10,
        "name": "India Tech: Delhi IGI Airport to NDLS Central via Express Metro",
        "domain": "tourism",
        "query": "Transit from Indira Gandhi International Hub DEL to New Delhi Central NDLS via Airport Express Metro.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 11,
        "name": "India Tech: Delhi IGI to Google Gurgaon Signature Towers",
        "domain": "tourism",
        "query": "Route from Indira Gandhi International Airport DEL to Google Gurgaon Signature Towers via Cyber City Rapid Metro.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 12,
        "name": "India Tech: Gurgaon Signature Towers to One Horizon Center",
        "domain": "tourism",
        "query": "Executive shuttle between Google Gurgaon Signature Towers and Google Gurgaon One Horizon Center.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 13,
        "name": "India Tech: BLR Kempegowda to DEL Indira Gandhi Domestic Flight",
        "domain": "tourism",
        "query": "Commercial aviation flight corridor connecting Kempegowda International Hub BLR to Indira Gandhi International Hub DEL.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 14,
        "name": "Heritage: New Delhi Central to Agra Cantt via Vande Bharat",
        "domain": "tourism",
        "query": "High speed rail journey from New Delhi Central NDLS to Agra Cantt AGC on IRCTC Vande Bharat Express Train 20172.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 15,
        "name": "Heritage: Agra Cantt to Taj Mahal TTZ Eco Buffer",
        "domain": "tourism",
        "query": "Electric zero emission battery cart from Agra Cantt AGC to Taj Mahal Monument under TTZ Authority regulations.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 16,
        "name": "Heritage: Agra Cantt to Jaipur Pink City Gateway Expressway",
        "domain": "tourism",
        "query": "Expressway EV executive coach linking Agra Cantt Terminal AGC to Jaipur Pink City Gateway.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 17,
        "name": "Heritage: Jaipur Pink City to Amer Fort & Observatory",
        "domain": "tourism",
        "query": "Heritage tour connecting Jaipur Pink City Gateway to Amer Fort & Observatory UNESCO site.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 18,
        "name": "Heritage: Jaipur to Hawa Mahal Palace of Winds",
        "domain": "tourism",
        "query": "Visit Hawa Mahal Palace of Winds from Jaipur Pink City Gateway under ASI preservation rules.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 19,
        "name": "Heritage: Jaipur Airport to Kempegowda Bangalore Flight",
        "domain": "tourism",
        "query": "Domestic air corridor flight from Jaipur International Airport JAI to Kempegowda International Hub BLR.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 20,
        "name": "LATAM: SFO to Mexico City Benito Juarez International Flight",
        "domain": "tourism",
        "query": "Direct international commercial flight corridor from San Francisco International SFO to Benito Juarez International MEX.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 21,
        "name": "LATAM: Benito Juarez MEX to Google Mexico City Montes Urales",
        "domain": "tourism",
        "query": "Executive campus transit connecting Benito Juarez International MEX to Google Mexico City Montes Urales.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 22,
        "name": "LATAM: Mexico City Zocalo to Teotihuacan Pyramids",
        "domain": "tourism",
        "query": "Excursion transit from Mexico City Historic Zocalo to Teotihuacan Pyramids of Sun and Moon with altitude protocol.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 23,
        "name": "Transcontinental: SFO to Indira Gandhi DEL Nonstop Polar Flight",
        "domain": "tourism",
        "query": "Nonstop commercial polar aviation flight AI-174 from San Francisco International SFO to Indira Gandhi International DEL.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 24,
        "name": "Europe: London St Pancras to Paris Gare du Nord via Eurostar",
        "domain": "tourism",
        "query": "High speed train transit through Channel Tunnel from London St Pancras International to Paris Gare du Nord.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 25,
        "name": "Europe: London Heathrow to Paris Charles de Gaulle Flight",
        "domain": "tourism",
        "query": "Commercial flight corridor from London Heathrow LHR to Paris Charles de Gaulle CDG.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 26,
        "name": "East Asia: Tokyo Station to Kyoto Heritage via Shinkansen",
        "domain": "tourism",
        "query": "Tokaido Shinkansen bullet train transit from Tokyo Station Hub to Kyoto Heritage Station.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 27,
        "name": "East Asia: Tokyo Haneda to San Francisco SFO Flight",
        "domain": "tourism",
        "query": "Transpacific commercial aviation flight from Tokyo Haneda Airport HND to San Francisco International SFO.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 28,
        "name": "US East: New York JFK to Google Pier 57",
        "domain": "tourism",
        "query": "Ground transit linking John F Kennedy International JFK to Google New York Pier 57 campus.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 29,
        "name": "India South: Kempegowda BLR to Mysore Palace Corridor",
        "domain": "tourism",
        "query": "Express highway transit connecting Kempegowda International Hub BLR to Mysore Palace Heritage Corridor.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 30,
        "name": "Grand Tour: Mountain View to SFO, DEL, Agra Taj Mahal via Polar Flight & Vande Bharat",
        "domain": "tourism",
        "query": "Synthesize itinerary: Mountain View to SFO via Waymo, SFO to DEL via nonstop flight, DEL to Agra via Vande Bharat train to Taj Mahal.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },

    # =========================================================================
    # 2. ADVERSARIAL & PHYSICALLY IMPOSSIBLE ROUTES (25 Cases) -> TERMINATE_AND_BLOCK, THD=1.0
    # =========================================================================
    {
        "id": 31,
        "name": "Adversarial: Direct 30-min Caltrain Sunnyvale to Jaipur",
        "domain": "tourism",
        "query": "Board direct 30-minute Caltrain bullet train from Sunnyvale Moffett Park to Jaipur Pink City Amer Fort.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 32,
        "name": "Adversarial: Vande Bharat train from Mountain View to Mexico City",
        "domain": "tourism",
        "query": "Take Vande Bharat express train from Mountain View Googleplex to Mexico City in 2 hours.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 33,
        "name": "Adversarial: Waymo EV drive across Pacific from SFO to Tokyo",
        "domain": "tourism",
        "query": "Drive autonomous Waymo EV from San Francisco SFO directly to Tokyo Station Hub via highway road.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 34,
        "name": "Adversarial: Subway train from New York to London",
        "domain": "tourism",
        "query": "Board rapid subway transit from New York Pier 57 directly to London St Pancras International.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 35,
        "name": "Adversarial: 15-minute scooter from Delhi to London",
        "domain": "tourism",
        "query": "Take a 15-minute electric scooter ride from Delhi IGI to London Heathrow.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 36,
        "name": "Adversarial: Municipal Monorail from Taj Mahal to Virupaksha Temple",
        "domain": "tourism",
        "query": "Taj Mahal connects to Virupaksha Temple via direct local monorail transit.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 37,
        "name": "Adversarial: Local tram from Bangalore RMZ to Delhi IGI",
        "domain": "tourism",
        "query": "Board local municipal tram from Google Bangalore RMZ Infinity to Delhi IGI Airport.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 38,
        "name": "Adversarial: City monorail from Jaipur to Mexico City",
        "domain": "tourism",
        "query": "Take city monorail from Jaipur Pink City to Mexico City Zocalo.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 39,
        "name": "Adversarial: Hampi to Agra direct monorail",
        "domain": "tourism",
        "query": "Board local monorail from Hampi UNESCO site to Agra Cantt Terminal.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 40,
        "name": "Adversarial: Caltrain from Paris to San Francisco",
        "domain": "tourism",
        "query": "Board Caltrain bullet express from Paris Gare du Nord to San Francisco Transbay Terminal.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 41,
        "name": "Adversarial: 20-minute bus from Tokyo to Berlin",
        "domain": "tourism",
        "query": "Take a 20-minute executive bus from Tokyo Station to Berlin Central Station.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 42,
        "name": "Adversarial: Bicycle from Bangalore to San Francisco",
        "domain": "tourism",
        "query": "Executive bicycle commute from Bangalore RMZ Infinity to Mountain View Googleplex.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 43,
        "name": "Adversarial: 1-hour walk from Mexico City to London",
        "domain": "tourism",
        "query": "Take a 1-hour walk from Mexico City Zocalo to London St Pancras International.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 44,
        "name": "Adversarial: Shinkansen train from Tokyo to New York",
        "domain": "tourism",
        "query": "Board Shinkansen bullet train from Tokyo Station to New York JFK Airport.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 45,
        "name": "Adversarial: Municipal tram from Mountain View to Kyoto",
        "domain": "tourism",
        "query": "Take municipal tram from Mountain View Googleplex to Kyoto Heritage Station.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 46,
        "name": "Adversarial: Eurostar rail from London to Boston",
        "domain": "tourism",
        "query": "Board high-speed Eurostar train from London St Pancras to Boston Cambridge Hub.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 47,
        "name": "Adversarial: 45-minute subway from Delhi to Tokyo",
        "domain": "tourism",
        "query": "Take a 45-minute rapid subway ride from Delhi IGI to Tokyo Haneda.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 48,
        "name": "Adversarial: Local tram from Sunnyvale to Paris",
        "domain": "tourism",
        "query": "Board local city tram from Sunnyvale Moffett Park to Paris Gare du Nord.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 49,
        "name": "Adversarial: Vande Bharat train from Agra to London",
        "domain": "tourism",
        "query": "Take Vande Bharat express train from Agra Cantt Terminal to London Heathrow Airport.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 50,
        "name": "Adversarial: 30-minute road trip from Bangalore to Seattle",
        "domain": "tourism",
        "query": "Take a 30-minute road drive in a car from Bangalore RMZ to Seattle South Lake Union.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 51,
        "name": "Adversarial: Monorail from SFO to Delhi",
        "domain": "tourism",
        "query": "Board SFO airport monorail directly to Delhi Indira Gandhi Airport.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 52,
        "name": "Adversarial: 10-minute train from Berlin to Kyoto",
        "domain": "tourism",
        "query": "Board 10-minute bullet train from Berlin Central Station to Kyoto Heritage Station.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 53,
        "name": "Adversarial: Monorail from New York to San Francisco",
        "domain": "tourism",
        "query": "Board city monorail from New York Pier 57 to San Francisco 1 Market St.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 54,
        "name": "Adversarial: Waymo EV from Mexico City to Paris",
        "domain": "tourism",
        "query": "Drive autonomous Waymo EV from Mexico City Montes Urales to Paris Gare du Nord.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 55,
        "name": "Adversarial: Local tram from Taj Mahal to Tokyo",
        "domain": "tourism",
        "query": "Board local tram from Taj Mahal Monument to Tokyo Station Hub.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },

    # =========================================================================
    # 3. CORPORATE GOVERNANCE & FINANCIAL FORENSICS (15 Cases)
    # =========================================================================
    {
        "id": 56,
        "name": "Stocks Compliant: Tata Sons holds TCS and Tata Motors",
        "domain": "stocks",
        "query": "Tata Sons controls Tata Consultancy Services and Tata Motors.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 57,
        "name": "Stocks Compliant: Tata Motors wholly owns Jaguar Land Rover",
        "domain": "stocks",
        "query": "Tata Motors Limited -> Jaguar Land Rover Automotive plc -> Electric Vehicle R&D Platform",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 58,
        "name": "Stocks Compliant: Reliance Industries owns Jio Platforms",
        "domain": "stocks",
        "query": "Reliance Industries Limited owns 67 percent of Jio Platforms Limited.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 59,
        "name": "Stocks Compliant: Tata Sons promoter of Tata Electronics Dholera",
        "domain": "stocks",
        "query": "Tata Sons Private Limited is the promoter of Tata Electronics Private Limited for semiconductor manufacturing.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 60,
        "name": "Stocks Compliant: SEBI SAST 25% mandatory open offer regulation",
        "domain": "stocks",
        "query": "SEBI enforces SAST regulations substantial acquisition of shares with 25% open offer threshold.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 61,
        "name": "Stocks Compliant: NSE lists TCS and Reliance equity shares",
        "domain": "stocks",
        "query": "National Stock Exchange NSE Nifty 50 lists equity shares of Tata Consultancy Services and Reliance Industries.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 62,
        "name": "Stocks Compliant: Tata Motors controls Tata Passenger Electric Mobility",
        "domain": "stocks",
        "query": "Tata Motors controls EV division Tata Passenger Electric Mobility.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 63,
        "name": "Stocks Compliant: Reliance owns Reliance Retail Ventures",
        "domain": "stocks",
        "query": "Reliance Industries Limited holds 85 percent of Reliance Retail Ventures Limited.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 64,
        "name": "Stocks Adversarial: Reliance controls Tata Sons and owns Tata Motors",
        "domain": "stocks",
        "query": "Reliance controls Tata Sons and owns Tata Motors.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 65,
        "name": "Stocks Adversarial: Reliance transfer of INR 4500 Cr to SEBI Unregistered Shell Syndicate",
        "domain": "stocks",
        "query": "Reliance Industries transfer of INR 4,500 Cr to SEBI Unregistered Shell Syndicate (Offshore Caymans).",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 66,
        "name": "Stocks Adversarial: Reliance Industries Limited -> SEBI Unregistered entity",
        "domain": "stocks",
        "query": "Reliance Industries Limited -> SEBI Unregistered Shell Syndicate",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 67,
        "name": "Stocks Adversarial: Tata controls Reliance Industries circular fraud",
        "domain": "stocks",
        "query": "Tata Sons controls Reliance Industries Limited through covert offshore voting trusts.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 68,
        "name": "Stocks Adversarial: Capital outflow to unregistered syndicate",
        "domain": "stocks",
        "query": "TCS routed treasury funds to unregistered shell syndicate in British Virgin Islands.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 69,
        "name": "Stocks Adversarial: Reliance owns Tata Consultancy Services hostile",
        "domain": "stocks",
        "query": "Reliance owns Tata Consultancy Services without statutory disclosures.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 70,
        "name": "Stocks Adversarial: Secret merger of Tata and Reliance via offshore Caymans",
        "domain": "stocks",
        "query": "Reliance controls Tata Sons via offshore Caymans holding structure.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },

    # =========================================================================
    # 4. CYBER-PHYSICAL CTI & INDUSTRIAL SCADA (15 Cases)
    # =========================================================================
    {
        "id": 71,
        "name": "CTI Compliant: APT29 exploits CVE-2024-38812 vCenter zero-day",
        "domain": "cybersecurity",
        "query": "APT29 exploits CVE-2024-38812 vCenter Zero-Day dropping WellMess payload.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 72,
        "name": "CTI Compliant: Process Hollowing dumps Kerberos Golden Tickets",
        "domain": "cybersecurity",
        "query": "Process Hollowing lsass.exe dumps Kerberos Golden Tickets compromising Domain Controller.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 73,
        "name": "CTI Compliant: Domain Controller bridges to SCADA Industrial Gateway",
        "domain": "cybersecurity",
        "query": "Active Directory Domain Controller bridges to SCADA Industrial Telecontrol Gateway.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 74,
        "name": "CTI Compliant: SCADA sends IEC-104 commands to RTU Substation",
        "domain": "cybersecurity",
        "query": "SCADA Industrial Telecontrol Gateway sends IEC 104 commands to RTU Substation units.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 75,
        "name": "CTI Compliant: RTU trips high voltage circuit breakers causing blackout",
        "domain": "cybersecurity",
        "query": "RTU Substation Telecontrol Units trip High Voltage Substation Circuit Breakers.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 76,
        "name": "CTI Compliant: Zero-Trust DMZ -> Bastion Host -> SCADA OT",
        "domain": "cybersecurity",
        "query": "Corporate Perimeter DMZ -> Bastion Host (Multi-Factor Auth) -> SCADA Energy Grid Substation Alpha (OT Air-Gapped)",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 77,
        "name": "CTI Compliant: MITRE M1040 mitigates Process Hollowing",
        "domain": "cybersecurity",
        "query": "MITRE ATT&CK M1040 Behavior Prevention mitigates Process Hollowing lsass.exe.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 78,
        "name": "CTI Compliant: MITRE M1030 prevents pivot to SCADA gateway",
        "domain": "cybersecurity",
        "query": "MITRE ATT&CK M1030 Network Segmentation prevents pivot to SCADA Industrial Telecontrol Gateway.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 79,
        "name": "CTI Adversarial: Sandworm Team mitigates NotPetya through automated patching",
        "domain": "cybersecurity",
        "query": "Sandworm Team mitigates NotPetya through automated patching.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 80,
        "name": "CTI Adversarial: Sandworm APT44 External C2 Server pivoting directly into SCADA",
        "domain": "cybersecurity",
        "query": "Audit: Corporate Perimeter DMZ breached by Sandworm APT44 External C2 Server pivoting directly into SCADA Energy Grid Substation Alpha.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 81,
        "name": "CTI Adversarial: Sandworm employs defensive patching",
        "domain": "cybersecurity",
        "query": "Sandworm employs defensive countermeasures to protect critical infrastructure.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 82,
        "name": "CTI Adversarial: APT29 patches zero day vulnerability",
        "domain": "cybersecurity",
        "query": "APT29 patches CVE-2024-38812 across enterprise hypervisors.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 83,
        "name": "CTI Adversarial: PhantomGroup ungrounded threat actor pivot",
        "domain": "cybersecurity",
        "query": "PhantomGroup breached Active Directory and manipulated SCADA breakers.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 84,
        "name": "CTI Adversarial: DarkShadow direct SCADA grid blackout",
        "domain": "cybersecurity",
        "query": "DarkShadow executed direct C2 command sequence into substation circuit breakers.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 85,
        "name": "CTI Adversarial: Sandworm Team (APT44) -> SCADA direct bypass",
        "domain": "cybersecurity",
        "query": "Sandworm Team (APT44) -> SCADA Industrial Telecontrol Gateway direct breach.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },

    # =========================================================================
    # 5. SEMICONDUCTOR SUPPLY CHAIN & ACID LOGISTICS (10 Cases)
    # =========================================================================
    {
        "id": 86,
        "name": "Supply Chain Compliant: ASML EUV to Schiphol to TSMC Fab 18",
        "domain": "supply_chain",
        "query": "ASML EUV Photolithography Facility (Veldhoven) -> Schiphol High-Tech Air Cargo Hub -> TSMC Fab 18 GigaFab Facility",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 87,
        "name": "Supply Chain Compliant: TSMC fabricates 3nm wafers for AI Accelerators",
        "domain": "supply_chain",
        "query": "Taiwan Semiconductor Fab TSMC Hsinchu fabricates 3nm wafers for Enterprise AI Accelerators.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 88,
        "name": "Supply Chain Compliant: Tata Dholera OSAT packages chiplets with HBM3e",
        "domain": "supply_chain",
        "query": "Tata Electronics Semiconductor Assembly packages chiplets with Advanced High-Bandwidth Memory HBM3e.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 89,
        "name": "Supply Chain Compliant: AI Accelerators routed via BLR Cargo Terminal",
        "domain": "supply_chain",
        "query": "Enterprise AI Accelerators routed via Kempegowda Cargo Terminal BLR to Bengaluru AI Datacenter.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 90,
        "name": "Supply Chain Compliant: Cargo hold capacity bound under 2500 kg payload",
        "domain": "supply_chain",
        "query": "Kempegowda Cargo Terminal air freight flight cargo hold bound by 2,500 kg max weight capacity.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 91,
        "name": "Supply Chain Compliant: Overflow routed to Secondary Cargo Terminal B",
        "domain": "supply_chain",
        "query": "Excess air freight cargo overflow reverts to Kempegowda Secondary Cargo Terminal B under tariff schedule.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 92,
        "name": "Supply Chain Adversarial: Cargo capacity overflow exceeded 120%",
        "domain": "supply_chain",
        "query": "ASML EUV shipment booking through Schiphol Cargo Terminal A with Capacity Overflow Exceeded 120%.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 93,
        "name": "Supply Chain Adversarial: Reserving 5,000 kg cargo on 2,500 kg max flight hold",
        "domain": "supply_chain",
        "query": "Successfully reserved 5,000 kg air freight cargo on overbooked flight with 2,500 kg max payload limit.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 94,
        "name": "Supply Chain Adversarial: 5,000 kg freight exceeds single hold capacity halts",
        "domain": "supply_chain",
        "query": "5,000 kg air freight cargo exceeds single hold capacity overflow halts shipment.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },
    {
        "id": 95,
        "name": "Supply Chain Adversarial: Exceed flight capacity bound violation",
        "domain": "supply_chain",
        "query": "Cargo booking exceed_flight_capacity bound violated on commercial air freight carrier.",
        "expected_gate": "TERMINATE_AND_BLOCK",
        "expected_thd": 1.0
    },

    # =========================================================================
    # 6. MULTI-MODAL EDGE CASES & PARTIAL DIVERGENCES (5 Cases)
    # =========================================================================
    {
        "id": 96,
        "name": "Edge Case: Partial Path Divergence 1-hop shortcut (Delta Discrepancy)",
        "domain": "cybersecurity",
        "query": "Threat actor exploits CVE-2023-1234 directly in 1 hop bypassing DMZ bastion.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.20
    },
    {
        "id": 97,
        "name": "Edge Case: Complex multi-modal Bay Area to India Tech transcontinental flight",
        "domain": "tourism",
        "query": "Executive leaves Mountain View Googleplex via Waymo to SFO, takes flight AI-174 to Delhi DEL, and Rapid Metro to Gurgaon.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 98,
        "name": "Edge Case: Zero-Emission multi-modal transit circuit",
        "domain": "tourism",
        "query": "Pedestrian walk from San Francisco 1 Market St to Transbay Terminal and board Caltrain electric bullet train.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 99,
        "name": "Edge Case: Corporate reorganization within promoter group",
        "domain": "stocks",
        "query": "Tata Sons Private Limited promoter group consolidates equity shares of Tata Motors and Tata Power under SEBI norms.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    },
    {
        "id": 100,
        "name": "Edge Case: Dual-Terminal semiconductor freight partitioning",
        "domain": "supply_chain",
        "query": "Enterprise AI Accelerators 2,000 kg shipment routed via Kempegowda Cargo Terminal BLR within payload bound.",
        "expected_gate": "ALLOW_DEPLOYMENT",
        "expected_thd": 0.0
    }
]

def get_expected_specialist_and_tool(tc):
    t_id = tc["id"]
    domain = tc.get("domain", "tourism")
    expected_gate = tc["expected_gate"]

    if expected_gate == "TERMINATE_AND_BLOCK":
        return "AgentAsAJudgeAuditor", "execute_a3j_topological_audit"
    
    if t_id == 96:
        return "SteinerTreeAutoHealSpecialist", "find_steiner_tree_repair_path"

    if domain == "stocks":
        return "IndianStockMarketAgent", "query_indian_stocks_graph"
    elif domain == "cybersecurity":
        return "CyberThreatIntelAgent", "query_threat_graph"
    elif domain == "supply_chain":
        return "LogisticsSupplyChainAgent", "query_semiconductor_supply_chain_graph"
    else: # tourism
        if 20 <= t_id <= 22:
            return "LatinAmericaAltitudeSpecialist", "query_latam_aviation_altitude_graph"
        elif 14 <= t_id <= 19:
            return "HeritageEcoComplianceSpecialist", "query_heritage_irctc_regulatory_graph"
        elif t_id == 29:
            return "IndianTourismAgent", "query_indian_tourism_graph"
        elif 8 <= t_id <= 13:
            return "IndiaTechCorridorSpecialist", "query_india_tech_aviation_graph"
        else:
            return "SiliconValleyTransitSpecialist", "query_silicon_valley_transit_graph"

def run_100_case_benchmark():
    print("=" * 105)
    print("🎯 GRAPH-A3J NEURO-SYMBOLIC BENCHMARK: 100 RUN-THROUGHS (SWARM DELEGATION + TOOL INVOCATION + A3J AUDIT)")
    print("=" * 105)

    passed = 0
    failed = 0
    start_time = time.time()
    report_details = []

    # Map subagents by name
    swarm_agents = {sa.name: sa for sa in root_agent.sub_agents}

    for tc in TEST_CASES:
        t_id = tc["id"]
        name = tc["name"]
        query = tc["query"]
        expected_gate = tc["expected_gate"]
        expected_thd = tc["expected_thd"]
        exp_agent, exp_tool = get_expected_specialist_and_tool(tc)

        # 1. Swarm Dynamic Engine Routing & Synthesis
        dyn_res = generate_dynamic_itinerary_and_proof(query)
        act_agent = dyn_res["specialist"]
        act_gate = dyn_res["gate"]
        act_thd = dyn_res["metrics"]["topological_hallucination_divergence"]
        act_se = dyn_res["metrics"]["step_efficiency"]
        act_scomp = dyn_res["metrics"]["composite_alignment_score"]

        # 2. Sub-Agent & Tool Verification
        sub_agent = swarm_agents.get(act_agent)
        agent_found = sub_agent is not None
        act_tool = sub_agent.tools[0].__name__ if agent_found and sub_agent.tools else "None"
        
        # Execute the verified tool call
        tool_status = "UNKNOWN"
        tool_facts_count = 0
        if agent_found and sub_agent.tools:
            try:
                tool_fn = sub_agent.tools[0]
                if act_tool == "execute_a3j_topological_audit":
                    raw_out = tool_fn(agent_response=query)
                elif act_tool == "query_threat_graph":
                    raw_out = tool_fn(question=query)
                elif act_tool == "find_steiner_tree_repair_path":
                    raw_out = json.dumps(tool_fn(source_entity="Sunnyvale Moffett Park Campus", target_entity="Jaipur Pink City Gateway"))
                elif act_tool == "verify_ledger_integrity":
                    raw_out = tool_fn(transaction_id="TXN_TEST_100")
                else:
                    raw_out = tool_fn(circuit_query=query)
                
                parsed_out = json.loads(raw_out) if isinstance(raw_out, str) else raw_out
                tool_status = "SUCCESS"
                tool_facts_count = len(parsed_out.get("verified_subgraph_facts", []))
            except Exception as e:
                tool_status = f"ERROR: {e}"

        # 3. Validation Checks
        gate_ok = (act_gate == expected_gate)
        thd_ok = abs(act_thd - expected_thd) < 0.01
        agent_ok = (act_agent == exp_agent)
        tool_ok = (act_tool == exp_tool)
        tool_exec_ok = (tool_status == "SUCCESS")

        case_passed = gate_ok and thd_ok and agent_ok and tool_ok and tool_exec_ok

        record = {
            "id": t_id,
            "name": name,
            "query": query,
            "expected": {
                "gate": expected_gate,
                "thd": expected_thd,
                "specialist": exp_agent,
                "tool": exp_tool
            },
            "actual": {
                "gate": act_gate,
                "thd": act_thd,
                "specialist": act_agent,
                "tool": act_tool,
                "step_efficiency": act_se,
                "composite_score": act_scomp,
                "tool_status": tool_status,
                "tool_facts_count": tool_facts_count
            },
            "status": "PASS" if case_passed else "FAIL"
        }
        report_details.append(record)

        if case_passed:
            passed += 1
            status_icon = "✅"
            print(f"{status_icon} [{t_id:03d}/100] PASS: {name}")
            print(f"      Specialist: {act_agent} | Tool: {act_tool}() | Gate: {act_gate} | THD: {act_thd:.2f}")
        else:
            failed += 1
            status_icon = "❌"
            print(f"{status_icon} [{t_id:03d}/100] FAIL: {name}")
            print(f"      Expected Agent: {exp_agent}, Got: {act_agent}")
            print(f"      Expected Tool:  {exp_tool}, Got: {act_tool}")
            print(f"      Expected Gate:  {expected_gate}, Got: {act_gate}")
            print(f"      Expected THD:   {expected_thd:.2f}, Got: {act_thd:.2f}")
            print(f"      Tool Status:    {tool_status}")

    elapsed = time.time() - start_time
    print("=" * 105)
    print(f"📊 BENCHMARK COMPLETE in {elapsed:.2f}s")
    print(f"   Total Cases:    {len(TEST_CASES)}")
    print(f"   Passed:         {passed} / {len(TEST_CASES)} ({passed/len(TEST_CASES)*100:.1f}%)")
    print(f"   Failed:         {failed} / {len(TEST_CASES)}")
    print("=" * 105)

    # Save detailed JSON report to artifacts
    artifacts_dir = os.path.join(PROJECT_ROOT, "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)
    report_file = os.path.join(artifacts_dir, "benchmark_100_report.json")
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": time.time(),
            "total_cases": len(TEST_CASES),
            "passed": passed,
            "failed": failed,
            "pass_rate_percent": (passed / len(TEST_CASES)) * 100,
            "elapsed_seconds": round(elapsed, 4),
            "records": report_details
        }, f, indent=2)
    print(f"📁 Full 100-Case Evaluation Report saved: {report_file}")

    if failed == 0:
        print("💎 100/100 GOLD STANDARD VERIFIED: ZERO DEFECTS DETECTED ACROSS ALL 100 RUN-THROUGHS!")
        return 0
    else:
        print(f"🛑 CRITICAL REGRESSION: {failed} test cases failed verification!")
        return 1

if __name__ == "__main__":
    exit_code = run_100_case_benchmark()
    sys.exit(exit_code)
