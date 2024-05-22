import secrets


def generate_secret_key():
    secret_key = secrets.token_urlsafe(16)
    return secret_key