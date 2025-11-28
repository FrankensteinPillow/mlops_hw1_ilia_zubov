import pickle
import sys
from pathlib import Path

import mlflow
import pandas as pd
from dvc.api import params_show
from sklearn.tree import DecisionTreeClassifier

PARAMS = params_show()["train"]


def main():
    mlflow.log_param("model", "DecisionTreeClassifier")
    X_train_path = Path(sys.argv[1]) / "X_train.csv"
    y_train_path = Path(sys.argv[1]) / "y_train.csv"

    # 1. Load dataset for train
    X_train = pd.read_csv(X_train_path, sep=",")
    y_train = pd.read_csv(y_train_path, sep=",")
    print(f"X_train loaded from file: {X_train_path}")
    print(f"y_train loaded from file: {y_train_path}")

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


if __name__ == "__main__":
    main()
