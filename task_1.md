# Make 3 endpoints:
a. "/register_user", which will register a new user (username: str, password: str)
{
    "username": "John",
    "password": "123456"
}

b. "/get_users", which will return all users (username: str, password: str)
{
    "users": [
        {
            "username": "John",
            "password": "123456"
        },
        {
            "username": "Jane",
            "password": "789012"
        }
    ]
}

c. "/login", which will login a user, check if password is valid (username: str, password: str)
{
    "status": "success"
}
or 
{
    "status": "failed"
}