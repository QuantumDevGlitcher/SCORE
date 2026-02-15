# 07 – Deployment Assumptions

## 1. Deployment Context

SCORE is developed as an academic intelligent systems project.

It is not intended for production deployment in Version 1.

Deployment assumptions are therefore aligned with:

- local execution
- classroom demo usage
- small team collaboration
- CPU-only environments

---

## 2. Target Execution Environment

Supported platforms:

- Windows 10/11
- macOS (Intel / Apple Silicon with CPU support)

Minimum hardware:

- 8GB RAM
- CPU-only execution (no GPU required)
- ~2GB free disk space for environment + dependencies

---

## 3. Runtime Requirements

- Python 3.11
- Conda environment named `score`
- uv-installed dependencies
- Local file system access

No cloud services are required.

No internet connection is required after dependencies are installed.

---

## 4. Model and Dataset Handling

### 4.1 Dataset

- Training dataset (~46,000 images) is NOT included in the repository.
- The dataset is used only for training experiments.
- It is excluded from version control.

### 4.2 Model Files

- Trained models (100–500MB range depending on an accuracy threshold) are not committed to Git.
- Models may be:
  - stored locally,
  - shared via external storage (e.g., cloud drive),
  - or replaced with stub logic for demo purposes.

Version 1 does not require large model downloads at runtime.

---

## 5. Execution Modes

SCORE can be executed in two modes:

### 5.1 CLI Mode

```bash
score recommend run --context presentation
```

or

```bash
python -m score_cli.main recommend run --context presentation
```

Used for:
- fast testing
- debugging
- grading demonstrations

---

### 5.2 GUI Mode

```text
streamlit run packages/gui/src/score_gui/app.py
```

Used for:
- interactive demos
- visual presentation
- user testing

---

## 6. No GPU Requirement

Version 1 does not require GPU acceleration.

If PyTorch is installed with CPU support only, the system remains fully functional.

This simplifies cross-platform compatibility.

---

## 7. No Cloud Infrastructure

The system does not depend on:

- AWS
- Azure
- Google Cloud
- External APIs
- REST endpoints

All components run locally.

Future versions may optionally introduce:

- API layer (FastAPI)
- Cloud inference
- Model serving endpoints

These are not part of Version 1.

---

## 8. Docker Consideration

Docker is optional.

Reasons Docker is not mandatory:

- Conda + lock file ensures reproducibility.
- No distributed deployment is required.
- Small team and local execution.

Docker may be introduced if:

- environment conflicts appear,
- reproducibility across machines becomes unstable,
- deployment beyond classroom context is required.

---

## 9. Security and Privacy Assumptions

Version 1 does not:

- collect personal biometric data
- store sensitive user identity information
- transmit data externally

If body modeling or advanced perception is added in the future,
additional privacy documentation will be required.

---

## 10. Failure Handling Assumptions

If:

- model loading fails,
- perception fails,
- input is invalid,

the system will:

- return structured error messages,
- avoid crashing silently,
- maintain deterministic behavior.

Graceful degradation is preferred over runtime failure.

---

## 11. Summary

SCORE Version 1 is designed for:

- local execution,
- deterministic behavior,
- minimal infrastructure complexity,
- academic evaluation context.

It does not assume production deployment constraints.
