import matplotlib.pyplot as plt
import numpy as np
import sys

class ConfusionMatrix:
    def __init__(self, truth: list, pred: list):
        if len(truth) != len(pred):
            raise ValueError("truth and pred must have the same length.")

        self.labels = sorted(list(set(truth) | set(pred)))
        self.label_idx = {label: i for i, label in enumerate(self.labels)}
        self.total = len(truth)

        # 1. Build the matrix in one place
        self.matrix = np.zeros((len(self.labels), len(self.labels)), dtype=int)
        for t, p in zip(truth, pred):
            self.matrix[self.label_idx[t], self.label_idx[p]] += 1

    def precision(self, target) -> float:
        """Calculates precision for a specific class."""
        i = self.label_idx[target]
        tp = self.matrix[i, i]
        fp = np.sum(self.matrix[:, i]) - tp
        return tp / (tp + fp) if (tp + fp) > 0 else 0.0

    def recall(self, target) -> float:
        """Calculates recall (sensitivity) for a specific class."""
        i = self.label_idx[target]
        tp = self.matrix[i, i]
        fn = np.sum(self.matrix[i, :]) - tp
        return tp / (tp + fn) if (tp + fn) > 0 else 0.0

    def f1_score(self, target) -> float:
        """Calculates F1-score for a specific class."""
        prec = self.precision(target)
        rec = self.recall(target)
        return 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

    def accuracy(self) -> float:
        """Calculates overall model accuracy."""
        return np.trace(self.matrix) / self.total if self.total > 0 else 0.0

    def get_metrics(self, target) -> tuple[float, float, float]:
        """Returns (precision, recall, f1_score) for a specific target class."""
        return self.precision(target), self.recall(target), self.f1_score(target)

    def __call__(self, target) -> tuple[float, float, float]:
        """Allows direct call: cm(target) -> (precision, recall, f1_score)."""
        return self.get_metrics(target)

    def __str__(self) -> str:
        """Prints a scikit-learn style classification report and grid."""
        output = f"{'':<15}{'precision':<12}{'recall':<12}{'f1-score':<12}{'total':<12}\n\n"

        for label in self.labels:
            i = self.label_idx[label]
            prec, rec, f1 = self.get_metrics(label)
            support = np.sum(self.matrix[i, :])
            output += f"{label:<15}{prec:<12.2f}{rec:<12.2f}{f1:<12.2f}{support:<12}\n"

        output += f"\n{'accuracy':<15}{'':<12}{'':<12}{self.accuracy():<12.2f}{self.total:<12}\n"
        output += f"\n{self.matrix}"
        return output



def main():

    try:
        if len(sys.argv) != 3:
            raise ValueError("Invalid number of arguments.")

        # Read files and append to lists
        predictions = []
        with open(sys.argv[1], "r") as f:
            for line in f:
                predictions.append(line.strip())

        truth = []
        with open(sys.argv[2], "r") as f:
            for line in f:
                truth.append(line.strip())
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


    cm = ConfusionMatrix(truth, predictions)

    print(f"{cm}")

    fig, ax = plt.subplots()

    im = ax.imshow(cm.matrix)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    fig.colorbar(im, ax=ax)

    for i in range(cm.matrix.shape[0]):
        for j in range(cm.matrix.shape[1]):
            color = "black" if cm.matrix[i, j] == cm.matrix.max() else "white"
            ax.text(j, i, f"{cm.matrix[i, j]}",
                    ha="center", va="center", fontsize=15, color=color)

    fig.savefig("confusion_matrix.jpg")

    return 0


if __name__ == "__main__":
    main()