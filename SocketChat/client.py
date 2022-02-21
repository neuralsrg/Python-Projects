import socket
import os
import colorslib as clr
import threading
import time
import sender
try:
    import playsound
except:
    os.system('pip install playsound')
    import playsound

PORT = 8080
SERVER = '192.168.68.115'
ADDR = (SERVER, PORT)
DEMOSENDER = None
HEADER = 64
FORMAT = 'utf-8'
SOUND_FILE = 'sound.wav'
DISCONNECT_MESSAGE = '!dsc'
COMMANDS = {
    '!help': 'Shows all commands available',
    '!dsc': 'Disconnects user from the server',
    '!online': 'Shows current online'}


class Client:

    def __init__(self, addr):

        os.system('color')
        self.nickname = ''
        while not self.nickname:
            self.nickname = input(clr.bcolors.WARNING + '[SERVER] ' + clr.bcolors.ENDC + 'Enter your nickname: ')

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr)

        self.running = True

        receive_thread = threading.Thread(target=self.receive)
        write_thread = threading.Thread(target=self.write)

        receive_thread.start()
        time.sleep(2)
        write_thread.start()

    def info(self, msg):
        print(clr.bcolors.WARNING + '[SERVER] ' + clr.bcolors.ENDC + str(msg))

    def send(self, msg):
        message = msg.encode(FORMAT)
        msg_len = len(message)
        send_length = str(msg_len).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))  # send_length += b' ' * (HEADER - msg_len)

        self.sock.send(send_length)
        self.sock.send(message)

    def receive(self):
        while self.running:
            try:
                msg_length = self.sock.recv(HEADER).decode(FORMAT)
                if msg_length:
                    try:
                        msg_length = int(msg_length)
                    except:
                        self.info(f'{clr.bcolors.FAIL}We got some message.. But could not decode it{clr.bcolors.ENDC}')
                        self.info('Please use only English letters')
                        continue
                    msg = self.sock.recv(msg_length).decode(FORMAT)

                    if msg == 'NICK':
                        self.sock.send(self.nickname.encode(FORMAT))
                    elif msg == DISCONNECT_MESSAGE:  # SERVER stops --> sends '!dsc' --> all users sends '!dsc' back
                        self.write(DISCONNECT_MESSAGE)
                    elif msg.startswith('--'):  # --showdemo 1920 1080
                        msg_ar = msg.split()
                        if msg.startswith('--showdemo'):
                            self.start_demo(int(msg_ar[1]), int(msg_ar[2]))
                        if msg.startswith('--stopdemo'):
                            # print('They want to stop server')
                            self.stop_demo()
                    else:
                        self.info(msg)
                        if msg.count(f'[{self.nickname}]') == 0 and msg.count('!help') == 0:
                            sound_thread = threading.Thread(target=self.sound)
                            sound_thread.start()
            except ConnectionAbortedError:
                break
            except Exception as ex:
                print('Error', ex)
                self.sock.close()
                exit(0)

    def write(self, message=None):
        while self.running:
            if not message:
                message = input()
            if not message.startswith('!'):
                message = clr.bcolors.OKGREEN + f"[{self.nickname}] " + clr.bcolors.ENDC + message
                self.send(message)
            else:
                if message not in COMMANDS:
                    self.info('Unknown command\n')
                else:
                    if message == '!help':
                        print('Available commands:')
                        for command, action in COMMANDS.items():
                            print(clr.bcolors.OKCYAN + f'{command}: ' + clr.bcolors.ENDC + action)
                    elif message == DISCONNECT_MESSAGE:
                        self.send(message)
                        self.stop()
                    elif message == '!online':
                        print('Not available yet')
            message = None

    def start_demo(self, x_res, y_res):
        DEMOSENDER = sender.VidstreamClient(SERVER, x_res, y_res)
        DEMOSENDER.start()

    def stop_demo(self):
        try:
            DEMOSENDER.stop()
        except:
            pass

    def sound(self):
        playsound.playsound(SOUND_FILE)
    def stop(self):
        self.running = False
        self.sock.close()
        exit(0)


client1 = Client(ADDR)


# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)
# connected = True
# info(f'Connected to {SERVER}')
