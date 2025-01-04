import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to your Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# List of years to analyze
years = [2020, 2021, 2022, 2023, 2024]

# Loop through each year and generate a correlation matrix
for year in years:
    # Read the data for the current year
    df = pd.read_excel(file_path, sheet_name=str(year))
    
    # Ensure the 'Date' column is in datetime format and the necessary columns are numeric
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
    df['Electricity Price'] = pd.to_numeric(df['Electricity Price'], errors='coerce')
    df['Load (MW)'] = pd.to_numeric(df['Load (MW)'], errors='coerce')
    df['Non-Renewable Generation (MW)'] = pd.to_numeric(df['Non-Renewable Generation (MW)'], errors='coerce')
    df['Renewable Generation (MW)'] = pd.to_numeric(df['Renewable Generation (MW)'], errors='coerce')
    
    # Extract the day of the week (0=Monday, 6=Sunday)
    df['Day of Week'] = df['Date'].dt.dayofweek

    # Define weekdays and weekends
    df['Weekend/Weekday'] = df['Day of Week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

    # Calculate the correlation matrix for all relevant columns
    correlation_matrix = df[['Electricity Price', 'Load (MW)', 'Non-Renewable Generation (MW)', 'Renewable Generation (MW)']].corr()

    # Create a heatmap to visualize the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)
    plt.title(f'Correlation Matrix for {year}')
    
    # Add copyright text at the bottom left of the plot
    plt.figtext(0.01, 0.01, '© Srinaath Haribabu', ha='left', va='center', fontsize=10, color='gray')

    # Show the plot
    plt.tight_layout()
    plt.show()
