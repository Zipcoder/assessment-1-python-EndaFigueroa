
def delete_keys_from_dict(datadict, keylist):
    for i in keylist:
        del datadict[i]
    return datadict

#### Not passing
    # """
    # Delete a list of keys from a dictionary
    # """
    # pass

def check_dict_for_key(datadict, key):
    answer=datadict.values()
    if key in answer:
        return True
    return False
    # """
    # Check if a value exists in a dictionary
    # (NO FOR loops!)
    # """
    # pass

def get_key_of_min_value(ddd):
    littleGuy = ddd.values()
    littleGuy = min(littleGuy)
    dddKeys = ddd.keys()

    for i in dddKeys:
        if ddd[i] == littleGuy:
            return i
    # """
    # Get the key of the minimum value from a dictionary
    # """
    # pass

def get_key_of_max_value(ddd):
    littleGuy = ddd.values()
    littleGuy = max(littleGuy)
    dddKeys = ddd.keys()

    for i in dddKeys:
        if ddd[i] == littleGuy:
            return i
    
    # """
    # Get the key of the maximum value from a dictionary
    # """
    # pass

def letterfreq(word):
    answer = {}
    for letter in word:
        answer[letter] = word.count(letter)
    return answer
    # '''
    # # Write a function that returns a dictionary of letter frequencies from a word
    # '''
    # pass