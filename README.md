# ecotrace-ai
AI Agent tracking supply chain carbon footprints using Gemini 1.5 Pro and MongoDB Atlas.
<img width="1536" height="1024" alt="aa" src="https://github.com/user-attachments/assets/604b5a74-2857-40f8-97f6-76cb7c24d2dd" />
# 📦 EcoTrace AI: Multi-Modal Sustainable Supply Chain Agent

AI Agent tracking supply chain carbon footprints using Google Cloud Vertex AI (Gemini 1.5 Pro) and MongoDB Atlas.

---

## 🏗️ System Architecture Blueprint

![EcoTrace AI Architecture](https://res.cloudinary.com/practicaldev/image/fetch/s--V_S6Wv3V--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/http%3A%2F%2Fgoogleusercontent.com%2Fimage_generation_content%2F1)

### 📊 Blueprint Explanation & System Flow:

The entire EcoTrace AI infrastructure processes unstructured, multi-modal logistics data through a 3-stage intelligence pipeline to generate proactive green actions:

1. **📂 Stage 1: Multi-Modal Data Ingestion (Vertex AI Vision)**
   * **Visual Cargo Tracking:** Processes physical cargo container photos to identify freight vehicle types and transit conditions.
   * **Vernacular OCR Processing:** Automatically scans and reads unformatted freight bills, fuel receipts, and multi-language shipping documents.
   * **Spatial Telematics:** Ingests live GPS logs and maritime routing updates to track real-time travel parameters.

2. **🤖 Stage 2: Core Gemini 1.5 Pro Reasoning Hub**
   * **Data Structuring:** Gemini 1.5 Pro translates chaotic text and visual inputs into clean, unified JSON data arrays.
   * **Carbon Footprint Calculus:** Dynamically maps out the mathematical emissions model:
     $$E = \sum_{i=1}^{n} (W_i \times D_i \times C_i)$$
     *(Where $W$ = Cargo Weight, $D$ = Distance traveled, and $C$ = Transport Carbon Intensity Coefficient).*

3. **🛰️ Stage 3: Agentic Action & Storage Layer (MongoDB Atlas & BigQuery)**
   * **Decentralized Storage:** High-density logistics graphs and multi-modal tracking records are securely archived in **MongoDB Atlas**.
   * **Eco-Shield Alerts:** If the estimated carbon output breaches eco-compliance thresholds, the agent automatically triggers a **Supplier Violation Flag**.
   * **Proactive Green Routing:** Dynamically suggests optimized "Green Corridors" via BigQuery ML to minimize corporate carbon spikes.
