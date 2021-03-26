#!/usr/bin/python
#
# This program does a Google search for "quick and dirty" and returns
# 50 results.
#

#from xgoogle.search import GoogleSearch, SearchError, GoogleSets, LARGE_SET, SMALL_SET
from xgoogle.googlesets import GoogleSets, LARGE_SET, SMALL_SET
from xgoogle.search import GoogleSearch,SearchError
gs = GoogleSets(['python', 'perl'])
results_small = gs.get_results() # SMALL_SET by default
len(results_small)
print results_small
