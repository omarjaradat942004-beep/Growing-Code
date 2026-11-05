def ft_count_harvest_iterative() -> None:
    Days_until_harvest: int = int(input("Days until harvest:  "))
    index: int = 1
    while (index <= Days_until_harvest):
        print("Day ", index)
        index += 1
    print("Harvest time!")
