data = {}

with open('caffe_clients.txt', 'r') as file:
    for line in file:
        name, cups = line.split()
        data[name] = int(cups)

for client in data:
    data[client] //= 6
    print(client, data[client])

biggest_bonus = max(data.values())

for key, value in data.items():
    if value == biggest_bonus:
        with open('output.txt', 'w+') as file:
            file.write(key)