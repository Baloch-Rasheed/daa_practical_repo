def sub_string_matching_algorithm(text, sub):
    len_of_text = len(text)
    len_of_sub = len(sub)

    if len_of_sub > len_of_text:
        return -2
    
    matching = False
    
    for i in range((len_of_text - len_of_sub)+1):
        if text[i] == sub[0]:
            matching = True
            for j in range(len_of_sub ):
                
                if text[i+j] == sub[j]:
                    matching = True
                else:
                    matching = False
                    break
        if matching:
            return i
    return -1
                