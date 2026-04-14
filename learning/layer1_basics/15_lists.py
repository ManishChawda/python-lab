servers = ["web1", "web2", "db1"]

print(servers)
print(type(servers))

print(servers[0])
print(servers[1])
print(servers[2])

servers.append("backup1")
servers.remove("web2")

print(servers)
