import requests

# Define the base URL of your web server
BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    endpoint = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    response = requests.post(endpoint, data=data)
    assert response.status_code == 200, "Failed to register user"
    print("User registered successfully")


def log_in_wrong_password(email: str, password: str) -> None:
    endpoint = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(endpoint, data=data)
    assert response.status_code == 401, "Expected login failure, but succeeded"
    print("Login with wrong password failed as expected")


def log_in(email: str, password: str) -> str:
    endpoint = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(endpoint, data=data)
    assert response.status_code == 200, "Failed to log in"
    session_id = response.cookies.get("session_id")
    print("Logged in successfully")
    return session_id


def profile_unlogged() -> None:
    endpoint = f"{BASE_URL}/profile"
    response = requests.get(endpoint)
    assert response.status_code == 403, "Profile accessed without logging in"
    print("Profile accessed without logging in as expected")


def profile_logged(session_id: str) -> None:
    endpoint = f"{BASE_URL}/profile"
    cookies = {"session_id": session_id}
    response = requests.get(endpoint, cookies=cookies)
    assert response.status_code == 200, "Failed to access profile"
    print("Profile accessed while logged in")


def log_out(session_id: str) -> None:
    endpoint = f"{BASE_URL}/sessions"
    cookies = {"session_id": session_id}
    response = requests.delete(endpoint, cookies=cookies)
    assert response.status_code == 302, "Failed to log out"
    print("Logged out successfully")


def reset_password_token(email: str) -> str:
    endpoint = f"{BASE_URL}/reset_password"
    data = {"email": email}
    response = requests.post(endpoint, data=data)
    assert response.status_code == 200, "Failed to get reset password token"
    token = response.json()["reset_token"]
    print("Reset password token retrieved")
    return token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    endpoint = f"{BASE_URL}/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }
    response = requests.put(endpoint, data=data)
    assert response.status_code == 200, "Failed to update password"
    print("Password updated successfully")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
