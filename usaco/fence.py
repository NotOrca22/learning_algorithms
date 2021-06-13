x = "3 10"
y = "4 12"

result = int(y.split(" ")[1]) - int(x.split(" ")[0])
if int(x.split(" ")[1]) >= int(y.split(" ")[0]):
    pass
else:
    result -= int(y.split(" ")[0]) - int(x.split(" ")[1])
print(result)