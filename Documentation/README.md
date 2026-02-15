# SCORE — Smart Context-aware Outfit Recommendation Engine

SCORE is an intelligent system designed to assist users in selecting outfit combinations that are aesthetically compatible, contextually appropriate, and personalized through feedback. By combining computer vision, fuzzy logic, and reinforcement learning, SCORE provides explainable and adaptive style guidance.

## 🌟 High-Level Project Summary
SCORE bridges the gap between raw visual perception and structured aesthetic reasoning. The system identifies garments from images, extracts their color attributes, and evaluates them against a set of expert-inspired fuzzy rules. It adapts to user preferences over time via a lightweight reinforcement learning loop, ensuring recommendations become increasingly personalized.

## 🛠️ System Description
The project is built on **Clean Architecture** principles, ensuring a strict separation between domain logic and technology adapters.
- **Computer Vision Perception**: Automatic garment classification and color extraction using trained CNN models (Production-Ready weights included).
- **Manual Input Fallback**: Robust manual entry mode for all garment attributes.
- **Fuzzy Logic Scoring**: Nuanced compatibility evaluation based on color harmony and formality rules.
- **Context-Awareness**: Recommendations tailored to specific occasions (e.g., University, Gym, Formal events).
- **Personalization (Reinforcement-lite)**: Adaptation to user preferences through a lightweight feedback loop.
- **Clean Architecture**: Modular design separating domain logic, technology adapters, and UI (CLI/GUI).
- **Data Policy**: The training dataset (46,000 images) is excluded from the deployment to minimize footprint, but the system is production-ready using the provided weights.

## 📂 Documentation Map
The project documentation is organized into thematic modules:

*   **[01 – Overview](./01_Overview/01_Project_Introduction.md)**: Goals, problem statement, scope, and the **[Feature Maturity Matrix](./01_Overview/03_Objectives_and_Scope.md#3-feature-maturity-matrix-version-1)**.
*   **[02 – Data & Datasets](./02_Data_and_Datasets/01_Dataset_Description.md)**: Dataset specs (46k images, 80/20 split), preprocessing, and privacy.
*   **[03 – Modeling & Learning](./03_Modeling_and_Learning/01_Model_Architecture_Overview.md)**: CNN architecture, RL personalization, and size/accuracy tradeoffs.
*   **[04 – Architecture & Technology](./04_Architecture_and_Technology/01_System_Architecture.md)**: Clean Architecture layers, multi-module structure, and tech stack.
*   **[05 – Scoring & Decision Logic](./05_Scoring_and_Decision_Logic/01_Scoring_System_Overview.md)**: Fuzzy rules, context-aware logic, and explainability.
*   **[06 – User Interaction & Workflows](./06_User_Interaction_and_Workflows/01_My_Wardrobe_Concept.md)**: Input flows, wardrobe management, and feedback loops.

## 🏛️ Architecture Overview
SCORE follows a **Multi-Module** structure:
- `packages/core`: Domain entities, use cases, and the scoring brain. (No UI/Framework dependencies)
- `packages/cli`: Terminal interface built with Typer.
- `packages/gui`: Interactive dashboard built with Streamlit.

## 🚀 Quick Start

### 1️⃣ Create environment (Conda)
```bash
conda create -n score python=3.11 -y
conda activate score
```

### 2️⃣ Install Dependencies (using uv)
```bash
python -m pip install -U uv
uv pip install -e packages/core
uv pip install -e packages/cli
uv pip install -e packages/gui
```

### 3️⃣ Run the Application
- **CLI**: `score recommend run --context university`
- **GUI**: `streamlit run packages/gui/src/score_gui/app.py`

---
*For a detailed status of all features, see the [Feature Maturity Matrix](./01_Overview/03_Objectives_and_Scope.md#3-feature-maturity-matrix-version-1).*
