my_app ={
    "name": "Shatulo",
    "age": "31",
    "email": "chikumbeshats4@gmail.com"
}


# Access
print(my_app["name"])

# Add/ Update
my_app["country"] = "Zambia"

# Delete
del my_app["email"]

#print (person)

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def put(self, key, value):
    
        hash_key = hash(key) % self.size
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_key].append([key, value])

    def get(self, key):
        hash_key = hash(key) % self.size
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None
    
hm = HashMap(10)
hm.put("name", "Shatulo")
hm.put("age", 31)

print(hm.get("name"))
print(hm.get("age"))
print(hm.get("email"))