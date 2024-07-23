import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        return None

if __name__ == "__main__":
    username = "TIJANI0826"  # Replace with any GitHub username
    user_data = get_github_user(username)
    
    if user_data:
        print(f"User: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Public Repos: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
    else:
        print("User not found or an error occurred")
