import re

def camel_case(phrase):
    phrase = phrase.title()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("_", "")
    phrase = re.sub('[^0-9a-zA-Z]+', '', phrase)
    return phrase[0].lower() + phrase[1:]
