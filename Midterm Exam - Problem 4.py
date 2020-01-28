"""
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
"""
def lessThan4(aList):
    newList = []
    for item in aList:
        if len(item) <4:
            newList.append(item)
    return newList
    
aList = ["apple", "cat", "dog", "banana"]
result = lessThan4(aList)
print(result)
