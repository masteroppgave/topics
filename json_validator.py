import json
import os
from tqdm import tqdm
import sys

def validate(json_file):

	"""
	Takes a json file and removes lines that are not valid json
	"""

	f = open(json_file, "r")
	out = open("temp.json", "a")
	lines = f.readlines()

	for i in tqdm(range(len(lines))):

		try:
			line = json.loads(lines[i])
		except:
			continue

		out.write(json.dumps(line) + "\n")

	os.remove(json_file)
	os.rename("temp.json", json_file)


if __name__ == "__main__":
	
	if (len(sys.argv) == 2) and (sys.argv[1][-5:] == ".json"):
		validate(sys.argv[1])
	else:
		print "Need one json file as argument."
