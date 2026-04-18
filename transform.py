import pandas as pd
import os

def transform_data(df):
    # Drop unnamed index column
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Drop nulls in important columns
    df = df.dropna(subset=['batter', 'bowler', 'batting_team'])
    
    return df
