
n = 10
list = []

for i in range(n):
    exec(f"var{i} = {i+2}")
    exec(f"print(var{i})")
    exec(f"list.append(var{i})")

print(list)

list_j = "".join(list)

print(list_j)

# print(var2)