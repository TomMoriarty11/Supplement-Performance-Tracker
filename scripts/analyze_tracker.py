import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/supplement_log.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and calculate average effectiveness
daily_effectiveness = df.groupby('Date')['Effectiveness'].mean()

# Plot
plt.figure(figsize=(10,5))
daily_effectiveness.plot(marker='o', title='Daily Supplement Effectiveness')
plt.xlabel('Date')
plt.ylabel('Average Effectiveness (1–10)')
plt.grid(True)
plt.savefig('visuals/effectiveness_trend.png')
plt.show()
