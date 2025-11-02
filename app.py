def greet_user(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to the Chatbot Automation Demo."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
