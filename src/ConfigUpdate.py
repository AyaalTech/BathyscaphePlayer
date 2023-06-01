import json
from colorama import Fore, Style

def create_json():
    config = {}
    server = {}
    server["http_port"] = input("Enter http_port: ")
    server["ice_servers"] = [input("Enter ice_server: ")]
    config["server"] = server
    streams = {}
    while True:
        stream_name = input("Enter stream name (or type 'exit' to finish): ")
        if stream_name.lower() == "exit":
            break
        stream = {}
        stream["deviceNumber"] = input("Enter deviceNumber: ")
        stream["on_demand"] = input("Enter on_demand (True/False): ").lower() == "true"
        stream["disable_audio"] = input("Enter disable_audio (True/False): ").lower() == "true"
        stream["url"] = input("Enter URL: ")
        streams[stream_name] = stream
    config["streams"] = streams
    return config

print(Fore.CYAN + r'''
╋╋╋╋╋╋╋╋╋┏━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓
╋╋╋╋╋╋╋╋╋┃┏┛╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓
┏━━┳━━┳━┳┛┗┳┳━━┓┏━━┳━┳━━┳━┻┓┏╋━━┳━┓
┃┏━┫┏┓┃┏╋┓┏╋┫┏┓┃┃┏━┫┏┫┃━┫┏┓┃┃┃┏┓┃┏┛
┃┗━┫┗┛┃┃┃┃┃┃┃┗┛┃┃┗━┫┃┃┃━┫┏┓┃┗┫┗┛┃┃
┗━━┻━━┻┛┗┻┛┗┻━┓┃┗━━┻┛┗━━┻┛┗┻━┻━━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
    ''' + Style.RESET_ALL)

print(Fore.YELLOW + "Welcome to config creator! To start creating, type 'c'. To use the demo list, type 'd'. To add a stream to an existing config, type 'w'")
user_input = input(Style.BRIGHT)
print(Style.RESET_ALL)

if user_input.lower() == 'c':
    config = create_json()
    config_json = json.dumps(config, indent=4)
    print(Fore.GREEN + config_json + Style.RESET_ALL)
    with open("../RTSPtoWebRTC/config.json", "w") as file:
        file.write(config_json)
        print(Fore.YELLOW + "Config JSON written to file." + Style.RESET_ALL)

elif user_input.lower() == 'd':
    demo_list = {
        "server": {
            "http_port": ":8083",
            "ice_servers": [
                "stun:stun.example.com:19302"
            ]
        },
        "streams": {
            "Japan": {
                "deviceNumber": "Not Russia",
                "on_demand": False,
                "disable_audio": False,
                "url": "rtsp://admin:12345@95.154.86.198:554/"
            },
            "Vladivostok": {
                "deviceNumber": "Russia",
                "on_demand": False,
                "disable_audio": False,
                "url": "rtsp://admin:12345@95.154.69.152:554/"
            }
        }
    }
    demo_json = json.dumps(demo_list, indent=4)
    print(Fore.GREEN + demo_json + Style.RESET_ALL)

    with open("../RTSPtoWebRTC/config.json", "w") as file:
        file.write(demo_json)
        print(Fore.YELLOW + "Demo JSON written to file." + Style.RESET_ALL)

    while True:
        print(Fore.YELLOW + "Do you want to continue working? (y/n)" + Style.RESET_ALL)
        continue_input = input().lower()
        if continue_input == 'y':
            user_input = input("Enter 'c' to create a new JSON, 'd' to print the demo JSON, or 'w' to add a stream to an existing config: ")
            if user_input.lower() == 'c':
                config = create_json()
                config_json = json.dumps(config, indent=4)
                print(Fore.GREEN + config_json + Style.RESET_ALL)
                with open("../RTSPtoWebRTC/config.json", "w") as file:
                    file.write(config_json)
                    print(Fore.YELLOW + "Config JSON written to file." + Style.RESET_ALL)
            elif user_input.lower() == 'd':
                demo_json = json.dumps(demo_list, indent=4)
                print(Fore.GREEN + demo_json + Style.RESET_ALL)
            elif user_input.lower() == 'w':
                existing_config_path = "../RTSPtoWebRTC/config.json"
                try:
                    with open(existing_config_path, "r") as file:
                        existing_config = json.load(file)
                except FileNotFoundError:
                    print(Fore.RED + "Existing config file not found." + Style.RESET_ALL)
                    continue
                new_stream_name = input("Enter stream name: ")
                new_stream = {}
                new_stream["deviceNumber"] = input("Enter deviceNumber: ")
                new_stream["on_demand"] = input("Enter on_demand (True/False): ").lower() == "true"
                new_stream["disable_audio"] = input("Enter disable_audio (True/False): ").lower() == "true"
                new_stream["url"] = input("Enter URL: ")
                existing_config["streams"][new_stream_name] = new_stream
                with open(existing_config_path, "w") as file:
                    file.write(json.dumps(existing_config, indent=4))
                    print(Fore.YELLOW + "Stream added to existing config." + Style.RESET_ALL)
        elif continue_input == 'n':
            print(Fore.YELLOW + "Program ended." + Style.RESET_ALL)
            break