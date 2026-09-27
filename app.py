def greet(name):
    if not name:
        name = "World"
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("Sunrise"))
