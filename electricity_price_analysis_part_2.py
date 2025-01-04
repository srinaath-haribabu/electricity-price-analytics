import pandas as pd
import matplotlib.pyplot as plt

# Path to the Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# List of years to analyze (corresponding to sheet names)
years = [2020, 2021, 2022, 2023, 2024]

# Initialize a dictionary to store the negative price hours for weekdays and weekends
negative_hours_weekdays = {year: 0 for year in years}
negative_hours_weekends = {year: 0 for year in years}

# Loop through each year, read the corresponding sheet, and calculate negative price hours for weekdays and weekends
for year in years:
    # Read the sheet for the current year
    sheet_name = str(year)  # Sheet name corresponds to the year, e.g., '2020', '2021'
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Ensure the 'Date' column is in datetime format (adjusting for 'AM/PM' format)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
    
    # Check if there are any NaT values (missing or unparsed dates) and fix them if necessary
    if df['Date'].isna().any():
        print(f"Warning: Some date values could not be parsed in sheet {sheet_name}.")

    # Filter rows where the electricity price is negative
    negative_prices = df[df['Electricity Price'] < 0]
    
    # Add a column for the day of the week (0=Monday, 6=Sunday)
    negative_prices['Weekday'] = negative_prices['Date'].dt.weekday  # Monday=0, Sunday=6
    
    # Count the negative price hours for weekdays (0-4) and weekends (5-6)
    weekdays_count = negative_prices[negative_prices['Weekday'] < 5].shape[0]  # Weekdays: Monday to Friday
    weekends_count = negative_prices[negative_prices['Weekday'] >= 5].shape[0]  # Weekends: Saturday and Sunday
    
    # Store the counts in the dictionary for this year
    negative_hours_weekdays[year] = weekdays_count
    negative_hours_weekends[year] = weekends_count
    
    print(f"Year {year} - Weekdays negative hours: {weekdays_count}, Weekends negative hours: {weekends_count}")

# Step 2: Plotting the comparison for weekdays vs weekends across the years
labels = list(years)
weekdays_values = [negative_hours_weekdays[year] for year in years]
weekends_values = [negative_hours_weekends[year] for year in years]

x = range(len(years))  # Positions on the x-axis for each year

# Plotting the data
plt.figure(figsize=(12, 8))

# Bar plot for weekdays and weekends
bar_width = 0.35
plt.bar(x, weekdays_values, width=bar_width, label='Weekdays', color='lightblue')
plt.bar([i + bar_width for i in x], weekends_values, width=bar_width, label='Weekends', color='salmon')

# Customizing the plot
plt.xlabel('Year')
plt.ylabel('Number of Negative Price Hours')
plt.title('Negative Electricity Price Hours: Weekdays vs Weekends (2020-2024)')
plt.xticks([i + bar_width / 2 for i in x], labels)  # Position x-ticks to be between bars
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add copyright text at the bottom-left corner
plt.figtext(0.01, 0.01, "© Srinaath Haribabu", horizontalalignment='left', verticalalignment='bottom', fontsize=10, color='gray')

# Show the plot
plt.show()

# Print the results
print("\nComparison of Negative Price Hours for Weekdays vs Weekends:")
for year in years:
    print(f"{year}: Weekdays = {negative_hours_weekdays[year]}, Weekends = {negative_hours_weekends[year]}")
