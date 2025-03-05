import socket

# Function to check if there's an internet connection
def is_online() -> bool:
    try:
        # Try to resolve a common host
        socket.gethostbyname("www.google.com")
        return True
    except socket.error:
        return False