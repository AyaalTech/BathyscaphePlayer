import json

# Read the existing config.json file
with open('../RTSPtoWebRTC/config.json', 'r') as file:
    config = json.load(file)

# Modify the desired values
config['server']['http_port'] = ':8083'
config['server']['ice_servers'] = ['stun:stun.example.com:19302']
config['streams']['Bathyscaphe']['disable_audio'] = False
config['streams']['Bathyscaphe']['url'] = 'rtsp://admin:12345@95.154.86.198:554/'

# Write the modified config back to config.json
with open('../RTSPtoWebRTC/config.json', 'w') as file:
    json.dump(config, file, indent=4)