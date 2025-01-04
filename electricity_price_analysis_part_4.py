import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your Excel file
file_path = r'C:\Users\user\OneDrive\Desktop\Srinaath personal files\Personal projects\Project 3 Negative electricity price analysis\master data electricity price.xlsx'  # Replace with your actual file path

# Read the data for 2020
df_2020 = pd.read_excel(file_path, sheet_name='2020')

# Ensure the 'Date' column is in datetime format and the necessary columns are numeric
df_2020['Date'] = pd.to_datetime(df_2020['Date'], errors='coerce', format='%m/%d/%Y %I:%M:%S %p')
df_2020['Electricity Price'] = pd.to_numeric(df_2020['Electricity Price'], errors='coerce')
df_2020['Load (MW)'] = pd.to_numeric(df_2020['Load (MW)'], errors='coerce')

# Extract the day of the week (0=Monday, 6=Sunday)
df_2020['Day of Week'] = df_2020['Date'].dt.dayofweek

# Classify the data as Weekday or Weekend
df_2020['Weekend/Weekday'] = df_2020['Day of Week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Filter for negative electricity price
negative_prices_2020 = df_2020[df_2020['Electricity Price'] < 0]

# Separate the data into weekdays and weekends for load and electricity price
weekday_data = negative_prices_2020[negative_prices_2020['Weekend/Weekday'] == 'Weekday']
weekend_data = negative_prices_2020[negative_prices_2020['Weekend/Weekday'] == 'Weekend']

# Create DataFrame for correlation analysis: Electricity Price vs Load for Weekdays and Weekends
correlation_data = pd.DataFrame({
    'Electricity Price (Weekday)': weekday_data['Electricity Price'],
    'Load (Weekday)': weekday_data['Load (MW)'],
    'Electricity Price (Weekend)': weekend_data['Electricity Price'],
    'Load (Weekend)': weekend_data['Load (MW)']
})

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Matrix: Negative Electricity Price vs Load (Weekdays and Weekends) for 2020')

# Add copyright text at the bottom left of the plot
plt.figtext(0.01, 0.01, '© Srinaath Haribabu', ha='left', va='center', fontsize=10, color='gray')

# Display the plot
plt.tight_layout()
plt.show()
