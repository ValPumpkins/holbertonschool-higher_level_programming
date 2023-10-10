#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ponctuation in ".?:":
        text = (ponctuation + "\n\n").join(
            [line.strip(" ") for line in text.split(ponctuation)])

    print("{}".format(text), end="")
