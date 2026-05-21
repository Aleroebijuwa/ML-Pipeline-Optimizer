import asyncio
import time

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from async_pipeline import load_csv_async, train_model_async



def timer(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        print(f"\n⏱ Total pipeline time: {end - start:.2f} seconds")
        return result
    return wrapper



@timer
async def run_pipeline():

    print("\n🚀 STARTING ML PIPELINE\n")

  
    df = await load_csv_async("data.csv")

    print("[DATA LOADED]")

   
    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

   
    tasks = [
        train_model_async(
            LogisticRegression(),
            X_train,
            y_train,
            "Logistic Regression"
        ),
        train_model_async(
            DecisionTreeClassifier(),
            X_train,
            y_train,
            "Decision Tree"
        )
    ]

    trained_models = await asyncio.gather(*tasks)

   
    print("\n✅ PIPELINE COMPLETE")
    print(f"Trained Models: {len(trained_models)}")

    return trained_models



if __name__ == "__main__":
    asyncio.run(run_pipeline())