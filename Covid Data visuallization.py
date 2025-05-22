import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv('owid-covid-data.csv.csv')



print(df.columns)
print(df.head())


# Keep only required columns
covid = df[['location', 'date', 'total_cases', 'total_deaths']]

# Get the latest data (e.g., latest date for each country)
latest = covid.drop_duplicates('location', keep='last')
latest = latest[latest['location'].apply(lambda x: x not in ['World', 'Africa', 'Asia', 'Europe', 'European Union', 'International', 
 'Oceania','High-income countries','Upper-middle-income countries',
 'Lower-middle-income countries','South America', 'North America','European Union (27)'])]



top_cases = latest.sort_values('total_cases', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_cases['location'], top_cases['total_cases'], color='orange')
plt.xlabel("Total Cases")
plt.title("Top 10 Countries by Total COVID-19 Cases")
print(top_cases)
plt.show()


top_deaths = latest.sort_values('total_deaths', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_deaths['location'], top_deaths['total_deaths'], color='red')
plt.xlabel("Total Deaths")
plt.title("Top 10 Countries by Death")
plt.show()