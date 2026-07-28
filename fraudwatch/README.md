# FraudWatch

Hands-on **transaction fraud detection** project for interviews.

**Goal:** flag fraud without drowning analysts in false alarms.  
**North-star metrics:** PR-AUC, Precision@K, and precision at a fixed recall (e.g. 80%).

This folder lives next to the [AI from scratch](https://ai.josyulablog.org/) site so progress stays public.  
Tracker: https://ai.josyulablog.org/projects.html#start

---

## Step-by-step: how to start (Week 1)

### Step 0 — Setup (30–45 min)

1. Install Python 3.10+ and create a virtualenv (recommended):

```bash
cd fraudwatch
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Create a GitHub repo later if you want it separate; for now you can work inside this folder.

3. Open a notes doc (or a page on the blog) titled **FraudWatch build log — Week 1**.

### Step 1 — Understand the problem (45 min)

Write 5–10 lines answering:

- Who uses the model? (fraud analyst)
- What is a false positive vs false negative cost?
- Why is **accuracy** a terrible metric here?

Fraud is rare (~0.17% in this dataset). A model that always says “not fraud” is ~99.8% accurate and useless.

### Step 2 — Load data & peek (1–2 hrs)

```bash
python 01_baseline.py
```

What this script does:

1. Downloads the public **creditcard** dataset via OpenML (PCA features `V1…V28` + `Amount`)
2. Shows class imbalance
3. Stratified train/test split
4. Trains **Logistic Regression** and **Random Forest**
5. Reports Precision, Recall, F1, ROC-AUC, **PR-AUC**
6. Saves a simple PR curve under `artifacts/`

Read the printed table. Note which model wins on **PR-AUC** (not accuracy).

### Step 3 — Force the right metric (1 hr)

In your build log, paste:

- Class counts
- PR-AUC for both models
- One sentence: which model you’d put in front of analysts **today** and why

### Step 4 — Threshold thinking (Week 1 stretch)

Fraud scores are probabilities. Analysts need a cutoff:

- High threshold → fewer alerts, miss more fraud (low recall)
- Low threshold → more alerts, more noise (low precision)

Next script (`02_thresholds.py` — we’ll add when you finish Step 2) will sweep thresholds and plot precision/recall.

### Step 5 — Interview drill (30 min)

Answer out loud (see site interview bank):

1. When is accuracy a bad metric?
2. Precision vs recall — which matters more for fraud review queues?
3. What is data leakage? Could `Amount` or time ordering leak if we split wrong?

---

## Roadmap for this project

| Week | Milestone | Output |
|------|-----------|--------|
| 1 | Baseline | `01_baseline.py` runs; build-log notes |
| 2 | Thresholds + cost matrix | Choose operating point; PR curve |
| 3 | Stronger model | LightGBM/HistGBM + calibration |
| 4 | Hardening | Time-aware concerns, error analysis |
| 5–6 | Ship v1 | FastAPI `/score` endpoint |
| later | FilingPilot | RAG over filings (GenAI layer) |

---

## Data note

Dataset: OpenML `creditcard` (same famous anonymised PCA fraud set).  
Features `V1–V28` are transformed — you can’t invent domain stories about “merchant category,” but you **can** practice the ML craft interviewers test.
