import sys
import pandas as pd
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def main():
    try:
        df_train = pd.read_csv(sys.argv[1])
        df_test = pd.read_csv(sys.argv[2])
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # ----- Training and validation -----
    knight_code = {"Sith": 0, "Jedi": 1}
    y = df_train["knight"].map(knight_code)
    X = df_train.drop(columns=["knight"])

    # 2. Train / Validation Split
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Define Base Estimators
    # Note: Wrap distance/scale-sensitive models (KNN, Logistic) in Pipelines!
    knn_pipeline = Pipeline(
        [("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=7))]
    )

    log_pipeline = Pipeline(
        [("scaler", StandardScaler()), ("log_reg", LogisticRegression())]
    )

    dt_model = DecisionTreeClassifier(max_depth=2, random_state=42)

    voting_clf = VotingClassifier(
        estimators=[
            ("knn", knn_pipeline),
            ("log_reg", log_pipeline),
            ("dt", dt_model),
        ],
        voting="soft"
    )
    voting_clf.fit(X_train, y_train)

    valid_preds = voting_clf.predict(X_valid)
    print(classification_report(y_valid, valid_preds,
                              target_names=knight_code.keys())
    )

    # ----- Test -----
    X_test = df_test
    test_preds = voting_clf.predict(X_test)

    knight_rcode = {0: "Sith", 1: "Jedi"}
    test_preds_str = [knight_rcode[pred] for pred in test_preds]

    with open("Voting.txt", "w") as f:
        f.write("\n".join(test_preds_str))


if __name__ == "__main__":
    main()