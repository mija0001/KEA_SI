from argon2 import PasswordHasher, Type
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(time_cost = 3, memory_cost = 65536, parallelism = 4, hash_len = 32, salt_len = 16, type = Type.ID)


def check_password(password, hashed):
    try:
        if ph.verify(hashed, password):
            return True
    except VerifyMismatchError:
        return False

    
if __name__ == "__main__":
    password = input("Enter password: ")
    hashed = ph.hash(password)
    print("Hashed password: ", hashed)
    password = input("Enter password again: ")
    if check_password(password, hashed):
        print("Password is correct")
    else:
        print("Password is incorrect")