import pandas as pd
import matplotlib.pyplot as plt

# Path to the Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# List of years to analyze (corresponding to sheet names)
years = [2020, 2021, 2022, 2023, 2024]

# Initialize a list to store the negative price counts for each year
negative_price_counts = []

# Loop through each year, read the corresponding sheet, and calculate the negative hours
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
    
    # Count the number of negative price hours for the current year
    negative_hours_count = negative_prices.shape[0]
    
    # Store the result for this year
    negative_price_counts.append(negative_hours_count)
    
    print(f"Number of negative price hours in {year}: {negative_hours_count}")

# Step 2: Create a bar graph to show the negative price hours for each year
plt.figure(figsize=(10, 6))
plt.bar(years, negative_price_counts, color='green')
plt.xlabel('Year')
plt.ylabel('Number of Negative Price Hours')
plt.title('Number of Negative Electricity Price Hours (2020-2024)')
plt.xticks(years)

# Add copyright text at the bottom-left corner
plt.figtext(0.01, 0.01, "© Srinaath Haribabu", horizontalalignment='left', verticalalignment='bottom', fontsize=10, color='gray')

plt.show()

#-------------------------------------------------------------------------------------------

# Loop through each year, read the corresponding sheet, and generate the negative price depth histogram
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
    
    # Get the magnitude of the negative prices (depth), which is the absolute value of the negative price
    negative_prices['Price Depth'] = negative_prices['Electricity Price'].abs()

    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(negative_prices['Price Depth'], bins=20, color='blue', edgecolor='black')  # Histogram of negative price depth
    plt.xlabel('Depth of Negative Prices (Absolute Value)')
    plt.ylabel('Number of Hours with Negative Prices')
    plt.title(f'Negative Price Depth Distribution for {year}')
    plt.grid(True)

    # Add copyright text at the bottom-left corner
    plt.figtext(0.01, 0.01, "© Srinaath Haribabu", horizontalalignment='left', verticalalignment='bottom', fontsize=10, color='gray')

    plt.show()

#-------------------------------------------------------------------------------------------

# Initialize a list to store the total number of negative price hours for each month (combined for all years)
monthly_negative_hours_combined = [0] * 12  # List to accumulate the negative hours for each month (Jan to Dec)

# Loop through each year, read the corresponding sheet, and calculate the negative hours by month
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
    
    # Get the month of each negative price hour and count them
    negative_prices['Month'] = negative_prices['Date'].dt.month  # Extract the month (1-12)
    
    # Accumulate the number of negative price hours for each month
    for month in range(1, 13):  # Months range from 1 to 12
        monthly_negative_hours_combined[month - 1] += negative_prices[negative_prices['Month'] == month].shape[0]

    print(f"Accumulated negative hours by month for {year}: {monthly_negative_hours_combined}")

# Step 1: Plotting the combined data for all years
plt.figure(figsize=(12, 8))

# Plot bars for the combined negative price hours across all years
plt.bar(range(1, 13), monthly_negative_hours_combined, width=0.6, color='skyblue', edgecolor='black')

# Customizing the plot
plt.xlabel('Month')
plt.ylabel('Total Number of Negative Price Hours')
plt.title('Total Number of Negative Electricity Price Hours by Month (2020-2024)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add copyright text at the bottom-left corner
plt.figtext(0.01, 0.01, "© Srinaath Haribabu", horizontalalignment='left', verticalalignment='bottom', fontsize=10, color='gray')

# Show the plot
plt.show()

#------------------------------------------------------------------------------


# Initialize a dictionary to store the negative price hours for each year by month
monthly_negative_hours_by_year = {year: [0] * 12 for year in years}

# Colors for each year (one color per year)
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Loop through each year, read the corresponding sheet, and calculate the negative hours by month
for i, year in enumerate(years):
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
        monthly_negative_hours_by_year[year][month - 1] = negative_prices[negative_prices['Month'] == month].shape[0]

    print(f"Negative hours by month for {year}: {monthly_negative_hours_by_year[year]}")

# Step 1: Plotting the data for all years (stacked bar chart)
plt.figure(figsize=(12, 8))

# Create a stacked bar chart for each year's data
bottom = [0] * 12  # Initialize bottom to 0 for stacking
for i, year in enumerate(years):
    plt.bar(range(1, 13), monthly_negative_hours_by_year[year], width=0.6, color=colors[i], label=str(year), bottom=bottom)
    bottom = [bottom[j] + monthly_negative_hours_by_year[year][j] for j in range(12)]  # Update bottom

# Customizing the plot
plt.xlabel('Month')
plt.ylabel('Total Number of Negative Price Hours')
plt.title('Monthly Negative Electricity Price Hours by Year (2020-2024)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title="Year")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add copyright text at the bottom-left corner
plt.figtext(0.01, 0.01, "© Srinaath Haribabu", horizontalalignment='left', verticalalignment='bottom', fontsize=10, color='gray')

# Show the plot
plt.show()
