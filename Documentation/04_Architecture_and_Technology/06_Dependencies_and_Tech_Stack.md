# 06 – Dependencies and Technology Stack

## 1. Overview

SCORE is designed as a modular, cross-platform Python system
targeting Windows and macOS environments.

The technology stack is selected based on:

- architectural clarity
- reproducibility
- minimal friction for a small academic team
- future extensibility

---

# 2. Python Version

- **Python 3.11.x**
- Managed through **Conda**
- Locked via `uv pip freeze`

Python 3.11 was chosen because:

- stable
- widely supported by PyTorch
- good performance improvements over 3.9/3.10
- compatible with Streamlit ecosystem

---

# 3. Environment Strategy

## 3.1 Environment Manager

We use:

- **Miniconda**
- `conda` for environment isolation
- `uv` for dependency installation and locking

### Why this combination?

Conda:
- handles Python version isolation cleanly
- reduces platform-specific binary issues (Windows/macOS)
- easier for mixed-skill teams

uv:
- fast dependency resolution
- reproducible lock generation
- modern replacement for traditional pip workflows

---

## 3.2 Lock Strategy

After installing dependencies:

```bash
uv pip freeze > requirements.lock.txt
```

This file ensures:

- all team members share identical dependency versions
- reproducible installs
- easier debugging across platforms

---

# 4. Core Dependencies (score-core)

## 4.1 ML / Vision

- `torch`
- `torchvision`
- `opencv-python`
- `numpy`

### Purpose

- Image processing (future)
- Feature extraction
- Tensor operations
- Foundation for perception layer

Note:
Version 1 does not require heavy model training.
Pretrained backbones or lightweight logic are enough.

---

## 4.2 Fuzzy Logic

- `scikit-fuzzy`

Purpose:
- Define membership functions
- Implement interpretable scoring logic
- Model soft fashion constraints (e.g., "too bright", "formal enough")

Rationale:
Fuzzy logic allows explainable scoring instead of black-box ML.

---

## 4.3 Data Validation

- `pydantic`

Purpose:
- Structured domain models
- Input validation
- Strong typing support

Used across domain and application layers.

---

# 5. CLI Dependencies (score-cli)

- `typer`
- `rich`
- `click` (via typer)

Purpose:

- Structured CLI commands
- Subcommand support
- Better output formatting
- Future extensibility

---

# 6. GUI Dependencies (score-gui)

- `streamlit`
- `pandas`
- `altair` (optional visualization)

Purpose:

- Rapid interactive interface
- Table visualization
- Demo-ready interface for presentations

GUI dependencies are isolated in `score-gui`.

Core must never depend on GUI libraries.

---

# 7. Storage Options

Version 1 supports:

- In-memory objects
- JSON storage (simple persistence)

Future option:
- SQLite
- SQLAlchemy

We avoid early database complexity in Version 1.

---

# 8. Testing and Code Quality

- `pytest`
- `ruff`
- optional: `pre-commit`

Purpose:

- ensure correctness
- enforce style
- maintain consistent code quality

---

# 9. Cross-Platform Considerations

Target platforms:

- Windows (primary development)
- macOS (expected team usage)

Key compatibility concerns:

- PyTorch CPU version consistency
- OpenCV binary compatibility
- Conda channel alignment

Conda mitigates most platform-specific issues.

---

# 10. Why Not Docker (Yet)

Docker is not mandatory for Version 1 because:

- Conda + lock file already ensures reproducibility
- Team size is small
- ML workloads are CPU-based
- No production deployment required

Docker may be added if:

- environment conflicts appear
- reproducibility becomes difficult
- deployment becomes required

---

# 11. Summary

The stack prioritizes:

- clarity
- modularity
- explainability
- reproducibility
- low friction for a mixed-experience team

This is not an experimental stack.

It is intentionally structured for long-term scalability.
