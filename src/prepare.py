import sys
from pathlib import Path

import pandas as pd
from dvc.api import params_show
from sklearn.model_selection import train_test_split

PARAMS = params_show()["prepare"]


def main():
    print(f"{PARAMS=}")
    data_path = Path(sys.argv[1])
    print(f"Data file path: '{data_path}'")
    df = pd.read_csv(data_path, sep=",")
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=PARAMS["split"],
        random_state=PARAMS["seed"],
    )

    X_train_path = Path("./data/prepared/X_train.csv")
    y_train_path = Path("./data/prepared/y_train.csv")
    X_test_path = Path("./data/prepared/X_test.csv")
    y_test_path = Path("./data/prepared/y_test.csv")
    X_train_path.parent.mkdir(exist_ok=True)

    X_train.to_csv(X_train_path, index=False)
    y_train.to_csv(y_train_path, index=False)
    X_test.to_csv(X_test_path, index=False)
    y_test.to_csv(y_test_path, index=False)

    print(f"X_train saved to file: {X_train_path}")
    print(f"y_train saved to file: {y_train_path}")
    print(f"X_test saved to file: {X_test_path}")
    print(f"y_test saved to file: {y_test_path}")


if __name__ == "__main__":
    main()
