key_to_delete = int(input())

if key_to_delete in squares.keys():
    print(squares[key_to_delete])
    del squares[key_to_delete]
else:
    print("There is no such key")

print(squares)
