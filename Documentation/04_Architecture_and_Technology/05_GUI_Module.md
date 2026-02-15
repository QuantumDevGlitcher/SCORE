# 05 – GUI Module (score-gui)

## 1. Purpose

The GUI module provides a visual interface for SCORE to support:
- fast demos,
- non-technical users,
- interactive configuration (context, wardrobe items, feedback).

The GUI is a **presentation adapter**, not a logic layer.

---

## 2. Architectural Role

Within Clean Architecture:

```text
GUI
↓
Application Use Cases
↓
Domain
```

The GUI’s responsibility is to:
- collect user inputs (forms / selectors),
- call core use cases,
- render results (ranked outfits, explanations, scores),
- capture feedback (like/dislike/neutral).

The GUI must NOT:
- contain scoring rules,
- implement decision-making,
- replicate core logic.

---

## 3. Technology Stack

The GUI uses:

- **Streamlit** (rapid UI development)
- **Pandas** (optional table / dataset manipulation for display only)
- optional visualization libraries (Altair via Streamlit)

These dependencies exist ONLY inside `score-gui`.

Core must not depend on them.

---

## 4. GUI Features (Version 1)

Version 1 GUI is focused on enabling a functional demo:

- Context selection (e.g., university, presentation, gym)
- Manual garment input (kind, color, material)
- Wardrobe browsing (My Wardrobe concept)
- Recommendation results panel:
  - ranked list
  - numeric scores
  - explanation strings
- Feedback buttons (optional):
  - Like / Neutral / Dislike
  - used to simulate personalization loop (stub or minimal)

---

## 5. Data Flow

1. User selects context
2. User provides current garments (manual)
3. GUI calls core use case `recommend_outfits(...)`
4. GUI renders results (score + explanation)
5. User optionally provides feedback
6. GUI calls `update_preferences(...)` (future / optional)

---

## 6. Multi-Module Boundary

The GUI depends on `score-core` through imports such as:

- `score_core.domain.entities`
- `score_core.application.use_cases`

The GUI must never implement:
- fuzzy rules,
- scoring weights,
- ranking logic.

All intelligence lives inside core.

---

## 7. Example Internal Structure

```text
packages/gui/src/score_gui/
│
├── app.py
├── pages/
│ ├── recommend.py
│ ├── wardrobe.py
│ └── feedback.py
├── components/
│ ├── garment_form.py
│ ├── results_panel.py
│ └── context_selector.py
└── init.py
```

This keeps the UI modular and readable.

---

## 8. Testing Strategy

GUI tests are optional for Version 1.

If implemented, they should focus on:
- input validation logic at the UI layer
- formatting correctness
- mocking the core use case calls

Core must remain fully testable independently.

---

## 9. Why Streamlit

Streamlit is chosen because:

- it minimizes time spent building UI mechanics,
- allows rapid prototyping and iteration,
- is cross-platform,
- supports simple deployments for classroom demos.

The architectural separation ensures Streamlit can later be replaced by:
- a desktop GUI,
- a web frontend,
- a mobile client,
- or a REST API.

---

## 10. Future GUI Extensions

Potential future improvements:

- photo input + perception preview (“detected colors/materials”)
- wardrobe import/export
- recommendation history
- difference comparison view (before/after preference learning)

These are excluded from Version 1 unless time permits.

---

## 11. Summary

The GUI module:

- is a presentation adapter,
- provides an interactive demo layer,
- depends on core,
- contains zero business logic.

The GUI is replaceable.

The core is not.
