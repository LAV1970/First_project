import re

def find_word(text, word):
    result = re.search(word, text)  
    if result:
        first_index = result.start()
        last_index = result.end()
        search_string = result.group()
    else:
        first_index = None
        last_index = None
        search_string = word
    
    result_dict = {
        'result': result is not None,
        'first_index': first_index,
        'last_index': last_index,
        'search_string': search_string,
        'string': text
    }
    
    return result_dict
    