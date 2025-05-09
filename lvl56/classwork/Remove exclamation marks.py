def remove_exclamation_marks(s):
    res = ""
    
    for i in s:
        if i != "!": res += i
        
    return res
def remove_exclamation_marks(s):
    return s.replace("!", "")