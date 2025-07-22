grocery_list = {
}
items = []

while True:
    try:
        item = input().strip().upper()
    except EOFError as e:
        print()
        for i in items:
            how_many = items.count(i)
            grocery_list[i] = how_many
        for key, value in sorted(grocery_list.items()):
            print(value, key)
        break
    else:
        items.append(item)
        for i in items:
            how_many = items.count(i)
