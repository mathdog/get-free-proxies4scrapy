import re


print("Reading proxies.txt...")

with open('proxies.txt') as f:
    content = f.readlines()

#clean proxy data
proxy_lines = "\n"
for i in content:
    match = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', i)
    proxy_lines += "'" + match[0] + "'," + "\n"

print("Cleaning proxies format...")
print(proxy_lines)


#read settings.py
with open('settings.py', 'r') as f:
    settings_file = f.read()

#print(settings_file)
settings_content = ''.join(re.findall(r'ROTATING_PROXY_LIST = \[((.|\n)*?)\]', settings_file)[0])
print(settings_content)
proxies2replace = re.findall(r"'(.*?)',?", settings_content)
print(proxies2replace)


#replace old proxies
for line in iter(settings_file.splitlines()):
    for proxy in proxies2replace:
        if proxy in line:
            settings_file = settings_file.replace(line+'\n', '') 

settings_file = settings_file.replace('ROTATING_PROXY_LIST = [\n', 'ROTATING_PROXY_LIST = ['+proxy_lines)
#print(settings_file)


#save the changes to the settings file
with open('settings.py', 'w') as f:
    f.write(settings_file)

print('\n***Done!***\n')