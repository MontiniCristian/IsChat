"""
    Written by:

    Montini Cristian: montinicristian@gmail.com
    Uberti Davide: ubertidavide@gmail.com
    For any question contact us via mail.
"""

import os
import socket
import threading
from time import sleep

banner = '''
                   ______     
                   \    /   _____    _____
                    |  |   / ____|  / ____| 
                    |  |  / /__    | /
                    |  |  \____ \  | |
                    |  |   ____\ \ | \____
                   /____\ |______/  \_____|

         '''

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
        self.port = 50
        self.banner = str(banner)

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
                threading.Thread(target=self.handler, args=(self.client, self.address), daemon=True).start()

            except KeyboardInterrupt:

                self.stop()

            except (ConnectionResetError,
                    ConnectionError, ConnectionAbortedError,
                    ConnectionRefusedError):

                self.connection_error()

    def handler(self, client, address):
        """
        This method hand the client (thread) and his connection
        with the server.

        :param client:
        :param address:
        """
        while True:

            self.server.send(banner.encode)

            while True:

                try:

                    data = client.recv(self.buffer_size)
                    if data:
                        print(str(data.decode()))


                    else:
                        print("Connection closed by client")
                        break

                except ConnectionAbortedError:

                    print("\n\nError!")
                    break
            break

    def stop(self):
        """
        This method is used to quit the server every time
        that is needed, like ctrl+C closing.
        """

        print("\nQuitting...\n\n")
        self.server.close()
        sleep(1)
        os.system("reset")
        exit()

    def connection_error(self):
        """
        This method is called every time the server has
        an error in runtime, like connection error.
        """

        print("Connection Error!\n\nAborted!")
        self.server.close()
        exit()


