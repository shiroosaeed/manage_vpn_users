import os
import json

class Ovpn:

    def __init__(self) -> None:
        pass


    def create_user(self,config):

        cmd =f''
        output = os.popen(cmd).read()

        

        print(output)
        print(cmd)

        