# Add new attribute
- is_admin: bool = False
- Add admin logic to endpoints (cannot register admin user, when login, check if user is admin)

# Add hashing logic to password
- Use sha256 hash algorithm
- Hash the password before saving it to the database
- When login, hash the password and compare it with the hashed password in the database
