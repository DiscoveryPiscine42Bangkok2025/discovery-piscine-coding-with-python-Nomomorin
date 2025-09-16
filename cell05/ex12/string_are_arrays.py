import sys

params = sys.argv[1:]

if len(params) != 1:
    print("none")
else:
    text = params[0]
    result = "".join([ch for ch in text if ch == "z"])
    if result:
        print(result)
    else:
        print("none")