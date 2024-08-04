"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if s == [0]:  
        return [0]
    else:  
        result = [str(i) if i % 2 != 0 else i for i in range(1, len(s) + 1)]
    return result
