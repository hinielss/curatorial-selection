f = open("26.txt")
n, m = map(int, f.readline().split())

data = []
news = []
max_percentage = -float("inf")
answer = -1

for _ in range(n):
    number, price, k = f.readline().split()
    number = int(number)
    price = float(price) * 10
    k = int(k)
    data.append([number, price, k])

for _ in range(m):
    news.append(int(f.readline()))

for number, price, k in data:
    first_price = price
    for p in news:
        price = price * (100 + k*p) / 100 + k
    percentage = (price - first_price) / first_price * 100
    if percentage > max_percentage:
        max_percentage = percentage
        answer = number

print(answer, int(max_percentage))
