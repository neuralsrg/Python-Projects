import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import colorslib as clr

PORT = 8080
SERVER = '192.168.68.115'
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = '!dsc'
COMMANDS = ['!dsc']


class Client:

    def __init__(self, addr):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr)

        msg = tkinter.Tk()
        msg.withdraw()

        try:
            self.nickname = simpledialog.askstring('Nickname', 'Please choose a nickname', parent=msg)
        except Exception:
            self.stop()

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()


    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg='lightgray')

        self.chat_label = tkinter.Label(self.win, text='Chat', bg='lightgray')
        self.chat_label.config(font=('Arial', 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.config(state='disabled')
        self.text_area.pack(padx=20, pady=5)

        self.msg_label = tkinter.Label(self.win, text='Message', bg='lightgray')
        self.msg_label.config(font=('Arial', 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text='Send', command=self.write)
        self.send_button.config(font=('Arial', 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol('WM_DELETE_WINDOW', self.stop)

        self.win.mainloop()

    def info(self, msg):
        self.text_area.config(state='normal')
        self.text_area.insert('end', msg)
        self.text_area.yview('end')
        self.text_area.config(state='disabled')

    def receive(self):
        while self.running:
            try:
                msg_length = self.sock.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = self.sock.recv(msg_length).decode(FORMAT)

                    if msg == 'NICK':
                        self.sock.send(self.nickname.encode(FORMAT))
                    else:
                        if self.gui_done:
                            self.info(msg)
            except ConnectionAbortedError:
                break
            except Exception as ex:
                print('Error', ex)
                self.sock.close()
                exit(0)

    def send(self, msg):
        message = msg.encode(FORMAT)
        msg_len = len(message)
        send_length = str(msg_len).encode(FORMAT)
        send_length += b' ' * (HEADER - msg_len)

        self.sock.send(send_length)
        self.sock.send(message)

    def write(self):
        message = self.input_area.get('1.0', 'end')
        if not message.startswith('!'):
            message = f"[{self.nickname}] {message}"
            self.send(message)
        else:
            if message[:-1] not in COMMANDS:
                self.info('Unknown command\n')
            else:
                if message[:-1] == COMMANDS[0]:
                    self.send(message)
                    self.stop()
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

client1 = Client(ADDR)