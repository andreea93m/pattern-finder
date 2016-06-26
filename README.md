# pattern-finder

- `$ git clone https://github.com/andreea93m/pattern-finder.git`
- `$ cd pattern-finder`
- `$ python test_pattern_finder.py`

The program uses the <i>unittest</i> Python module to run a few tests that search for different patterns in regular expression format in a set of files and check that the returned IDs are correct. The input files contain lines in the format: [id]':'[content]. The tests are in the <i>test_pattern_finder.py</i> file, while the logic is in <i>find_reg_ex.py</i>. To run the tests, follow the instructions above. To search for a pattern, provide the pattern and the files as command line arguments, like this:

- `$ python find_reg_ex.py --pattern 'Section \d+ Refresh' --files 'input/*.html'`

The class <i>PatternFinder</i> uses a Pool of 4 processes from the <i>multiprocessing</i> module to search for a pattern inside each of the files provided as arguments to the <i>find</i> function. Each of these processes calls the function <i>find_in_file</i> for one file. When a process finishes, it goes to the next file, such that the processes are recycled. This ensures better performance, since files can be processed in parallel. When comparing the implementation with the pool of processes to the one without, I observe the time needed to execute the tests is shorter in the first case.

I use the Python module <i>re</i> for handling regular expressions. The expression is searched for in each line of the input file. This makes it easier to find the ID, in case the expression is actually found, rather than looking in the entire file. In terms of I/O operations, this is a good solution because it only reads each whole file once, but it might be problematic in terms of memory if the files are extremely large.
