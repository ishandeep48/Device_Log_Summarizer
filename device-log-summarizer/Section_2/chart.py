
import json
import matplotlib.pyplot as plt


def main():
    # Open JSON file
    with open("./outputs/output.json", "r") as file:
        data = json.load(file)

    # Extract device IDs and average temperatures
    devices = [item["device_id"] for item in data["aggregated_data"]]
    temperatures = [
        item["average_temperature"]
        for item in data["aggregated_data"]
    ]

    # Dynamically adjust chart height
    chart_height = max(5, len(devices) * 0.4)

    plt.figure(figsize=(10, chart_height))

    # Create horizontal bar chart
    bars = plt.barh(devices, temperatures)

    # Add temperature values at the end of each bar
    for bar, temperature in zip(bars, temperatures):
        plt.text(
            bar.get_width() + 0.5,
            bar.get_y() + bar.get_height() / 2,
            f"{temperature:.2f}",
            va="center"
        )

    # Add labels and title
    plt.xlabel("Average Temperature (°C)")
    plt.ylabel("Device ID")
    plt.title("Average Temperature per Device")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
