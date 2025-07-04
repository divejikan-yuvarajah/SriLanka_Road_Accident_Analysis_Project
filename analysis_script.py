import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("road_accidents_srilanka.csv")

# --------------------------------------------
# Preprocessing
# --------------------------------------------

# Convert time to hour (assumes time column in format '%H:%M')
df['hour'] = pd.to_datetime(df['time'], format='%H:%M').dt.hour

# Convert 'date' column to datetime if available (needed for weekday analysis)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_week'] = df['date'].dt.day_name()

# Create new column to flag fatal accidents
df['is_fatal'] = df['fatalities'] > 0

# --------------------------------------------
# 1. District-wise Accident Count
# --------------------------------------------
district_counts = df['district'].value_counts()
district_counts.plot(kind='bar', title='Accidents per District', color='orange')
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("District_Accidents.png")
plt.close()

# --------------------------------------------
# 2. Hourly Accident Distribution
# --------------------------------------------
sns.histplot(df['hour'], bins=24, kde=True)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Hourly_Accidents.png")
plt.close()

# --------------------------------------------
# 3. Weather-wise Accident Count
# --------------------------------------------
sns.countplot(x="weather", data=df)
plt.title("Accidents by Weather Condition")
plt.tight_layout()
plt.savefig("Weather_Accidents.png")
plt.close()

# --------------------------------------------
# 4. Severity-wise Statistics (Fatalities and Injuries)
# --------------------------------------------
severity_group = df.groupby('severity')[['fatalities', 'injuries']].sum()
print("Severity-wise statistics:\n", severity_group)

# --------------------------------------------
# Additional Analysis Options
# --------------------------------------------

# 5. Top 10 Accident-Prone Locations (if 'location' column exists)
if 'location' in df.columns:
    top_locations = df['location'].value_counts().head(10)
    top_locations.plot(kind='barh', color='crimson')
    plt.title("Top 10 Accident-Prone Locations")
    plt.xlabel("Number of Accidents")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.savefig("Top_Locations.png")
    plt.close()

# 6. Accidents by Day of the Week (if 'date' exists)
if 'day_of_week' in df.columns:
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sns.countplot(x='day_of_week', data=df, order=order, palette='magma')
    plt.title("Accidents by Day of Week")
    plt.xlabel("Day")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Day_of_Week_Accidents.png")
    plt.close()

# 7. Accidents by Vehicle Type (if 'vehicle_type' column exists)
if 'vehicle_type' in df.columns:
    sns.countplot(x='vehicle_type', data=df, order=df['vehicle_type'].value_counts().index, palette='Set2')
    plt.title("Accidents by Vehicle Type")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Vehicle_Type_Accidents.png")
    plt.close()

# 8. Correlation Heatmap (Numeric columns only)
numeric_df = df.select_dtypes(include=['number'])
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.savefig("Correlation_Heatmap.png")
plt.close()

# 9. Pie Chart of Accident Severity
severity_counts = df['severity'].value_counts()
plt.figure()
plt.pie(severity_counts, labels=severity_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Accident Severity Distribution")
plt.tight_layout()
plt.savefig("Severity_Pie.png")
plt.close()

# 10. Fatal vs Non-Fatal Accidents by District
district_fatal = df.groupby('district')['is_fatal'].value_counts().unstack().fillna(0)
district_fatal.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'])
plt.title("Fatal vs Non-Fatal Accidents by District")
plt.xlabel("District")
plt.ylabel("Number of Accidents")
plt.legend(['Non-Fatal', 'Fatal'])
plt.tight_layout()
plt.savefig("Fatal_vs_Nonfatal_District.png")
plt.close()

print("All graphs have been saved successfully.")
