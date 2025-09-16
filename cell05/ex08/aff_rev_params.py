import sys

params = sys.argv[1:]
if len(params) >= 2:
      print("\n".join(reversed(params))) 
else:
    print("none")