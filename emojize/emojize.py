import emoji

switch = input('Input: ').strip().lower()
print("Output: ", emoji.emojize(switch, language = 'alias'))
