def compare(x, y):
    rezult = 0
    if x < y:
        rezult = x
    elif x > y:
        rezult = y
    return rezult


string1 = input("input first: ")
string2 = input("input second: ")
a = compare(string1, string2)
if a == 0:
    print("strings are eqial")
else:
    print("String", a, " is bigger ")
