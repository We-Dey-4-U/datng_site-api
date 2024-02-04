import secrets

secret_key = secrets.token_hex(32)

with open("secret_key.txt", "w") as f:
    f.write(secret_key)

print("Secret key has been generated and saved to secret_key.txt.")