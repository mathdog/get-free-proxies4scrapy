import re

print("Reading proxies.txt...")

with open('proxies.txt') as f:
    content = f.readlines()

proxy_lines = "\n"
for i in content:
    match = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', i)
    proxy_lines += "'" + match[0] + "'," + "\n"

print("Cleaning proxies format...")
print(proxy_lines)


#reading settings.py
with open('settings.py', 'r') as f:
    settings_file = f.read()
    
settings_content = ''.join(re.findall(r'ROTATING_PROXY_LIST = \[((.|\n)*?)\]', settings_file)[0])
print(settings_content)
settings_file = settings_file.replace(settings_content, proxy_lines)
#print(settings_file)

with open('settings.py', 'w') as f:
    f.write(settings_file)

print('\n***Done!***\n')


