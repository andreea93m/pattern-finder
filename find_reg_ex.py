import re

def find(pattern, files):
	ids = []
	for fileName in files:
		file = open(fileName, "r" )
		lines = file.readlines()
		for line in lines:
			res = re.search(pattern, line, re.DOTALL)
			if res is not None:
				ids.append(re.search('^(\d+)', line[:res.start()]).group(0))
		file.close()
	return ids