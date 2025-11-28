import json
import pickle
import sys
from pathlib import Path

import mlflow
import pandas as pd
from sklearn.metrics import accuracy_score


def main():
    model_file_path = Path(sys.argv[2])
    X_test_path = Path(sys.argv[1]) / "X_test.csv"
    y_test_path = Path(sys.argv[1]) / "y_test.csv"

    # 1. Load test data
    X_test = pd.read_csv(X_test_path, sep=",")
    y_test = pd.read_csv(y_test_path, sep=",")
    print(f"X_test loaded from file: {X_test_path}")
    print(f"y_test loaded to file: {y_test_path}")

    # 2. Load model
    with open(model_file_path, "rb") as f:
        model = pickle.load(f)

    # 3. Model predict on test data
    y_pred = model.predict(X_test)

    # 4. Get metrics (accuracy)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy score on test data is: {accuracy}")

    # 5. Save metrics to file
    metrics_file_path = Path("./metrics.json")
    with open(metrics_file_path, "w") as f:
        json.dump({"accuracy": accuracy}, f)
    print(f"Saved metrics to file: {metrics_file_path}")

    # 6. Log metrics
    mlflow.log_metrics("accuracy", accuracy)


if __name__ == "__main__":
    main()
