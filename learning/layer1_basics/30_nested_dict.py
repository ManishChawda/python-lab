server = {
    "name": "web1",
    "network": {
        "ip": "192.168.1.10",
        "port": 80
    },
    "status": "running"
}

print(server["name"])
print(server["status"])
print(server["network"]["ip"])
print(server["network"]["port"])


server = {
    "name": "web1",
    "ip": "192.168.1.10",
    "status": "running"
}

# Loop through keys
for key in server:
    print("Key:", key)

# Loop through values
for value in server.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in server.items():
    print(key, ":", value)