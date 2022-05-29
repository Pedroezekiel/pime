import functools


def verified_user(str):
     for i in str:
        if i["verified"] == True:
            print(i["username"],i["verified"])


fields = [{"username": "Jonathan", "age": 27, "tweets": ["I am bored", "i am single and seriously searching"],"verified": False},

          {"username": "Joel", "age": 30, "tweets": ["I am happy because i am single"], "verified": False},

          {"username": "Endurance", "age": 18, "tweets": ["some scars are never going to heal"], "verified": True},

          {"username": "Jona", "age": 22, "tweets": ["I know sorry can't heal the scar i created", "i know sorry can't fix the mess i created","but am sorry"], "verified": True},

          {"username": "Hope", "age": 20, "tweets": ["please can you let me sail through your heart maybe i will find my final destination ?", ],"verified": False},

          {"username": "Nathan", "age": 15, "tweets": ["All my lives i have been carried by grace and i can't explain why"], "verified": False},

          {"username": "MG", "age": 25, "tweets": ["If a man understand the present he will predict the future"], "verified": True},

          {"username": "mike", "age": 17, "tweets": ["Who discover fire"], "verified": False},

          {"username": "grace", "age": 27, "tweets": ["it is easy to build a trust but it is not easy to rebuild one"], "verified": True},

          {"username": "abel", "age": 27, "tweets": [], "verified": False},
        ]
lst =[a["username"]   for a in fields if a["verified"] == True]
lst2 = map(lambda x : x["username"], filter(lambda x : x["verified"],fields))

ls = [user["username"] for user in fields if user["tweets"] >0]

users_below_25 = [a for a in fields if a["age"] < 25 and a["verified"] == True]

longest_name = functools.reduce(lambda x,y:x if len(x) > len(y) else y ,list(field["username"] for field in fields))

user_ascending_order = sorted(fields, key=lambda field: field["username"])
user_desending_order = sorted(fields, key=lambda field: field["username"],reverse = True)
list_age =list(field["age"] for field in fields)
user_max_age = max(list_age)
user_min_age = min(list_age)
print(ls)