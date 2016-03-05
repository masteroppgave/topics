import json
import operator
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

def co_occurrences(lines, number_of_results=0):

	"""
	Finds co-occurrences of hashtags in tweets
	"""

	com = defaultdict(lambda: defaultdict(int))

	for line in lines:
		tweet = json.loads(line)

		if len(tweet["entities"]["hashtags"]) < 2:
			continue

		hashtags = [hashtag["text"] for hashtag in tweet["entities"]["hashtags"]]

		# Build co-occurrence matrix

		for i in range(len(hashtags)-1):
			for j in range(i+1, len(hashtags)):
				h1, h2 = sorted([hashtags[i], hashtags[j]])
				if h1 != h2:
					com[h1][h2] += 1

	most_common = []

	for h1 in com:
		h1_max = max(com[h1].items(), key=operator.itemgetter(1))
		for h2 in h1_max:
			most_common.append(((h1, h2), com[h1][h2]))

	max_hashtags = sorted(most_common, key=operator.itemgetter(1), reverse=True)

	if number_of_results>0:
		return([m for m in max_hashtags if m[-1]>0][:number_of_results])
	else:
		return([m for m in max_hashtags if m[-1]>0])



if __name__ == "__main__":
	f = open("superbowltweets.json", "r")

	print (most_common(f.readlines(), 100))
