SYNTHETIC AIR QUALITY INSIGHT DATASET
======================================
Purpose
-------
Created for U23AD491 Data Science - DS Sprint Skill Based Assessment 2,
Use Case 20: Air Quality Insight. All records are synthetic and are not
measurements from a real city or monitoring network.

Files
-----
air_quality.csv : timestamp + station level air quality (PM2.5, PM10, NO2, AQI)
stations.csv    : station metadata (location and land-use type)
weather.csv     : timestamp-level weather (wind, temperature, humidity, rain)
traffic.csv     : timestamp + station level traffic volume and peak flag
calendar.csv    : timestamp-level weekday, holiday and season fields

Coverage
--------
Hourly data from 2026-01-01 00:00 through 2026-02-14 23:00 inclusive.
Six synthetic monitoring stations.

Intentional data-quality issues in raw files
--------------------------------------------
- Missing sensor readings in air_quality.csv
- Missing wind/humidity values in weather.csv
- A small number of inconsistent station names in air_quality.csv
- A small number of extreme sensor values in air_quality.csv
- Duplicate air_quality timestamp/station records

Suggested cleaning workflow
---------------------------
1. Parse timestamp columns as datetime.
2. Standardize station names (case, spaces, underscores) and map aliases.
3. Investigate duplicates on [timestamp, station]; choose a documented rule.
4. Investigate extreme values using domain checks and IQR/z-score; do not
   delete automatically without documenting the decision.
5. Impute or otherwise handle missing values with a justified method.
6. Merge air_quality with stations on station; traffic on timestamp + station;
   weather and calendar on timestamp.
7. Validate row counts and join coverage after merging.

Important
---------
This dataset is deliberately synthetic and contains injected quality issues
for practice. Do not describe its patterns as real-world measured evidence.
