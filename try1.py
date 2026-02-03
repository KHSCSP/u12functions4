# Question:
# When you send a list to a function,
# does the function change the list?
# Answer: it depends on what you send.

# iterate through, convert to upper case
def ex1(names):
    pass

usernames = ['hannah', 'ty', 'margot']
# change the list
# TODO call the function
print("sent the list, it changed:", usernames, "\n")


usernames = ['hannah', 'ty', 'margot']
# do not change the list
# TODO call the function, send a *copy*
print("sent a copy, did not change:", usernames, "\n")




# ---- next, assume we *do* want to modify the list ---


# greet each person, remove from the list
# this will not remove all, why?
def greet1(names):
    pass


usernames = ['hannah', 'ty', 'margot']
# TODO call the function
print("did not remove all:", usernames, "\n")






# this *will* remove all
# iterate through a *copy*
# greet each person, remove from the list
def greet2(names):
    pass

usernames = ['hannah', 'ty', 'margot']
# TODO call the function
print("iterated through a copy:", usernames, "\n")



