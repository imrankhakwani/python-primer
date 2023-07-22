import random, math

print(random.randint(1, 5))

print(math.trunc(random.random() * 100))

colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]

print(random.choice(colors))

random.shuffle(colors)

print(colors)

lst = [[i] for i in range(20)]

print(lst)

random.shuffle(lst)

print(lst)

print(random.randrange(0, 200, 7))

output = {"Heads": 0, "Tails": 0}
coin = list(output.keys())

for i in range(10000):
    output[random.choice(coin)] += 1

print("Heads: ", output["Heads"])
print("Tails: ", output["Tails"])
