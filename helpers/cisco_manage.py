import os
import json

class Cisco:

    def __init__(self) -> None:
        pass


    def create_user(username, password, self):

        output = os.popen('printf "'+password+'\n'+password+'\n"|ocpasswd -c /etc/ocserv/ocpasswd '+username+'').read()

        

        print(output)

        