def main():
    """
    Given the string "s". add a double quote on both sides, beginning and end.
    Args:
        None
    Returns:
        str: return answer.
    """
    s = 's'
    
    #return  "\'" +s + "\'"
    return f'" {s} "'
b = main()
print(b)