import json
from collections import Counter


def most_common(lines, number_of_results):

	"""
	Takes a json file with tweets and returns
	the most common hashtags.
	"""

	hashtags = []

	for line in lines:

		line = json.loads(line) 

		for hashtag in line["entities"]["hashtags"]:
			hashtags.append(hashtag["text"])

	return Counter(hashtags).most_common(number_of_results)


if __name__ == "__main__":
	f = open("29jan_tweets.json", "r")

	print most_common(f.readlines(), 10)
