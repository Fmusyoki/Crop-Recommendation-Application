
import database as db
import streamlit_authenticator as stauth 

usernames = ["fmusyoki", "skyalo", "rafikim"]
names = ["fred musyoki", "steve kyalo", "rafiki fred"]
passwords = ["2023", "1010", "2000"]
hashed_passwords = stauth.Hasher(passwords).generate()




for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)
    


import json
 
# Opening JSON file
with open('_secret_auth_.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print("\nusername1:", data['username1'])
    print("\nusername2:", data['username2'])