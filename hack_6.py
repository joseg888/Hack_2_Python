"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []
    count = 1
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(str(count))
            count += 2
        else:
            result.append("-")
    if len(s) == 0:
        result = ["0"]
    return result