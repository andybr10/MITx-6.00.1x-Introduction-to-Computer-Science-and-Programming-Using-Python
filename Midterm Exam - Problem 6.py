def max_val(t): 
   
    result = 0
    rec_result = 0
    i = 0
    
    for item in t:
        if type(item) == int:
            if item > result:
                result = item
        else:
            rec_result = max_val(t[i])
            if rec_result > result:
                result = rec_result
        i += 1
    
    return result
