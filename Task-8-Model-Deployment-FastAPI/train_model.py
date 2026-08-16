"""
train_model.py
----------------
Trains a classifier on the sklearn Breast Cancer Wisconsin dataset and
saves the fitted pipeline (scaler + model) to disk for the FastAPI
service to load at startup.

Using a built-in sklearn dataset avoids any download/path dependency,
consistent with earlier tasks in this internship.
"""

from pathlib import Path
import json

import joblib
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------------------
# Config / constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "model.joblib"
METADATA_PATH = PROJECT_ROOT / "model_metadata.json"
RANDOM_STATE = 42
TEST_SIZE = 0.2


def load_data():
    """Load the Breast Cancer Wisconsin dataset (sklearn built-in)."""
    data = load_breast_cancer()
    X, y = data.data, data.target
    feature_names = list(data.feature_names)
    target_names = list(data.target_names)
    return X, y, feature_names, target_names


def build_pipeline():
    """Build a scaler + classifier pipeline."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200, random_state=RANDOM_STATE
                ),
            ),
        ]
    )


def train_model(X, y):
    """Split data, fit the pipeline, and return the fitted model plus test metrics."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    return pipeline, acc, report


def validate_pipeline(pipeline, feature_names):
    """Post-training sanity checks before saving the model."""
    n_features_expected = len(feature_names)
    assert pipeline.named_steps["classifier"].n_features_in_ == n_features_expected, (
        "Trained model feature count does not match dataset feature count."
    )
    # Confirm predict_proba is available (needed for confidence scores in the API)
    assert hasattr(pipeline, "predict_proba"), "Model must support predict_proba."
    print(f"Validation passed: model expects {n_features_expected} features.")


def save_artifacts(pipeline, feature_names, target_names, accuracy):
    """Persist the fitted pipeline and its metadata to disk."""
    joblib.dump(pipeline, MODEL_PATH)

    metadata = {
        "feature_names": feature_names,
        "target_names": target_names,
        "n_features": len(feature_names),
        "test_accuracy": accuracy,
        "model_type": "RandomForestClassifier",
        "random_state": RANDOM_STATE,
    }
    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Saved model to: {MODEL_PATH}")
    print(f"Saved metadata to: {METADATA_PATH}")


def main():
    X, y, feature_names, target_names = load_data()
    pipeline, accuracy, report = train_model(X, y)
    validate_pipeline(pipeline, feature_names)
    save_artifacts(pipeline, feature_names, target_names, accuracy)

    print(f"\nTest accuracy: {accuracy:.4f}")
    print(f"Macro F1: {report['macro avg']['f1-score']:.4f}")


if __name__ == "__main__":
    main()
