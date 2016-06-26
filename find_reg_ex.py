import re
import itertools
from multiprocessing import Pool

class PatternFinder(object):

	def __init__(self):
		super(PatternFinder, self).__init__()
		self.pool = Pool(processes=4)

	def find(self, pattern, files):
		ids = []
		res = self.pool.starmap(self.find_in_file, zip([pattern]*len(files), files))
		ids = list(itertools.chain.from_iterable(res))
		return ids

	def find_in_file(self, pattern, fileName):
		ids = []
		file = open(fileName, "r" )
		lines = file.readlines()
		for line in lines:
			res = re.search(pattern, line, re.DOTALL)
			if res is not None:
				ids.append(re.search('^(\d+)', line[:res.start()]).group(0))
		file.close()
		return ids

	def __getstate__(self):
		self_dict = self.__dict__.copy()
		del self_dict['pool']
		return self_dict

	def __setstate__(self, state):
		self.__dict__.update(state)