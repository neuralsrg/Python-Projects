from vidstream import ScreenShareClient

class VidstreamClient:

    def __init__(self, server_ip, x_res, y_res):
        self.server_ip = server_ip
        self.x_res = x_res
        self.y_res = y_res

    def start(self):
        self.client = ScreenShareClient(self.server_ip, 9999, self.x_res, self.y_res)
        self.client.start_stream()

    def stop(self):
        try:
            self.client.stop_stream()
        except:
            pass