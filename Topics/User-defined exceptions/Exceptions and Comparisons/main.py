
class WordError(Exception):
    pass

def check_w_letter(word):
    # word = ""
    if word.find("w")>=0:
        raise WordError
    else:
        return word


check_w_letter("chuj")
