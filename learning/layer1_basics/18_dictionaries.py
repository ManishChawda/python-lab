server = {
    "name": "web1",
    "ip": "192.168.1.10",
    "status": "running"
}

print(server)
print(type(server))

print(server["name"])
print(server["ip"])

server["status"] = "stopped"

print(server)