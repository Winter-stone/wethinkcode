def convert(string):
    smiley = ['🙂', '🙁']
    smile_count = string.count(":)")
    frown_count = string.count(":(")
    if ":)" in string:
        string = string.replace(':)', smiley[0], smile_count)
    if ":(" in string:
        string = string.replace(':(', smiley[1], frown_count)

    return string

def main(string):
    converted=convert(string)
    return converted
print(main("Hello :) Goodbye :( \nYou're Welcome"))