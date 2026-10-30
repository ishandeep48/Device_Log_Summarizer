
import pandas as pd
import json


def main():
    # 1. Load CSV
    file_name= input("What is the name of the file you want to analyse : ").strip()
    if not file_name.lower().endswith(".csv"):
        file_name += ".csv"
        
    try:
        df = pd.read_csv(f"./inputs/{file_name}")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        return

    # 2. Validate required columns
    required_columns = {"device_id", "status", "temperature"}

    if not required_columns.issubset(df.columns):
        print("Error: CSV is missing required columns.")
        return

    # Handle CSV containing only headers and no records
    if df.empty:
        print("Error: CSV contains no records.")
        return

    # 3. Clean device IDs
    df["device_id"] = df["device_id"].astype("string").str.strip()

    # Remove missing and blank device IDs
    df = df.dropna(subset=["device_id"])
    df = df[df["device_id"] != ""]

    # 4. Normalize status values
    df["status"] = df["status"].astype("string").str.strip().str.upper()

    # 5. Convert temperatures to numeric values
    df["temperature"] = pd.to_numeric(
        df["temperature"], errors="coerce"
    )

    # Treat infinite temperatures as invalid
    df.loc[~df["temperature"].between(float("-inf"), float("inf")), "temperature"] = float("nan")

    # 6. Aggregate data by device
    summary = df.groupby("device_id").agg(
        total_records=("device_id", "count"),
        average_temperature=("temperature", "mean"),
        error_count=("status", lambda x: (x == "ERROR").sum())
    )

    # 7. Identify devices with no valid temperature readings
    invalid_temperature_devices = int(
        summary["average_temperature"].isna().sum()
    )

    summary = summary.dropna(subset=["average_temperature"])

    # 8. Count devices exceeding 80°C
    devices_skipped = int(
        (summary["average_temperature"] > 80.0).sum()
    )

    # 9. Filter devices with average temperature <= 80°C
    summary = summary[summary["average_temperature"] <= 80.0]

    # 10. Round averages to 2 decimal places
    summary["average_temperature"] = (
        summary["average_temperature"].round(2)
    )

    # 11. Convert results into JSON-friendly records
    aggregated_data = summary.reset_index().to_dict(orient="records")

    output = {
        "aggregated_data": aggregated_data,
        "devices_skipped": devices_skipped,
        "devices_invalid": invalid_temperature_devices
    }

    # 12. Export JSON
    with open("outputs/output.json", "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4, allow_nan=False)

    # 13. Print terminal summary
    print("\n========== DEVICE SUMMARY ==========")

    if summary.empty:
        print("No devices passed the temperature filter.")
    else:
        print(summary.reset_index().to_string(index=False))

    print("\n========== PROCESSING SUMMARY ==========")
    print(f"Devices retained: {len(summary)}")
    print(f"Devices skipped (>80°C): {devices_skipped}")
    print(f"Devices invalid (no valid temperatures): {invalid_temperature_devices}")
    print(f"Total devices processed: {len(summary) + devices_skipped + invalid_temperature_devices}")

    print("\nResults exported to output.json")


if __name__ == "__main__":
    main()
