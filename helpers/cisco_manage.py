import os
import json

class Cisco:

    def __init__(self) -> None:
        pass


    def create_user(self,username, password):

        cmd =f'printf "{password}\n{password}\n"|ocpasswd -c /etc/ocserv/ocpasswd {username}'
        output = os.popen(cmd).read()

        

        print(output)
        print(cmd)

        