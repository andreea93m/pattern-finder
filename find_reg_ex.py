import re
import glob

def find(pattern, files):
	ids = []
	for file in files:
		lines = open(file, "r" ).readlines()
		for line in lines:
			res = re.search(pattern, line, re.DOTALL)
			if res is not None:
				ids.append(re.search('^(\d+)', line[:res.start()]).group(0))
	return ids

pattern = 'Section \d+ Refresh'
files = glob.glob('./*.html')
ids = find(pattern, files)
print(ids)