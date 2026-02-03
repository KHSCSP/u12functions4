# Question:
# When you send a list to a function,
# does the function change the list?
# Answer: it depends on what you send.

# iterate through, convert to upper case
def ex1(names):
    pass

usernames = ['hannah', 'ty', 'margot']
# TODO call the function
print("sent the list, it changed:", usernames, "\n")


usernames = ['hannah', 'ty', 'margot']
# TODO call the function, send a copy
print("sent a copy, did not change:", usernames, "\n")







# greet each person, remove from the list
def greet1(names):
    pass


# this will *not* change the original list
usernames = ['hannah', 'ty', 'margot']
# TODO call the function
print("tried to remove all:", usernames, "not correct\n")






# this *will* change the original list
# iterate through a copy
# greet each person, remove from the list
def greet2(names):
    pass

usernames = ['hannah', 'ty', 'margot']
# TODO call the function
print("iterated through a copy:", usernames, "\n")



