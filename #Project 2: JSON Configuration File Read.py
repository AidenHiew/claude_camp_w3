#Project 2: JSON Configuration File Reader_Writer
#Read a config.json file containing user preferences (e.g., theme, language, font size).
#Use the command line to let the user modify any setting.
#Save the modified settings back to config.json.

#Bonus: Add data validation (e.g., font size must be between 8 and 32).

import json
import os

FILE_NAME = "config.json"
#load the config file
def load_config():
    if not os.path.exists(FILE_NAME):
        print (f"{FILE_NAME} not found. Creating a new file with default settings.")
        default_config ={"theme": "orange", "language": "en", "font_size": 14}
        save_config(default_config)
        return default_config
    
    #if the file exists, load the config
    with open(FILE_NAME, 'r') as files:
        config = json.load(files)
    
    #validate loaded values
    for key, value in config.items():
        is_valid, validate_value = validate_setting(key, value)
        if is_valid:
            config[key] = validate_value
        else:
            print (f"Invalid value found for {key} in config file. Using default value.")

            if key == "font_size":
                config[key] = 14
            elif key == "theme":
                config[key] = "orange"
            elif key == "language":
                config[key] = "en"
    save_config(config)
    return config
           


    
def save_config(config_data):
    with open (FILE_NAME, 'w') as files:
        json.dump(config_data, files, indent=4)
    print(f"Settings saved to {FILE_NAME}")


def validate_setting(key, value):
    if key == "font_size":
        try:
            font_size = int(value)
            if 8 <= font_size <= 32:
                return True,font_size
            else:
                print("Font size must be between 8 and 32.")
                return False, None
        except ValueError:
            print("Font size must be a number.")
            return False, None

    if key == "theme":
        allowed_theme = ["orange", "blue", "green"]
        cleaned_value = value.strip().lower()
        
        if cleaned_value in allowed_theme:
            return True, cleaned_value
        else:
            print(f"Please enter from the following options: {', '.join(allowed_theme)}.")
            return False, None

    if key == "language":
        allowed_language = ["en", "es", "fr"]

        if value.lower() in allowed_language:
            return True, value.lower()
        else:
            print("Language must be either 'en', 'es', or 'fr'.")
            return False, None
        

    return True, value

def main():
    config = load_config()
    
    while True:
        print("Current configuration:")
        for key, value in config.items():
            print(f"{key}: {value}")
    
        print("-------------------------")
    
        target_setting = input("Enter the setting you want to modify (or 'exit' to quit):").strip().lower()
        
    
        if target_setting.lower() == "exit":
            print("Exiting the configuration editor.")
            break
        
        if target_setting not in config:
            print("Invalid setting. Please try again.")
            continue
        
        while True:
            new_value = input(f"Enter the new value for {target_setting}:")

            is_valid, validated_value = validate_setting(target_setting, new_value)

            if is_valid:
                config[target_setting] = validated_value
                save_config(config)
                break
            print(f"Please pick one from the list and try again.")

if __name__ == "__main__":
    main()


        