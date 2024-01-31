#!/usr/bin/python3
def text_indentation(text):
    '''
     prints a text with 2 new lines after each of these characters: ., ? and :
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newText = ""
    for char in text:
        if char == "." or char == "?" or char == ":":
            newText += char + "\n\n"
        else:
            newText += char
    print(newText)
