import asyncio
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


# -----------------------------
# 📊 ASYNC CSV LOADER
# -----------------------------
async def load_csv_async(file_path):
    df = await asyncio.to_thread(pd.read_csv, file_path)
    return df


# -----------------------------
# 🧠 ASYNC TRAINER
# -----------------------------
async def train_model_async(model, X, y, name="model"):
    print(f"[START] {name}")
    await asyncio.to_thread(model.fit, X, y)
    print(f"[DONE] {name}")
    return model


# -----------------------------
# 🚀 PIPELINE RUNNER
# -----------------------------
async def run_pipeline():
    df = await load_csv_async("data.csv")

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    models = {
        "log_reg": LogisticRegression(),
        "tree": DecisionTreeClassifier()
    }

    tasks = [
        train_model_async(model, X, y, name=name)
        for name, model in models.items()
    ]

    results = await asyncio.gather(*tasks)
    return results