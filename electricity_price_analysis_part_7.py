import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# List of years to analyze
years = [2020, 2021, 2022, 2023, 2024]

# Loop through each year to plot the data for May and July
for year in years:
    # Read the data for the current year
    df = pd.read_excel(file_path, sheet_name=str(year))

    # Ensure the 'Date' column is in datetime format and the necessary columns are numeric
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
    df['Electricity Price'] = pd.to_numeric(df['Electricity Price'], errors='coerce')
    df['Non-Renewable Generation (MW)'] = pd.to_numeric(df['Non-Renewable Generation (MW)'], errors='coerce')
    df['Renewable Generation (MW)'] = pd.to_numeric(df['Renewable Generation (MW)'], errors='coerce')
    df['Load (MW)'] = pd.to_numeric(df['Load (MW)'], errors='coerce')

    # Filter data for May (5) and July (7)
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    # Select data for May and July
    df_selected_months = df[(df['Year'] == year) & (df['Month'].isin([5, 7]))]

    # Calculate the RES percentage (ensure no division by zero)
    df_selected_months['RES Percentage'] = df_selected_months['Renewable Generation (MW)'] / \
                                             (df_selected_months['Renewable Generation (MW)'] + df_selected_months['Non-Renewable Generation (MW)']) * 100

    # Find the % RES value where negative prices occur most frequently
    negative_price_data = df_selected_months[df_selected_months['Electricity Price'] < 0]
    average_res_negative_price = negative_price_data['RES Percentage'].mean()

    # Plotting the scatter plot
    plt.figure(figsize=(10, 6))

    # Plot for positive and negative prices separately
    plt.scatter(df_selected_months[df_selected_months['Electricity Price'] >= 0]['RES Percentage'],
                df_selected_months[df_selected_months['Electricity Price'] >= 0]['Electricity Price'],
                color='blue', label='Positive Price', alpha=0.6, marker='o')

    plt.scatter(df_selected_months[df_selected_months['Electricity Price'] < 0]['RES Percentage'],
                df_selected_months[df_selected_months['Electricity Price'] < 0]['Electricity Price'],
                color='red', label='Negative Price', alpha=0.6, marker='x')

    # Add a vertical line at the average RES percentage where negative prices occur
    plt.axvline(x=average_res_negative_price, color='purple', linestyle='--', label=f'Avg RES Threshold for Negative Prices: {average_res_negative_price:.2f}%')

    # Set title and labels
    plt.title(f'Electricity Price vs RES Percentage for May and July {year}')
    plt.xlabel('% Renewable Generation')
    plt.ylabel('Electricity Price (EUR/MWh)')
    plt.grid(True)
    plt.legend()

    # Add copyright text at the bottom left of the plot
    plt.figtext(0.01, 0.01, 'Copyright © Srinaath Haribabu', ha='left', va='center', fontsize=10, color='gray')

    # Show the plot
    plt.tight_layout()
    plt.show()

    # Print the average RES threshold where negative prices occur
    print(f"Average RES Percentage where negative prices occur for {year}: {average_res_negative_price:.2f}%")
