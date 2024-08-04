"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    ls = []
    if len(result).__mod__(2) == 0:    
        for u, p in enumerate(result):
                result = str(u+1)
                ls.append(result)
    else:
        for i, p in enumerate(result):
                result = str(p) + "-"  + str(i+1)
                ls.append(result)
    return ls[::-1]