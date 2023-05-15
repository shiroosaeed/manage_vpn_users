import os
import json

class Cisco:

    def __init__(self) -> None:
        pass


    def create_user(username, password, self) -> bool:

        output = os.popen(f'printf "{password}\n{password}\n"|ocpasswd -c /etc/ocserv/ocpasswd {username}').read()

        out = json.loads(output)

        print(out)

        