import pandas as pd

# Load the cleaned dataset
data = pd.read_csv("cleaned_air_quality.csv")

# Create new features from timestamp
data["timestamp"] = pd.to_datetime(data["timestamp"])

data["hour"] = data["timestamp"].dt.hour
data["day"] = data["timestamp"].dt.day
data["month"] = data["timestamp"].dt.month

# Create a weekend feature
data["weekend"] = (
    data["timestamp"].dt.dayofweek >= 5
).astype(int)

# Create a rush hour feature
data["rush_hour"] = data["hour"].isin(
    [7, 8, 9, 17, 18, 19]
).astype(int)

# Convert season into numerical columns
if "season" in data.columns:
    data = pd.get_dummies(
        data, columns=["season"], dtype=int
    )

# Select numerical columns for analysis
numeric_data = data.select_dtypes(include="number")

# Find correlation with AQI
correlation = numeric_data.corr()["AQI"].abs()
correlation = correlation.sort_values(ascending=False)

print("Features most related to AQI:")
print(correlation)

# Select features with correlation above 0.1
selected_features = correlation[correlation > 0.1].index.tolist()

print("\nSelected features:")
print(selected_features)

data.to_csv("final_air_quality.csv", index=False)
print("\nFeature engineering completed!")
print("Final dataset shape:", data.shape)
