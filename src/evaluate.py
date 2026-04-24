import os
import pandas as pd
import matplotlib.pyplot as plt

from metrics_helper import calculate_metrics, print_metrics


def evaluate_model(y_true, y_pred, dataset_name="dataset"):
    print(f"\nEvaluation for: {dataset_name}")
    metrics = calculate_metrics(y_true, y_pred)
    print_metrics(metrics)
    return metrics


def save_results(y_true, y_pred, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    results_df = pd.DataFrame({
        "Actual": y_true,
        "Predicted": y_pred
    })

    results_path = os.path.join(output_dir, "predictions.csv")
    results_df.to_csv(results_path, index=False)

    print(f"Results saved to: {results_path}")


def plot_results(y_true, y_pred, output_dir, dataset_name="dataset", target_name="UTS (MPa)"):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred)
    plt.xlabel(f"Actual {target_name}")
    plt.ylabel(f"Predicted {target_name}")
    plt.title(f"Actual vs Predicted {target_name} - {dataset_name}")
    plt.grid(True)

    plot_path = os.path.join(output_dir, "predicted_vs_actual.png")
    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Plot saved to: {plot_path}")