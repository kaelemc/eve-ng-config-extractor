import os
import base64
import xml.etree.ElementTree as ET
import re

configs = []

filename = "CCIE SP bootcamp ch02-ipv6.unl"

with open(f"./{filename}") as file:
    tree = ET.parse(file)
    root = tree.getroot()
    
    for cfg in root.iter('config'):
        cfg2 = base64.b64decode(cfg.text)
        # print(cfg.text)
        configs.append(cfg2)

print(configs[1].decode())

export_dir_path = f"./export-{filename}"

try:
    os.makedirs(export_dir_path)
except:
    print(f"Couldn't make {export_dir_path}, Does this directory already exist?")

for config in configs:
    hostname = re.search("hostname .*$", config.decode(), re.MULTILINE)
        
    with open(f"{export_dir_path}/{hostname.group(0).strip("hostname ")}.cfg", "w") as cfg_file:
        cfg_file.write(config.decode())