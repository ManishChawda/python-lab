servers = ["web1", "web2", "db1", "db2"]

print(servers[0:3])
print(servers[1:4])
print(servers[:2])
print(servers[2:])


servers.append("backup1")
print("After append:", servers)

servers.insert(1, "api1")
print("After insert:", servers)

servers.pop()
print("After pop:", servers)

servers.sort()
print("After sort:", servers)