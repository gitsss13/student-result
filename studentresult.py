mark1 = 80
mark2 = 75
mark3 = 65

total = mark1 + mark2 + mark3
average = total / 3

print("Mark 1:", mark1)
print("Mark 2:", mark2)
print("Mark 3:", mark3)
print("Total:", total)
print("Average:", average)

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")