"""
    Written by:

    Montini Cristian: montinicristian@gmail.com
    Uberti Davide: ubertidavide@gmail.com
    For any question contact us via mail.
"""

import socket
import threading
from time import sleep


# Written by Montini Cristian and Uberti Davide



class Server(object):

    def __init__(self):
        """
        Constructor: initialize server variables.

        """
        super().__init__()
        self.client = None
        self.address = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer_size = 1024
        self.host = 'localhost'
        self.port = 49

    def run(self):

        """
        This method run the server and create a thread
        for handle every new client that could be connected to.

        """

        print("Starting server " + self.host + " on port " + str(self.port))
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        while True:
            try:
                client, address = self.server.accept()
                # Look the signal module to handle the closing thread
                threading.Thread(target=self.handler, args=(client, address)).start()

            except KeyboardInterrupt:
                print("\n\nQuitting..")
                break

    def handler(self, client, address):
        """
        This method hand the client (thread) and his connection
        with the server.

        :param client:
        :param address:
        :return:
        """
        while True:

            self.print_banner(client)

            while True:

                try:
                    data = client.recv(self.buffer_size)
                    if data:
                        print(str(data.decode()))

                    else:
                        print("Connection closed by client")
                        break

                except:
                    print("\n\nError!")
                    break
            break

    @staticmethod
    def print_banner(client):
        """
        This method send the server banner to the client before
        starting messaging.
        The banner will be customizable by the user modifying it
        from a configuration file.

        :param client:
        :return:
        """
        banner = '''
                   ______     
                   \    /   _____    _____
                    |  |   / ____|  / ____| 
                    |  |  / /__    | /
                    |  |  \____ \  | |
                    |  |   ____\ \ | \____
                   /____\ |______/  \_____|
              
              '''

        client.send(banner.encode())
