from extract import extract_data
from transform import transform_data
from analyze import analyze_data
from visualize import plot_top_batters

df = extract_data()
df = transform_data(df)
top_batters, top_bowlers, wins = analyze_data(df)
plot_top_batters(top_batters)
