import time
from datetime import datetime as dt

hosts_path="/etc/hosts"
redirect="127.0.0.1"
print("Type in the website[s] you want to avoid:")
website_to_block = input("A website should follow the format <www.websitename.com>. Delimiter being used is ' '.\n")
if " " in website_to_block.strip():
    website_list = website_to_block.split(" ")
    for website in website_list:
        website.strip()
else:
    website_list = [website_to_block.strip()]

hour1 = input("Enter the time you want to start blocking the websites (24hr format)")
hour2 = input("Enter the time you want to start blocking the websites (24hr format)")

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, int(hour1)) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, int(hour2)):
        print("The specified websites have been disabled.")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("The specified websites have been enabled.")
    time.sleep(5)
