def ft_count_harvest_recursive_helper(Days_until_harvest: int) -> None:
    if (Days_until_harvest == 0):
        return
    else:
        ft_count_harvest_recursive_helper(Days_until_harvest - 1)
        print("Day ", Days_until_harvest)


def ft_count_harvest_recursive() -> None:
    Days_until_harvest: int = int(input("Days until harvest:  "))
    ft_count_harvest_recursive_helper(Days_until_harvest)
    print("Harvest time!")
