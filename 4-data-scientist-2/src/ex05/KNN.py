import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


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

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Standardize features for KNN (z-score normalization)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_valid_scaled = scaler.transform(X_valid)

    # Evaluate KNN across k values from 1 to 31
    k_range = range(1, 32)
    accuracies = []
    best_k = 1
    best_accuracy = 0.0
    best_model = None

    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        preds = knn.predict(X_valid_scaled)
        acc = accuracy_score(y_valid, preds)
        accuracies.append(acc)

        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k
            best_model = knn

    # Print evaluation for the best model found
    best_preds = best_model.predict(X_valid_scaled)
    print(classification_report(y_valid, best_preds,
                                target_names=knight_code.keys())
    )

    plt.figure(figsize=(8, 5))
    plt.plot(k_range, accuracies)
    plt.xlabel("k values")
    plt.ylabel("accuracy")
    plt.grid(True)
    plt.savefig("knn_accuracy.svg")

    # ----- Test -----
    X_test = df_test
    X_test_scaled = scaler.transform(X_test)

    test_preds = best_model.predict(X_test_scaled)
    knight_rcode = {0: "Sith", 1: "Jedi"}
    test_preds_str = [knight_rcode[pred] for pred in test_preds]

    with open("KNN.txt", "w") as f:
        f.write("\n".join(test_preds_str))


if __name__ == "__main__":
    main()