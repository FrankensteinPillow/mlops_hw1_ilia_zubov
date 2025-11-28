import json
import pickle
import sys
from pathlib import Path
from uuid import uuid4

import mlflow
import pandas as pd
from dvc.api import params_show
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

PARAMS = params_show()["train"]


mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Iris_Classification_Experiment")


def main():
    print(f"{PARAMS=}")

    X_train_path = Path(sys.argv[1]) / "X_train.csv"
    y_train_path = Path(sys.argv[1]) / "y_train.csv"
    X_test_path = Path(sys.argv[1]) / "X_test.csv"
    y_test_path = Path(sys.argv[1]) / "y_test.csv"

    # 1. Load dataset for train
    X_train = pd.read_csv(X_train_path, sep=",")
    y_train = pd.read_csv(y_train_path, sep=",")
    print(f"X_train loaded from file: {X_train_path}")
    print(f"y_train loaded from file: {y_train_path}")
    X_test = pd.read_csv(X_test_path, sep=",")
    y_test = pd.read_csv(y_test_path, sep=",")
    print(f"X_test loaded from file: {X_test_path}")
    print(f"y_test loaded to file: {y_test_path}")

    metrics = {}

    with mlflow.start_run(run_name=f"{uuid4()}"):
        mlflow.log_param("model", "DecisionTreeClassifier")
        # 2. Prepare model
        model = DecisionTreeClassifier(
            max_depth=PARAMS["max_depth"],
            min_samples_split=PARAMS["min_samples_split"],
            min_samples_leaf=PARAMS["min_samples_leaf"],
            random_state=PARAMS["seed"],
        )

        # 3. Train model
        model.fit(X_train, y_train)

        # 4. Save model as artifact
        result_file_path = Path(sys.argv[2])
        with open(result_file_path, "wb") as f:
            pickle.dump(model, f)

        # 5. Log model
        mlflow.log_artifact("model.pkl")

        # 6. Save metrics on train
        y_pred = model.predict(X_train)
        accuracy_train = accuracy_score(y_train, y_pred)
        metrics["accuracy_train"] = accuracy_train
        print(f"Accuracy score on train data is: {accuracy_train}")

        # 7. Save metrics on test
        y_pred_test = model.predict(X_test)
        accuracy_test = accuracy_score(y_test, y_pred_test)
        metrics["accuracy_test"] = accuracy_test
        print(f"Accuracy score on test data is: {accuracy_test}")

        # 8. Log and save metrics
        mlflow.log_metrics(metrics)
        metrics_file_path = Path("./metrics.json")
        with open(metrics_file_path, "w") as f:
            json.dump(metrics, f)
        print(f"Saved metrics to file: {metrics_file_path}")


if __name__ == "__main__":
    main()
