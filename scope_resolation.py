temp =2
def function():
    temp=6
    print("local variable function scope",+temp)
print(temp)

function()

print(temp)