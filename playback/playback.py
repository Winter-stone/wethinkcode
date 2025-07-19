string = input('')
str_count = string.count(" ")
new = string.replace(" ", '...', str_count)
print(new)