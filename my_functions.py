import random
# this function will create a list with n random items
def create_list(min=1, max=100, n=100):
    lst = []
    for i in range(n):
        lst.append(random.randint(min, max))
    return lst
    # TODO convert to list comprehension


# this function will receive a list
# and return a 2D list of useful information
def create_list_stats(lst):
    my_stats = []
    # NOTE: this *will* change the list unless you send a copy

    return my_stats


