import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# List of years to analyze
years = [2020, 2021, 2022, 2023, 2024]

# Initialize lists to store average weekday and weekend demand for each year
weekday_demand = []
weekend_demand = []
year_labels = []

# Loop through each year and calculate average demand for weekdays and weekends
for year in years:
    # Read the data for the current year
    df = pd.read_excel(file_path, sheet_name=str(year))
    
    # Ensure the 'Date' column is in datetime format and the necessary columns are numeric
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
    df['Load (MW)'] = pd.to_numeric(df['Load (MW)'], errors='coerce')

    # Extract the day of the week (0=Monday, 6=Sunday)
    df['Day of Week'] = df['Date'].dt.dayofweek

    # Define weekdays and weekends
    # Weekdays: Monday to Friday (0-4), Weekends: Saturday and Sunday (5-6)
    df['Weekend/Weekday'] = df['Day of Week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

    # Calculate the average load for weekdays and weekends
    avg_load = df.groupby('Weekend/Weekday')['Load (MW)'].mean()
    
    # Store the average load values and the year label
    weekday_demand.append(avg_load['Weekday'])
    weekend_demand.append(avg_load['Weekend'])
    year_labels.append(str(year))

# Set the positions of the bars on the x-axis
x = range(len(years))

# Plotting the data for all years
plt.figure(figsize=(10, 6))

# Bar plot for weekdays and weekends across all years
bar_width = 0.35  # Width of the bars
plt.bar(x, weekday_demand, width=bar_width, color='blue', label='Weekday Demand', alpha=0.7)
plt.bar([i + bar_width for i in x], weekend_demand, width=bar_width, color='green', label='Weekend Demand', alpha=0.7)

# Adding labels and title
plt.title('Average Electricity Demand: Weekdays vs Weekends (2020-2024)')
plt.xlabel('Year')
plt.ylabel('Average Load (MW)')
plt.xticks([i + bar_width / 2 for i in x], year_labels)  # Adjust x-ticks to align with the bars
plt.legend()

# Add copyright text at the bottom left of the plot
plt.figtext(0.01, 0.01, 'Copyright © Srinaath Haribabu', ha='left', va='center', fontsize=10, color='gray')

# Show the plot
plt.tight_layout()
plt.show()
