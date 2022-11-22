tel = {'jack': 4098, 'sape': 4139}

# grabbing a value from a key
firstvalue = tel['jack']
firstvalue1 = tel.get("jack")
print(firstvalue)
print(firstvalue1)

# grabbing a key fromn a value
def get_key(val):
    for key, value in tel.items():
        if val == value:
            return key
 
    return "key doesn't exist"

print(tel.items())


print(get_key(4098))


"""
    important functions for dicts
    
    items returns a list of the dict
    websitelist.get(shows) returns a list with all the shows
    dict[key] returns value
    
    dict[new_key] = "new_value"
    
"""

