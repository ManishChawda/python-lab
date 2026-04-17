server = {
    "name": "web1",
    "ip": "192.168.1.10",
    "status": "running"
}

# Get value safely
print(server.get("name"))

# Add new key
server["port"] = 80

# Update existing key
server["status"] = "stopped"

# Remove key
server.pop("ip")

print(server)