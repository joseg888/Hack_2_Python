"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = [] 
    counter = 1
    
    for i in s:
        new_item = {}
        
        for key, value in i.items():
            new_item[str(counter)] = str(counter + 1)
            counter += 2
        
        result.append(new_item)
    
    return result