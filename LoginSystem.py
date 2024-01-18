class LoginSystem:
    def __init__(self):
        self.users=dict()
        self.logged_users=set()
        self.__mapping={}
        for i in range(0,128):
            k=i/11
            self.__mapping[chr(i)]=str(k%128)

    def encrypt(self, password):
        pwd=""
        for i in password:
            pwd=pwd+self.__mapping[i]
        return pwd
    def register(self,username,password):
        if username in self.users:
            print("user already exists")
        else:
            self.users[username]=self.encrypt(password)
            print("user registered successfully")
    def login(self,username,password):
        if username in self.users:
            if(self.encrypt(password)==self.users[username]):
                self.logged_users.add(username)
                print("user logged in successfully")
            else:
                print("password doesn't match")
        else:
            print("user isn't in the system")
    def sign_out(self, username):
        if username in self.users:
            if username in self.logged_users:
                self.logged_users.remove(username)
                print("user signed out successfully")
            else:
                print("user is not logged in")
        else:
            print("user is not in the system")


a=LoginSystem()
a.register("khyati","khyati")
a.login("khyati","bhatt")
a.login("prakriti","1234")
a.sign_out("kbhatt")
