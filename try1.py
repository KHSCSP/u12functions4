# Question:
# When you send a list to a function,
# does the function change the list?
# Answer: it depends on what you send
# and how you iterate through


# if your goal *is* to change the list, here is how
# indexed loop, convert to upper case
def change1(names):
    pass

# if your goal is to *not* change the list
# here are two ways (enhanced loop, send copy)
def no_change(names):
    pass




usernames = ['hannah', 'ty', 'margot']
# TODO call the functions
print("did it change??", usernames, "\n")








# Question #2 - removing from a list
# --- assume we *do* want to modify the list
# --- how can we *remove* from a list?

# greet each person, remove from the list
# this will not remove all, why?
def greet_wrong(names):
    pass


# this *will* remove all
# iterate through a *copy*
# greet each person, remove from the list
def greet_remove(names):
    pass



usernames = ['hannah', 'ty', 'margot']
# TODO call the functions
print("did it remove all??", usernames, "\n")



