def simple_parameter(num):
    num = 10000000
    print("in the function the variable is:", num)


my_num = 10
print("The original variable is:", my_num)
simple_parameter(my_num)
print("After the function call the variable is:", my_num)



print("\n\n--- compare to a function that changes a *list* variable ---")

def list_parameter(lst):
    print("The function was called...")
    lst[0] = 'banana'


my_list = [10, 11, 12, 13]
print("\nthe original list is:", my_list)
list_parameter(my_list)
print("After the function call the list is:", my_list)





print("\n\n--- ...aaaannddd the weird one ---")
print("if the function reassigns the list, it is a *new* list")
def reassign(lst):
    lst = [1,2,3]

ans = [0,0,0]
reassign(ans)
print("no change:", ans)


