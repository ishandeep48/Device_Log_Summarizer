# Device Telemetry Analyzer

A Python project for processing device telemetry data and visualizing temperature statistics.

## Section 2 – Data Processing
- Reads telemetry data from CSV files.
- Validates required columns.
- Handles missing and invalid values.
- Normalizes device statuses.
- Groups records by device ID.
- Calculates total records, average temperature, and ERROR count.
- Filters devices with average temperatures above 80°C.
- Exports aggregated results to JSON.
- Reports skipped and invalid devices.

## Section 3 – Data Visualization
- Reads aggregated data from JSON.
- Generates a horizontal bar chart comparing device temperatures.
- Dynamically adjusts chart height based on the number of devices.
- Displays exact temperature values at the end of each bar.

## Technologies Used
- Python
- Pandas
- Matplotlib
- JSON

## Execution Order
1. Run Section 2 to generate `output.json`.
2. Run Section 3 to generate the temperature chart.

## How to run
1. Put the csv in the inputs folder
2. Run this command
```
python data_processing.py
```
and write the name of the file that you just copied to the inputs directory

At this point a json will be created in the outputs folder . if there is already one theen it will be overwritten

4. Run this command for bar chart
```
python chart.py
```

You will get a bar chart now

See `PROMPT_LOG.md` for AI prompting and chart improvement details.