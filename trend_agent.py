import pandas as pd

def build_trend(daily_topic_counts):
    df = pd.DataFrame(daily_topic_counts).fillna(0).astype(int)
    df = df.T
    return df
