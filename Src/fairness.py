import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import shap
from lime.lime_tabular import LimeTabularExplainer



class FairnessAnalyzer:

    def __init__(self, model, X_train, X_test, y_test, sensitive_feature_name):
        self.model = model
        self.X_train = X_train
        self.X_test = X_test
        self.y_test = y_test
        self.sensitive_feature_name = sensitive_feature_name


   
    def compute_bias_metrics(self, sensitive_column):
        """
        Compare prediction rates across groups.
        """

        df = self.X_test.copy()
        df["y_true"] = self.y_test
        df["y_pred"] = self.model.predict(self.X_test)

        groups = df[sensitive_column].unique()

        results = {}

        for g in groups:
            group_data = df[df[sensitive_column] == g]

            accuracy = (group_data["y_pred"] == group_data["y_true"]).mean()
            positive_rate = group_data["y_pred"].mean()

            results[g] = {
                "accuracy": accuracy,
                "positive_rate": positive_rate
            }

        return results


   
    def shap_explain(self):

        explainer = shap.Explainer(self.model, self.X_train)
        shap_values = explainer(self.X_test)

        shap.summary_plot(shap_values, self.X_test)


  
    def lime_explain(self, instance_index=0):

        explainer = LimeTabularExplainer(
            training_data=np.array(self.X_train),
            feature_names=self.X_train.columns,
            class_names=["0", "1"],
            mode="classification"
        )

        exp = explainer.explain_instance(
            data_row=self.X_test.iloc[instance_index],
            predict_fn=self.model.predict_proba
        )

        exp.show_in_notebook(show_table=True)


    
    def plot_fairness(self, bias_results):

        groups = list(bias_results.keys())
        accuracy = [bias_results[g]["accuracy"] for g in groups]
        positive_rate = [bias_results[g]["positive_rate"] for g in groups]

        x = np.arange(len(groups))

        plt.figure(figsize=(10, 5))

        plt.bar(x - 0.2, accuracy, width=0.4, label="Accuracy")
        plt.bar(x + 0.2, positive_rate, width=0.4, label="Positive Rate")

        plt.xticks(x, groups)
        plt.title("Fairness Metrics Across Groups")
        plt.legend()

        plt.show()