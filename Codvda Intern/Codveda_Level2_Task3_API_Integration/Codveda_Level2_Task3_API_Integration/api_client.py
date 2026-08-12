import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
DEFAULT_TIMEOUT = 10


class APIError(Exception):
    pass


def fetch_users(url=API_URL, timeout=DEFAULT_TIMEOUT):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.Timeout as exc:
        raise APIError("The API request timed out.") from exc
    except requests.exceptions.ConnectionError as exc:
        raise APIError("Could not connect to the API.") from exc
    except requests.exceptions.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "unknown"
        raise APIError(f"API returned HTTP status {status}.") from exc
    except requests.exceptions.RequestException as exc:
        raise APIError(f"API request failed: {exc}") from exc

    try:
        data = response.json()
    except ValueError as exc:
        raise APIError("The API returned invalid JSON.") from exc

    if not isinstance(data, list):
        raise APIError("Unexpected API response format: expected a list.")
    return data


def validate_user(user):
    return (
        isinstance(user, dict)
        and isinstance(user.get("id"), int)
        and isinstance(user.get("name"), str)
        and isinstance(user.get("username"), str)
        and isinstance(user.get("email"), str)
    )


def normalize_users(data):
    return [user for user in data if validate_user(user)]


def display_users(users):
    if not users:
        print("\nNo valid user records were found.")
        return
    print("\n" + "=" * 75)
    print("                    API USER DATA")
    print("=" * 75)
    for user in users:
        print(f"ID       : {user['id']}")
        print(f"Name     : {user['name']}")
        print(f"Username : {user['username']}")
        print(f"Email    : {user['email']}")
        print("-" * 75)


def search_user(users, user_id):
    return next((user for user in users if user["id"] == user_id), None)


def print_menu():
    print("\nSelect an option:")
    print("  1. Display all users")
    print("  2. Search user by ID")
    print("  3. Refresh data from API")
    print("  4. Exit")


def main():
    print("\n" + "=" * 75)
    print("              CODVEDA LEVEL 2 - API INTEGRATION")
    print("=" * 75)
    print("Public API: JSONPlaceholder")
    print("Endpoint  : /users")

    try:
        users = normalize_users(fetch_users())
        print(f"\nSuccessfully fetched {len(users)} valid user records.")
    except APIError as error:
        print(f"\n[ERROR] {error}")
        return

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            display_users(users)
        elif choice == "2":
            try:
                user_id = int(input("Enter user ID (1-10): ").strip())
            except ValueError:
                print("[ERROR] User ID must be an integer.")
                continue
            user = search_user(users, user_id)
            display_users([user] if user else [])
        elif choice == "3":
            try:
                users = normalize_users(fetch_users())
                print(f"Successfully fetched {len(users)} valid user records.")
            except APIError as error:
                print(f"[ERROR] {error}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[ERROR] Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
