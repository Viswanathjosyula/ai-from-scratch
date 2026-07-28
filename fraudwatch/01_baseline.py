"""
FraudWatch — Week 1 baseline
----------------------------
Load the public credit-card fraud dataset, train two simple models,
and score them with imbalance-aware metrics (PR-AUC, not accuracy).

Run:
    python 01_baseline.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    PrecisionRecallDisplay,
    average_precision_score,
    classification_report,
    precision_recall_fscore_support,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "creditcard.csv"
ART = ROOT / "artifacts"
ART.mkdir(parents=True, exist_ok=True)
DATA.parent.mkdir(parents=True, exist_ok=True)


def load_data() -> tuple[pd.DataFrame, pd.Series]:
    if DATA.exists():
        print(f"Loading cached data from {DATA}")
        df = pd.read_csv(DATA)
    else:
        print("Downloading OpenML creditcard dataset (first run only)…")
        bunch = fetch_openml("creditcard", version=1, as_frame=True, parser="auto")
        df = bunch.frame
        df.to_csv(DATA, index=False)
        print(f"Cached → {DATA}")

    y = df["Class"].astype(int)
    X = df.drop(columns=["Class"])
    # Time is an ordering column — drop for the simple Week-1 baseline
    # (Week 4: revisit with time-aware splits.)
    if "Time" in X.columns:
        X = X.drop(columns=["Time"])
    return X, y


def eval_model(name: str, model, X_test, y_test) -> dict:
    proba = model.predict_proba(X_test)[:, 1]
    pred = (proba >= 0.5).astype(int)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, pred, average="binary", zero_division=0
    )
    metrics = {
        "model": name,
        "precision@0.5": round(precision, 4),
        "recall@0.5": round(recall, 4),
        "f1@0.5": round(f1, 4),
        "roc_auc": round(roc_auc_score(y_test, proba), 4),
        "pr_auc": round(average_precision_score(y_test, proba), 4),
    }
    print(f"\n=== {name} ===")
    print(classification_report(y_test, pred, digits=4, zero_division=0))
    print(
        f"ROC-AUC={metrics['roc_auc']}  PR-AUC={metrics['pr_auc']}  "
        f"(PR-AUC is the one to trust under imbalance)"
    )
    return metrics, proba


def main() -> None:
    X, y = load_data()
    print("\nClass balance:")
    print(y.value_counts(normalize=True).rename({0: "legit", 1: "fraud"}))
    print(y.value_counts().rename({0: "legit", 1: "fraud"}))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\nTrain={len(X_train):,}  Test={len(X_test):,}")

    models = {
        "logistic": make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42),
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=100,
            max_depth=12,
            class_weight="balanced_subsample",
            n_jobs=-1,
            random_state=42,
        ),
    }

    rows = []
    fig, ax = plt.subplots(figsize=(7, 5))
    for name, model in models.items():
        print(f"\nTraining {name}…")
        model.fit(X_train, y_train)
        metrics, proba = eval_model(name, model, X_test, y_test)
        rows.append(metrics)
        PrecisionRecallDisplay.from_predictions(y_test, proba, name=name, ax=ax)

    ax.set_title("FraudWatch — Precision–Recall (Week 1 baselines)")
    ax.legend(loc="upper right")
    pr_path = ART / "pr_curve_week1.png"
    fig.tight_layout()
    fig.savefig(pr_path, dpi=140)
    print(f"\nSaved PR curve → {pr_path}")

    summary = pd.DataFrame(rows).sort_values("pr_auc", ascending=False)
    out_csv = ART / "metrics_week1.csv"
    summary.to_csv(out_csv, index=False)
    print("\nSummary (sorted by PR-AUC):")
    print(summary.to_string(index=False))
    print(f"\nSaved metrics → {out_csv}")
    print(
        "\nNext: write 5 lines in your build log — which model wins on PR-AUC and "
        "why accuracy would have lied to you."
    )


if __name__ == "__main__":
    main()
