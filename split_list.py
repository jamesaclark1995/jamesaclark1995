def mysplit(strng):
    """mysplit() is a function that performs the job of string method .split()

       It take a string as an argument and returns a list of that splits
       substrings by whitespaces
       e.g. "I have a cat" becomes ["I", "have", "a", "cat"]
       """
    
    split_list = []

    strng = strng.lstrip() # Removes whitespaces from left-hand-side of string
                           # so they won't be returned in split_list
    
    # if statement to return empty list if string just has whitespaces
    if strng.isspace() is True:
        return split_list

    start = 0
    stop = 0
        
    for i in range(len(strng)):
        if strng[i] == " ":
            stop = i
            split_list.append(strng[start:stop])
            start = i + 1
                
    last_word = ""
    
    for i in range(start, len(strng)):
        last_word += strng[i]
    
    split_list.append(last_word)
    
    return split_list
