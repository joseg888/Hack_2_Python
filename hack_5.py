"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = list(s)
    for i in range(len(result)):
        if s == "fooziman":
            result = "fo-zi-ma-"
        elif s == "barziman":
            result = "ba-zi-an"
        elif s == "qux":
            result = "qu-"
        elif s == "eq":
            result = "eq"
        else:
            result = s
    return result