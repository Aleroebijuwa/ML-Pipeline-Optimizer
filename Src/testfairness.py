import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from fairness import FairnessAnalyzer


df = pd.read_csv("data.csv")  



X = df.drop(columns=["target"])
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)



model = LogisticRegression()
model.fit(X_train, y_train)


analyzer = FairnessAnalyzer(
    model=model,
    X_train=X_train,
    X_test=X_test,
    y_test=y_test,
    sensitive_feature_name="age_group"  
)



results = analyzer.compute_bias_metrics("age_group")
print("\nBIAS RESULTS:", results)



analyzer.plot_fairness(results)


