import threading
from vidstream import StreamingServer
import colorslib as clr


class VidstreamServer:

    def __init__(self, server_ip, qk='`'):
        self.server_ip = server_ip
        self.qk = qk

    def run(self):
        self.server = StreamingServer(self.server_ip, 9999, quit_key=self.qk)
        th = threading.Thread(target=self.server.start_server)
        th.start()
        print(f'{clr.bcolors.WARNING}[SERVER] Running vidstream server...{clr.bcolors.ENDC}')

    def stop(self):
        self.server.stop_server()
        print(f'{clr.bcolors.WARNING}[SERVER] Vidstream server is stopped{clr.bcolors.ENDC}')