# ecotrace-ai
AI Agent tracking supply chain carbon footprints using Gemini 1.5 Pro and MongoDB Atlas.
<img width="1536" height="1024" alt="aa" src="https://github.com/user-attachments/assets/604b5a74-2857-40f8-97f6-76cb7c24d2dd" />
# 📦 EcoTrace AI: Multi-Modal Sustainable Supply Chain Agent

AI Agent tracking supply chain carbon footprints using Google Cloud Vertex AI (Gemini 1.5 Pro) and MongoDB Atlas.

---

## 🏗️ System Architecture Blueprint

<img width="1536" height="1024" alt="ec" src="https://github.com/user-attachments/assets/77a12a05-3632-4e8f-8824-fd7e4cac88b0" />


### 📊 Blueprint Explanation & System Flow:

EcoTrace AI operates as an automated enterprise sustainability agent, executing a unified 3-stage pipeline to analyze logistics operations and mitigate carbon spikes:

1. **📂 Stage 1: Multi-Modal Data Ingestion (Vertex AI Vision)**
   * **Visual Cargo Ingestion:** Scans physical cargo container photographs to catalog transport modes, freight dimensions, and container integrity.
   * **Vernacular OCR Decoding:** Automatically processes unstructured freight papers, fuel slips, and multi-language logistics receipts to extract core shipping parameters.
   * **Real-Time Telematics:** Captures live GPS logs and maritime routing updates to track continuous distance metrics.

2. **🤖 Stage 2: Core Gemini 1.5 Pro Reasoning Hub**
   * **Data Structuring Matrix:** Gemini 1.5 Pro synthesizes unstructured textual and visual arrays into structured JSON objects.
   * **Automated Emissions Calculus:** Feeds the dynamic mathematical model to evaluate real-time carbon footprints:
     $$E = \sum_{i=1}^{n} (W_i \times D_i \times C_i)$$
     *(Where $W$ = Cargo Weight, $D$ = Distance traveled, and $C$ = Mode-specific Carbon Intensity Coefficient).*

3. **🛰️ Stage 3: Agentic Action & Storage Layer (MongoDB Atlas & Looker)**
   * **Decentralized Logistics Graph:** High-density transactional ledgers and multi-modal tracking logs are stored instantly within **MongoDB Atlas**.
   * **Eco-Shield Protocols:** If a supplier's carbon footprint exceeds predefined localized compliance thresholds, the agent triggers an automated **Supplier Eco-Compliance Flag**.
   * **Enterprise Rerouting Alerts:** Dynamically pushes optimized "Green Corridor" recommendations directly to company dashboards via Looker to neutralize emission surges.
   
