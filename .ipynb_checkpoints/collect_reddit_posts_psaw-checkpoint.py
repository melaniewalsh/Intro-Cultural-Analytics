# -*- coding: utf-8 -*-
import pandas as pd
from psaw import PushshiftAPI
import sys
import datetime

collect_start_time = datetime.datetime.now()

print("Reddit comment collection beginning...")

api = PushshiftAPI()

query = sys.argv[1]

api_request_generator = api.search_submissions(q=query)
df = pd.DataFrame([comment.d_ for comment in api_request_generator])
df['full_date'] = pd.to_datetime(df['created_utc'], utc=True, unit='s')
df['date'] = df['full_date'].dt.strftime("%Y-%m-%d")

query_formatted = query.replace(' ', '-')
filename = f'{query_formatted}-Reddit-Submissions.csv'
df.to_csv(filename, index=False)

print(f"\n✨✨✨\n{len(df)} total Reddits posts collected\n\nThis Reddit data was written to the file:\n{filename}")
print(f"\n\nTotal time it took to collect this data:\n{str(datetime.datetime.now() - collect_start_time)}✨✨✨")
