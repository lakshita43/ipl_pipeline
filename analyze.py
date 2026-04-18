def analyze_data(df):
    # Top run scorers
    top_batters = df.groupby('batter')['batter_runs'].sum().sort_values(ascending=False).head(10)
    
    # Top wicket takers
    top_bowlers = df[df['result_type'] == 'wicket'].groupby('bowler')['result_type'].count().sort_values(ascending=False).head(10)
    
    # Most wins by team
    wins = df.groupby('match_won_by')['match_id'].nunique().sort_values(ascending=False)
    
    return top_batters, top_bowlers, wins
