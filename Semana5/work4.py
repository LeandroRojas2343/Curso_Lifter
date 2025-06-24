def remove_odds(list_):
    new_list = []
    for number in list_:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

# first example
# __________________________________________________

# 2 pop
def remove_odds_pop(list_):
    i = len(list_) - 1
    while i >= 0:
        if list_[i] % 2 != 0:
            list_.pop(i)
        i -= 1

# Example of use:
my_list = [2, 4, 3, 5, 8, 9, 6, 3]
print("Original list:", my_list)

remove_odds_pop(my_list)
print("List without odds:", my_list)

