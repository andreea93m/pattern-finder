import re
import itertools
import glob
import argparse
from multiprocessing import Pool

class PatternFinder(object):

	def __init__(self):
		""" Initializes the object and creates a pool of 4 processes """

		super(PatternFinder, self).__init__()
		self.pool = Pool(processes=4)

	def find(self, pattern, files):
		""" For each file, calls a function that searches for the pattern in
		that file. Each file is handled by a different process.
		To give 2 parameters to the function, a list of tuples is passed, each
		tuple contains the pattern and a file.
		Finally, the list of lists of ids is flattened and returned.
		"""

		res = self.pool.starmap(self.find_in_file, zip([pattern]*len(files), files))

		return list(itertools.chain.from_iterable(res))

	def find_in_file(self, pattern, fileName):
		""" Searches for the pattern in a file, line by line.
		If it finds it, it saves the id. Returns an array of ids.
		"""

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
		""" Removes pool object from the instance before pickling
		since Pool objects cannot be pickled.
		"""

		self_dict = self.__dict__.copy()
		del self_dict['pool']

		return self_dict

	def __setstate__(self, state):
		""" Called upon unpickling """

		self.__dict__.update(state)	

parser = argparse.ArgumentParser()
parser.add_argument("--pattern", type=str, help="provide search pattern in regular expression syntax", required=True)
parser.add_argument("--files", type=str, help="provide input files", required=True)
args = parser.parse_args()
if args.pattern is not None and args.files is not None:
	print("Searching for " + args.pattern + " in " + args.files)
	patternFinder = PatternFinder()
	print(patternFinder.find(args.pattern, glob.glob(args.files)))