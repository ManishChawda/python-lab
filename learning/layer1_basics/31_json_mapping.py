response = {
    "status": 200,
    "data": {
        "user": {
            "name": "Manish",
            "role": "admin"
        },
        "servers": [
            {"name": "web1", "status": "running"},
            {"name": "db1", "status": "stopped"}
        ]
    }
}

# Access user name
print(response["data"]["user"]["name"])

# Access first server name
print(response["data"]["servers"][0]["name"])

# Loop through servers
for server in response["data"]["servers"]:
    print(server["name"], ":", server["status"])