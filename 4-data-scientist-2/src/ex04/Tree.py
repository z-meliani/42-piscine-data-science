import matplotlib.pyplot as plt
import pandas as pd
import sys
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():
    try:
        df_train = pd.read_csv(sys.argv[1])
        df_test = pd.read_csv(sys.argv[2])
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # ----- Training and validation -----
    knight_code = {'Sith': 0, 'Jedi': 1}
    y = df_train["knight"].map(knight_code)
    X = df_train.drop(columns=["knight"])

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42)

    dt_model = DecisionTreeClassifier(max_depth=2, random_state=42)
    dt_model.fit(X_train, y_train)
    dt_preds = dt_model.predict(X_valid)

    cr = classification_report(y_valid, dt_preds, target_names=knight_code.keys())
    print(cr)

    plt.figure()
    plot_tree(dt_model, feature_names=X.columns, proportion=True,
              class_names=list(knight_code.keys()), filled=True)
    plt.savefig("decision_tree.svg")

    # ----- Test -----
    test_preds = dt_model.predict(df_test)
    knight_rcode = {0: "Sith", 1: "Jedi"}
    test_preds_str = [knight_rcode[pred] for pred in test_preds]
    with open("Tree.txt", "w") as f:
            f.write("\n".join(test_preds_str))

if __name__ == "__main__":
    main()