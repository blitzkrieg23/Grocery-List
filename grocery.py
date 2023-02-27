def grocery():

    grocery_list = []
    while True:
        try:
            item = input().strip().upper()
            grocery_list.append(item)

        except (EOFError, KeyError):
            i = sorted(set(grocery_list))
            for x in i:
                print(f"{grocery_list.count(x)} {x}")
            quit()


grocery()