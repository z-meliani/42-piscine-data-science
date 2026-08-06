# Piscine Data Science - Data Scientist 1

The `Data Scientist part 2` project explores basic supervised classification models, data preprocessing (PCA, VIF feature selection), hyperparameter tuning, performance evaluation metrics, and ensemble methods like Voting Classifiers.


## 🏗️ Project Architecture

```bash
.
├── .venv/
├── data/
│   ├── predictions.txt
│   ├── Test_knight.csv
│   ├── Train_knight.csv
│   └── truth.txt
├── src/
│   ├── ex00
│   ...
│   └── ex06
├── config.sh
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## ⚙️ Setup

**<ins>Option 1:</ins>** Using `uv`
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies from pyproject.toml
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

**<ins>Option 2:</ins>** Using `pip` and `venv`:
```bash
./config.sh
```

## ▶️ How to run
```bash

# Activate the virtual environment
source ./venv/bin/activate

# Open the notebooks interface
jupyter-lab
```