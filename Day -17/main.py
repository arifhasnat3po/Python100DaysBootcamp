class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        print("New user being created....")
    
    
user_1 = User("001","Arif")
print(user_1.username)

user_2 = User("002", "Hasnat")
print(user_2.followers)

