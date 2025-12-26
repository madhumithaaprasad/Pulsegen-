from datetime import date, timedelta
from agents.ingestion_agent import fetch_daily_reviews
from agents.topic_agent import extract_topics
from agents.dedup_agent import deduplicate_topics
from agents.trend_agent import build_trend

APP_ID = "in.swiggy.android"
END_DATE = date.today()
START_DATE = END_DATE - timedelta(days=30)

daily_topic_counts = {}

df = fetch_daily_reviews(APP_ID, START_DATE, END_DATE)

for day in sorted(df["date"].unique()):
    daily_reviews = df[df["date"] == day]["content"].tolist()
    raw_topics = extract_topics(daily_reviews)
    deduped = deduplicate_topics(raw_topics, raw_topics)
    daily_topic_counts[str(day)] = deduped

trend_df = build_trend(daily_topic_counts)
trend_df.to_csv("output/trend_report.csv")

print("✅ Trend report generated")
