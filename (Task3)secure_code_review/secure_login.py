import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Hashed Password:")
print(hashed_password)
