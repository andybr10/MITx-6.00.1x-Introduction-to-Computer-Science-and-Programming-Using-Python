def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    count_map = {}
    for v in aDict.values():
        count_map[v] = count_map.get(v, 0) + 1
    unique_keys = [ k for k, v in aDict.items() if count_map[v] == 1]  
    return unique_keys
