
import pandas as pd

# Load the datasets
air = pd.read_csv("air_quality.csv")
stations = pd.read_csv("stations.csv")
weather = pd.read_csv("weather.csv")
traffic = pd.read_csv("traffic.csv")
calendar = pd.read_csv("calendar.csv")

# Convert timestamp columns to date and time
air["timestamp"] = pd.to_datetime(air["timestamp"])
weather["timestamp"] = pd.to_datetime(weather["timestamp"])
traffic["timestamp"] = pd.to_datetime(traffic["timestamp"])
calendar["timestamp"] = pd.to_datetime(calendar["timestamp"])

# Check missing values
print("Missing values before cleaning:")
print(air.isnull().sum())

# Fix station names
air["station"] = air["station"].str.strip().str.lower()
stations["station"] = stations["station"].str.strip().str.lower()
traffic["station"] = traffic["station"].str.strip().str.lower()

# Replace inconsistent station names
air["station"] = air["station"].replace({
    "central traffic": "central_traffic",
    "industrial east": "industrial_east",
    "market square": "market_square"
})

# Remove duplicate air-quality records
air = air.drop_duplicates(subset=["timestamp", "station"])

# Remove unrealistic sensor readings
air.loc[air["PM2.5"] > 500, "PM2.5"] = None
air.loc[air["PM10"] > 600, "PM10"] = None
air.loc[air["NO2"] > 200, "NO2"] = None
air.loc[air["AQI"] > 500, "AQI"] = None

# Fill missing pollution values with column averages
for col in ["PM2.5", "PM10", "NO2", "AQI"]:
    air[col] = air[col].fillna(air[col].mean())

# Fill missing weather values with column averages
for col in ["wind", "temperature", "humidity", "rain"]:
    weather[col] = weather[col].fillna(weather[col].mean())

# Remove duplicate weather and calendar records
weather = weather.drop_duplicates(subset=["timestamp"])
calendar = calendar.drop_duplicates(subset=["timestamp"])

# Combine the datasets
data = pd.merge(air, stations, on="station", how="left")
data = pd.merge(data, weather, on="timestamp", how="left")
data = pd.merge(data, traffic, on=["timestamp", "station"], how="left")
data = pd.merge(data, calendar, on="timestamp", how="left")

# Create new time-based features
data["hour"] = data["timestamp"].dt.hour
data["month"] = data["timestamp"].dt.month
data["day"] = data["timestamp"].dt.day

# Create a rush-hour feature
data["rush_hour"] = data["hour"].isin(
    [7, 8, 9, 17, 18, 19]
).astype(int)

# Encode land-use type
data = pd.get_dummies(data, columns=["land_use_type"], dtype=int)

# Save the cleaned dataset
data.to_csv("cleaned_air_quality.csv", index=False)

# Display the results
print("\nCleaning completed!")
print("Dataset shape:", data.shape)
print("\nMissing values after cleaning:")
print(data.isnull().sum())
print("\nFirst five rows:")
print(data.head())
