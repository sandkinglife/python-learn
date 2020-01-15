
# if conditon for boolean
check = True
if check:
    print("true block")

# if else
check = False
if check:
    print("True block")
else:
    print("False block")

# if condition
number = 5
if number == 5:
    print("number is 5")

'''
When we need to check if its a number/string , no need to be check if its exactly equal
Truthy --> Any number except 0 and any string value
Falsy --> 0 and No string
'''
number = 0
if number:
    print("Truthy block for number")
number = 0
if not number:
    print("Falsy block for 0 ")
name = "Vinay"
if name:
    print("Truthy block for string")

# And or OR
number = 5
name = "Vinay"
if number ==5 and name == "Vinay":
    print("And Block")

'''
Ternary
condition_if_true if condition else condition_if_false
(if_test_is_false, if_test_is_true)[test]
'''
a=3
b=4
print("Bigger") if a>b else print("Smaller")

size = True
personality = ("Big", "Small")[size]
print("The cat is", personality)
