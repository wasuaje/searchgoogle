from xgoogle.googlesets import GoogleSets, LARGE_SET, SMALL_SET
gs = GoogleSets(['python', 'perl'])
results_small = gs.get_results() # SMALL_SET by default
len(results_small)
results_small
#    [u'python', u'perl', u'php', u'ruby', u'java', u'javascript', u'c++', u'c',
#     u'cgi', u'tcl', u'c#']
#    >>>
results_large = gs.get_results(LARGE_SET)
len(results_large)

