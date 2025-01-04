import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to the Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# List of years to analyze (corresponding to sheet names)
years = [2020, 2021, 2022, 2023, 2024]

# Initialize a dictionary to store the negative price hours for each month across all years
monthly_negative_hours = {month: [0] * len(years) for month in range(1, 13)}

# Loop through each year, read the corresponding sheet, and calculate the negative price hours for each month
for idx, year in enumerate(years):
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
    
    # Get the month of each negative price hour and count them
    negative_prices['Month'] = negative_prices['Date'].dt.month  # Extract the month (1-12)
    
    # Count the number of negative price hours for each month
    for month in range(1, 13):  # Months range from 1 to 12
        monthly_negative_hours[month][idx] = negative_prices[negative_prices['Month'] == month].shape[0]

# Step 2: Plotting the comparison for each month across all years
bar_width = 0.15  # Width of each bar
index = np.arange(1, 13)  # Month numbers (1 to 12)

plt.figure(figsize=(12, 8))

# Create bars for each year
for idx, year in enumerate(years):
    plt.bar(index + bar_width * idx, 
            [monthly_negative_hours[month][idx] for month in range(1, 13)], 
            width=bar_width, label=str(year))

# Customizing the plot
plt.xlabel('Month')
plt.ylabel('Number of Negative Price Hours')
plt.title('Monthly Negative Electricity Price Hours (2020-2024)')
plt.xticks(index + bar_width * (len(years) - 1) / 2, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title='Year')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()

# Print the results
print("\nComparison of Negative Price Hours for Each Month (2020-2024):")
for month in range(1, 13):
    print(f"{['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month-1]}: ")
    for year in years:
        print(f"  {year}: {monthly_negative_hours[month][years.index(year)]} hours")
