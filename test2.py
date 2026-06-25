# bug_test.py

password = "SuperSecret123"   # Hardcoded credential


def divide(a, b):
    return a / 0              # Division by zero bug


def get_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query              # SQL injection risk


def execute(user_input):
    eval(user_input)          # Arbitrary code execution risk


def infinite():
    while True:
        pass                  # Infinite loop


def greet():
    unused_variable = "hello" # Unused variable
    print("Welcome")


items = [1, 2, 3]
print(items[10])              # IndexError


data = {"name": "Vinay"}
print(data["age"])            # KeyError
