import os
import sys
import json
import requests

token_file = "api.key"
url = "https://api.intelbase.is/lookup/email"

def get_token():
    if not os.path.exists(token_file):
        token = input("Please enter your API token: ")
        with open(token_file, "w") as file:
            file.write(token)
    else:
        with open(token_file, "r") as file:
            token = file.read().strip()
    return token

def update_token():
    new_token = input("\nPlease enter your new API token: ")
    with open(token_file, "w") as file:
        file.write(new_token)
    print("\nAPI token updated successfully.")

def save_response(response_data):
    filename = input("\nPlease enter a name for the JSON file (without .json extension): ")
    with open(f"{filename}.json", "w") as json_file:
        json.dump(response_data, json_file, indent=4)
    print(f"\nResponse saved as {filename}.json")

def search_email(token):
    user_email = input("\nPlease enter an email address: ")
    payload = {
        "email": user_email,
        "timeout_ms": 123,
        "include_data_breaches": True,
        "exclude_modules": ["<string>"]
    }
    headers = {
        "x-api-key": token,
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print("\n")
    print(response.text)
    
    while True:
        save_option = input("\nWould you like to save this response? (y/n): ").strip().lower()
        if save_option == 'y':
            save_response(response.json())
            break
        elif save_option == 'n':
            main_2()
            break
        else:
            print("\nInvalid option, please choose 'y' or 'n'. ")

def main():
    print("""
.___        __         .__ __________                       
|   | _____/  |_  ____ |  |\______   \_____    ______ ____  
|   |/    \   __\/ __ \|  | |    |  _/\__  \  /  ___// __ \ 
|   |   |  \  | \  ___/|  |_|    |   \ / __ \_\___ \.  ___/ 
|___|___|  /__|  \___  >____/______  /(____  /____  >\___  >
         \/          \/            \/      \/     \/     \/ 
                                                            
        """)
    main_2()
def main_2():
    token = get_token()
    while True:        
        print("""
       x---------------------x
       | [1] Search Email    |
       | [2] Update Token    |
       | [3] Exit            |
       x---------------------x
        """)
        choice = input("Please choose an option: ")

        if choice == '1':
            search_email(token)
        elif choice == '2':
            update_token()
            token = get_token()
        elif choice == '3':
            sys.exit()
        else:
            print("\nInvalid option, please try again.")

main()
