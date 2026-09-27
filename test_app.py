from app import greet, farewell

assert greet("Dara") == "Hello, Dara!"
assert farewell("Dara") == "Goodbye, Dara!"
assert greet("") == "Hello, World!"

print("All tests passed")
