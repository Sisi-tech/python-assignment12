import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type='pandas')

print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))
print("\nUnique strengths:\n", df['strength'].unique())

def parse_strength(s):
    try:
        if isinstance(s, (int, float)):
            return float(s)
        if '-' in s:
            parts = s.split('-')
            return (float(parts[0]) + float(parts[1])) / 2
        return float(s)
    except:
        return None

df['strength'] = df['strength'].apply(parse_strength)
df = df.dropna(subset=['strength', 'frequency'])

fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'}
)

fig.write_html("wind.html")
print("✅ Plot saved as wind.html")

