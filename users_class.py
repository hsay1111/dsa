
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"

    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}! Contact me at {self.email}")


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


    


##user2 = User('john', 'john doe', 'jdoe@gmailcom')
##
##print(user2)    
##print(user2.introduce_yourself('hide'))



michael = User('michael', 'Michael Scott', 'Mscott@gmail.com')
jim = User('jim', 'Jim Halpert', 'Jhal@gmail.com')
dwight = User('dwight', 'Dwight Schrute', 'Dsch@gmail.com')
pam = User('pam', 'Pam Beasley', 'pam@gmail.com')

users = [michael, jim, dwight, pam]

database = UserDatabase()

database.insert(michael)
database.insert(jim)
database.insert(dwight)
database.insert(pam)

user = database.find('jim')
print(user)

database.update(User(username='pam', name='Pam Beasley', email='pamB@gmail.com'))
print(database.find('pam'))

print(database.list_all())


