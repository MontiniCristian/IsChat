"""
    Written by:

    Montini Cristian: montinicristian@gmail.com
    Uberti Davide: ubertidavide@gmail.com
    For any question contact us via mail.
"""

import os
import socket
from time import sleep


class Client(object):
    def __init__(self):
        """
        Initialization of the main parameters by constructor
        """

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.login()
        self.buffer_size = 1024

    def login(self):
        """
        This method take the ip address and the port
        of the server from command line input.
        Nick authentication is going to be developed.
        """

        self.ip = input("[IP-SERVER] > ")
        self.port = input("[PORT] > ")
        # self.nick = input("[NINK] > ")

    def run(self):
        """
        This method run the client object and connect
        it to the server specified from login() function
        The client can be closed typing Q or q to quit,
        also you can press ctrl+c for quitting client.
        There will be a way to change color of the
        command line and the theme aspect (colored module).
        """

        os.system("clear")
        server_address = (self.ip, int(self.port))
        self.server.connect(server_address)
        banner = self.server.recv(self.buffer_size)
        print(banner.decode())
        while True:
            try:

                message = input("> ")
                if message == "q" or message == "Q":

                    self.stop()

                else:

                    self.server.send(message.encode())

            except (ConnectionAbortedError, ConnectionRefusedError,
                    ConnectionError, ConnectionResetError):

                self.connection_error()



            except KeyboardInterrupt:
                self.stop()

    def stop(self):
        """
        This method is used to quit the client every time
        that is needed, like an ConnectionError or whatever
        error could be throwed on runtime.
        """

        print("\nQuitting...\n\n")
        self.server.close()
        sleep(1)
        os.system("reset")
        exit()

    def connection_error(self):
        """
        This method is called when client can't communicate
        with the server anymore.
        """

        print("Connection Error!\n\nAborted!")
        self.server.close()
        exit()
