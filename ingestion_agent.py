import pandas as pd
from google_play_scraper import reviews
from datetime import datetime

def fetch_daily_reviews(app_id, start_date, end_date):
    result, _ = reviews(
        app_id,
        lang="en",
        country="in",
        count=2000
    )

    df = pd.DataFrame(result)
    df["date"] = pd.to_datetime(df["at"]).dt.date
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    return df[["content", "date"]]
