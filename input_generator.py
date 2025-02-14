import random
import string

def generate_random_string(length=10):
    """Generates a random alphanumeric string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))