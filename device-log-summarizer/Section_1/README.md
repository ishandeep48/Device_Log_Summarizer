# Sensor Readings Sanitizer

A Python utility that cleans and normalizes mixed sensor readings.

## Features
- Converts valid values to floats.
- Removes invalid, null, and negative values.
- Removes NaN values.
- Caps values above 500.0.
- Handles positive and negative infinity.

## Run Doctest

```
python -m doctest -v sanitizer.py
```

## Test with you custom inputs

 Run this command 
 ```
 python test_sanitizer.py
 ```

 Then input the your sensor reading list with each value seperated by a comma 