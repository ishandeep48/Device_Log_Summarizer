# AI Prompt Log – Section 3: Charting Challenge

## 1. Initial Prompt

Ok so we have a file `output.json` in the `outputs` folder in the current working directory.

Inside the `aggregated_data` key, there is a list of objects containing sensor data. Each object has a `device_id` and an `average_temperature`.

Write a Python script that reads this JSON file and creates a bar chart comparing the average temperature of all devices. Put temperature on the Y-axis and device IDs on the X-axis.

Do not add anything else.

## 2. Bug / Formatting Issue Identified

The initial AI-generated chart used a vertical bar chart. When multiple sensors were present, their names overlapped along the X-axis, making the chart difficult to read.

The chart also did not dynamically adjust its dimensions based on the number of sensors.

## 3. First Follow-up Prompt

The name of all the sensors are overlapped.

Instead of a vertical bar chart, switch to a horizontal bar chart for better visibility of sensor names.

Also make sure the chart scales cleanly so that even if we get like 50 sensors it stays readable.

## 4. Changes Made

The AI updated the script with the following changes:

- Replaced `plt.bar()` with `plt.barh()` to create a horizontal bar chart.
- Dynamically adjusted the chart height based on the number of devices using `figsize`.
- Added `plt.tight_layout()` to prevent labels from being cut off.

## 5. Second Follow-up Prompt

Perfect. Now add the exact number of the temperature value at the end of each bar for better readability.

## 6. Additional Changes Made

- Added `plt.text()` to display the temperature value at the end of each bar.
- Used `bar.get_width()` to position the temperature label horizontally.
- Used `bar.get_y()` and `bar.get_height()` to vertically centre the label.
- Formatted temperature values to display two decimal places followed by °C.

## 7. Final Result

Generated a horizontal bar chart comparing the average temperatures of all devices.

The final chart includes:

- Device IDs on the Y-axis.
- Average temperatures on the X-axis.
- Temperature values displayed at the end of each bar.
- Dynamically adjusted chart height for better readability with larger numbers of devices.