f = open("26.txt")
n = int(f.readline())

data = []
layers = dict()
ox = dict()
answer1 = -1
answer2 = -1

for _ in range(n):
    x, y, z = map(int, f.readline().split())
    data.append([x, y, z])
    if y not in layers.keys():
        layers[y] = 1
    else:
        layers[y] += 1

max_k = max(layers.values())
for key in layers.keys():
    if layers[key] == max_k:
        answer1 = max(answer1, key)

for x, y, z in data:
    if y == answer1:
        if x not in ox.keys():
            ox[x] = 1
        else:
            ox[x] += 1

answer2 = max(ox.values())

print(answer1, answer2)
