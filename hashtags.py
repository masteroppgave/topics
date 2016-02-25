import json
from collections import Counter
from collections import defaultdict


def most_common(lines, number_of_results):

	"""
	Takes a json file with tweets and returns
	the most common hashtags.
	"""

	hashtags = []

	for line in lines:

		tweet = json.loads(line) 

		for hashtag in tweet["entities"]["hashtags"]:
			hashtags.append(hashtag["text"])

	return Counter(hashtags).most_common(number_of_results)

def co_occurrences(lines):

	"""
	Finds co-occurrences of hashtags in tweets
	"""

	com = defaultdict(lambda: defaultdict(int))

	for line in lines:
		tweet = json.loads(line)

		if len(tweet["entities"]["hashtags"]) < 2:
			continue

		hashtags = [hashtag["text"] for hashtag in tweet["entities"]["hashtags"]]

		print hashtags

		# Build co-occurrence matrix

		for i in range(len(hashtags)-1):
			for j in range(i+1, len(hashtags)):
				h1, h2 = sorted([hashtags[i], hashtags[j]])
				if h1 != h2:
					com[h1][h2] += 1

	return com


if __name__ == "__main__":
	f = open("29jan_tweets.json", "r")

	print co_occurrences(f.readlines())
