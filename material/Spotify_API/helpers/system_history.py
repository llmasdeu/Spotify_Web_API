import json
import datetime

USER_ID_ERROR = -1

def read_system_history_json(file_path):
    data = None

    try:
        with open(file_path) as f:
            data = json.load(f)
    except:
        data = False
        print("Error! Something happened opening the system history file.")

    return data

def update_system_history_json(file_path, data):
    try:
        with open(file_path, "w") as jsonFile:
            json.dump(data, jsonFile, indent=4, sort_keys=False)
    except:
        print("Error! Something happened updating the system history file.")

def log_system_history_action(file_path, token, action):
    try:
        data = read_system_history_json(file_path=file_path)

        if data:
            id = search_user_in_system_history(token=token, data=data)

            if id == USER_ID_ERROR:
                user_entry = {"userToken": token, "actions": []}
                user_entry["actions"].append(generate_entry(action=action))
                data["activity"].append(user_entry)
            else:
                data["activity"][id]["actions"].append(generate_entry(action=action))

            update_system_history_json(file_path=file_path, data=data)
    except:
        print("Error! Something happened logging the system history action.")

def retrieve_user_system_history(file_path, token):
    try:
        data = read_system_history_json(file_path=file_path)

        if data:
            id = search_user_in_system_history(token=token, data=data)

            if id != USER_ID_ERROR:
                return data["activity"][id]
    except:
        print("Error! Something happened retrieving the system history for a user.")

    return {"message": "There\'s been an error retrieving the system history for the specified user."}

def search_user_in_system_history(token, data):
    try:
        for i in range(len(data["activity"])):
            if data["activity"][i]["userToken"] == token:
                return i
    except:
        print("Error! Something happened searching the user in the system history.")

    return USER_ID_ERROR

def generate_entry(action):
    return {"timestamp": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "uri": action}