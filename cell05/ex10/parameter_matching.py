import sys

params = sys.argv[1:] 

if len(params) != 1:
    print("none")
else:
    expected = params[0]
    answer = input("What was the parameter? ")
    if answer == expected:
        print("Good job!")
    else:
        print("Nope, sorry...")