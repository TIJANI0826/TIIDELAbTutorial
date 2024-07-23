
# Python Project Setup and API Connection Tutorial

This tutorial provides step-by-step instructions on how to set up a virtual environment for a Python project and how to connect to an API using the `requests` library.

## Setting Up a Virtual Environment

Using a virtual environment ensures that your project dependencies are isolated and prevents conflicts with other projects.

### Step-by-Step Instructions

1. **Install Virtualenv (if not already installed):**
   ```bash
   pip install virtualenv
   ```

2. **Navigate to Your Project Directory:**
   ```bash
   cd /path/to/your/project
   ```

3. **Create a Virtual Environment:**
   ```bash
   virtualenv venv
   ```
   This command creates a directory named `venv` in your project directory.

4. **Activate the Virtual Environment:**
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install Required Packages:**
   Once the virtual environment is activated, you can install any required packages using pip. For example:
   ```bash
   pip install requests
   ```

6. **Deactivate the Virtual Environment:**
   When you're done working in the virtual environment, you can deactivate it:
   ```bash
   deactivate
   ```

## Connecting to an API

In this example, we'll use the GitHub API to fetch user details.

### Prerequisites

Make sure you have the `requests` library installed. You can install it using the following command:

```bash
pip install requests
```

### Example Code

Create a Python file (e.g., `github_api.py`) and add the following code:

```python
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
    username = input("Type the GitHub username")  # Replace with any GitHub username
    user_data = get_github_user(username)
    
    if user_data:
        print(f"User: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Public Repos: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
    else:
        print("User not found or an error occurred")
```

### Explanation

1. **Import `requests`:**
   Import the `requests` library to make HTTP requests.

2. **Define `get_github_user` Function:**
   - Takes a GitHub username as an argument.
   - Constructs the API URL.
   - Sends a GET request to the URL.
   - Checks if the response status code is 200 (OK).
   - Parses the JSON response and returns user data.
   - If the user is not found or an error occurs, it returns `None`.

3. **Main Block:**
   - Collects the username and set the GitHub username e.g TIJANI0826
   - Calls the `get_github_user` function.
   - Prints user details if the user is found; otherwise, prints an error message.

This code will output the GitHub user’s details such as username, name, public repositories, followers, and following.

## Conclusion

Following these steps will help you set up a virtual environment for your Python project and connect to an API using the `requests` library. This ensures your project dependencies are managed efficiently and allows you to interact with external APIs seamlessly.

## License

Include your project license information here.
