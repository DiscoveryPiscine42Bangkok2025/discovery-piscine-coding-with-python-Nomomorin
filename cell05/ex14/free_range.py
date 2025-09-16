import sys

params = sys.argv[1:]

if len(params) != 2:
    print("none")
else:
      start = int(params[0])
      end = int(params[1])
      arr = [x for x in range(start, end + 1)]
      print(arr)
      print("none")