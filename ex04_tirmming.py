userInput = "### Computer Enginner -----"

print(f" Before  : {userInput}")

print(f" After rstrip : {userInput.rstrip('#,-')}")
print(f" After lstrip : {userInput.lstrip('#,-')}")
print(f" Complete Strip : {userInput.strip('#,-')}")