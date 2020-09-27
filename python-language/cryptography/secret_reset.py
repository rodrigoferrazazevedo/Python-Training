import secrets

def get_reset_pwd_url(token_length=16):
    token = secrets.token_urlsafe(token_length)
    return f'https://mydomain.com/reset-pwd/{token}'

print(get_reset_pwd_url())
