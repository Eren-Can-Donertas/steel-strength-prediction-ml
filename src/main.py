from pathlib import Path

from preprocess import process
from train import train_model
from evaluate import evaluate_model, save_results, plot_results


def main():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data"
    results_dir = base_dir / "results"

    datasets = [
        {
            "name": "carbon_steel",
            "path": data_dir / "steel_property_and_composition_data.csv"
        },
        {
            "name": "stainless_steel",
            "path": data_dir / "steel_property_and_composition_stainless_steel.csv"
        }
    ]

    target_column = "UTS (MPa)"
    processed_count = 0

    for dataset in datasets:
        dataset_name = dataset["name"]
        dataset_path = dataset["path"]

        print("\n" + "=" * 60)
        print(f"Processing: {dataset_name}")
        print(f"File: {dataset_path}")
        print("=" * 60)

        if not dataset_path.exists():
            print(f"File not found, skipped: {dataset_path}")
            continue

        X, y = process(dataset_path, target=target_column)
        model, X_test, y_test = train_model(X, y)
        y_pred = model.predict(X_test)

        dataset_output_dir = results_dir / dataset_name

        evaluate_model(y_test, y_pred, dataset_name=dataset_name)
        save_results(y_test, y_pred, output_dir=dataset_output_dir)
        plot_results(
            y_test,
            y_pred,
            output_dir=dataset_output_dir,
            dataset_name=dataset_name,
            target_name=target_column
        )

        processed_count += 1

    if processed_count == 0:
        raise FileNotFoundError(
            "No dataset was found. Put the CSV files inside the project's data folder."
        )


if __name__ == "__main__":
    main()