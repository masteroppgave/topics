import json
import vincent
import pandas

f = open("superbowltweets.json")

lines = f.readlines()

broncos = []
panthers = []

for line in lines:
	line = json.loads(line)

	hashtags = [l["text"] for l in line["entities"]["hashtags"]]

	print hashtags

	if "broncos" in hashtags:
		broncos.append(line["created_at"])

	if "panthers" in hashtags:
		panthers.append(line["created_at"])


counts_b = [1] * len(broncos)
idx_b = pandas.DatetimeIndex(broncos)
series_b = pandas.Series(counts_b, index=idx_b)
per_minute_b = series_b.resample("1min", how="sum").fillna(0)

counts_p = [1] * len(panthers)
idx_p = pandas.DatetimeIndex(panthers)
series_p = pandas.Series(counts_p, index=idx_p)
per_minute_p = series_p.resample("1min", how="sum").fillna(0)

match_data = dict(BRONCOS=per_minute_b, PANTHERS=per_minute_p)

all_matches = pandas.DataFrame(data=match_data,
                               index=per_minute_b.index)

all_matches = all_matches.resample('1Min', how='sum').fillna(0)
 

time_chart = vincent.Line(all_matches[['BRONCOS', 'PANTHERS']])
time_chart.axis_titles(x='Time', y='Freq')
time_chart.legend(title='Matches')
time_chart.to_json('chart.json')
