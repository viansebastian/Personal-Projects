import os

def get_current_username():
    try:
        username = os.getlogin()
        return username
    except OSError:
        return "Unknown"

# Example usage
current_username = get_current_username()
print("Current user:", current_username)
