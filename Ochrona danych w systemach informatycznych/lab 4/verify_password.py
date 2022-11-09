import crypt
import sys

with open(sys.argv[1]) as file:
    user_db = [line.rstrip().split(":") for line in file]

username = input("Username: ")
password = input("Password: ")

user = ""
for u in user_db:
    if u[0] == username:
        user = u
        break

if len(user) != 0:
    password_hash = crypt.crypt(password, user[1][:2])

if len(user) == 0 or password_hash != user[1]:
    print("Invalid username or password")
else:
    print("Logged in!")
