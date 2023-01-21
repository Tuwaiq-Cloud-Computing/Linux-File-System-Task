import os
from datetime import date
from datetime import timedelta

dir_names = ["Accounting", "HR", "Engineering"]

# Create all directories and text files
for d in dir_names:
    os.makedirs(d, exist_ok=True)                                #create dir
    os.chdir(d)                                                  #change to new dir
    for x in range(5):                                           #loop 5 times and create 5 txt files
        open(f'{d[0:3].lower()}_{str(x + 1)}.txt', "x")          #create txt file name = first 3 letters of dir + _index
    os.chdir("..")                                               #go up dir

today = date.today()
encPass = "P@ssword123!"
expirationDate = today + timedelta(days=1095)

user_groups = [
    {
        "groupName": "CEO",
        "users": [
            {
                "name": "anas",
                "role": "CEO"
            }
        ]
    },
    {
        "groupName": "Accounting",
        "users": [
            {
                "name": "salwa",
                "role": "Accountant"
            },
            {
                "name": "rasha",
                "role": "Accountant"
            }
        ]
    },
    {
        "groupName": "HR",
        "users": [
            {
                "name": "ali",
                "role": "HRManager"
            },
            {
                "name": "hazem",
                "role": "HREmployee"
            }
        ]
    },
    {
        "groupName": "Engineering",
        "users": [
            {
                "name": "ahmad",
                "role": "Engineer"
            },
            {
                "name": "yaman",
                "role": "Engineer"
            }
        ]
    }
]

for index, group in enumerate(user_groups):
    os.system(f'groupadd {group["groupName"]}')
    for user in group["users"]:
        os.system(
            f'useradd {user["name"]}\
             --comment {user["role"]}\
               --groups {group["groupName"]}\
                --password {encPass}\
                  ')
        if user["role"] != "CEO" or "Manager" not in user["role"]:
            os.system(f'usermod {user["name"]} --expiredate {expirationDate}')

        if group["groupName"] != "CEO":
            os.system(f'chown -R {user["name"]}:{group["groupName"]} {group["groupName"]}')
            os.system(f'chmod ug+rwx {group["groupName"]}')

bakup_name = "Tuwaiq-bkup-" + str(date.today())
os.makedirs(f'/tmp/backups/{bakup_name}', exist_ok=True)
os.system(f'cp -R -v . /tmp/backups/{bakup_name}')
