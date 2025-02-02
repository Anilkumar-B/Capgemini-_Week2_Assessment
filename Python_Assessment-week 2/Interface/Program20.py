"""•	20. Write a scenario where a `UserAuthentication`
 interface contains `login()` and `logout()` methods,
 and it is implemented by `GoogleAuth` and `FacebookAuth` classes."""

from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass
    
    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        return f"GoogleAuth: {username} logged in successfully"

    def logout(self):
        return "GoogleAuth: User logged out successfully"

class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        return f"FacebookAuth: {username} logged in successfully"

    def logout(self):
        return "FacebookAuth: User logged out successfully"

username=input("enter username: ")
password=input("enter Password: ")

google_auth = GoogleAuth()
print(google_auth.login(username,password))
print(google_auth.logout())

facebook_auth = FacebookAuth()
print(facebook_auth.login(username,password))
print(facebook_auth.logout())