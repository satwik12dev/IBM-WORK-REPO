# Simple Python app

def greet(name):
    return f"Hello, {name}! Welcome to Docker."

if __name__ == "__main__":
    name = input("Enter your name: ")
    message = greet(name)
    print(message)