import socket
import threading
import colorslib as clr
# import time
import os
import receiver

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
VSSERVER = receiver.VidstreamServer(SERVER, '`')
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!dsc'
RUNNING = True
COMMANDS = {
    '!help': 'Shows all commands available',
    '!stop': 'Stops the server',
    '!show-demo': 'Starts the vidstream server and asks for sender. Params: <nickname> <x_res> <y_res>',
    '!stop-demo': 'Stops the vidstream server. Params: <nickname>'}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
nicknames = []


def correct_send(f):
    def wrapped(*args):
        msg = args[-1]
        msg_len = len(msg)
        # print(f'Wrapped: msg=[{msg}]')
        # print(f'Wrapped: msg_len={msg_len}')
        msg = msg.encode(FORMAT)

        send_length = str(msg_len).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))  # send_length += b' ' * (HEADER - msg_len)

        if len(args) == 1:
            return f(msg, send_length)
        client = args[0]
        return f(client, msg, send_length)

    return wrapped


@correct_send  # broadcast(msg)
def broadcast(msg, length):
    for client in clients:
        client.send(length)
        client.send(msg)


@correct_send  # send(client, msg)
def send(client, msg, length):
    client.send(length)
    client.send(msg)


def kick(nickname):
    index = nicknames.index(nickname)
    client = clients[index]

    client.close()
    clients.pop(index)
    nicknames.pop(index)

    info(f'USER: {nickname} disconnected')
    show_active_connections(4)
    broadcast(f'User {clr.bcolors.OKGREEN}[{nickname}]{clr.bcolors.ENDC} disconnected')


# SERVER
def info(msg):
    print(clr.bcolors.WARNING + '[SERVER] ' + str(msg) + clr.bcolors.ENDC)


# SERVER
def user_message(msg):
    # print(clr.bcolors.OKGREEN + f'[USER:{addr}] {msg}' + clr.bcolors.ENDC, end='')
    print(clr.bcolors.OKGREEN + msg + clr.bcolors.ENDC)


# SERVER
def show_active_connections(default=0):
    info('Active connections: {}'.format(threading.active_count() - default))
    print(clr.bcolors.WARNING + '[SERVER] Active users: ' + clr.bcolors.ENDC, end='')
    print(nicknames)


def handle_client(conn, nickname):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:  # if msg[:-1] == DISCONNECT_MESSAGE: # for gui_client
                connected = False
                kick(nickname)
            else:
                user_message(msg)
                broadcast(msg)


def start():
    global RUNNING
    os.system('color')
    info('Starting server...')
    info(f'Server is running on {SERVER}')
    server.listen()
    while RUNNING:
        conn, addr = server.accept()

        send(conn, 'NICK')
        nickname = conn.recv(1024).decode(FORMAT)

        nicknames.append(nickname)
        clients.append(conn)

        info(f'User [{nickname}] connected on {addr}')
        show_active_connections(2)
        new_th = threading.Thread(target=handle_client, args=(conn, nickname))
        new_th.start()
        # time.sleep(1)
        broadcast(f'User {clr.bcolors.OKGREEN}[{nickname}]{clr.bcolors.ENDC} connected on {addr}')
        send(conn, f'Run {clr.bcolors.OKCYAN}!help{clr.bcolors.ENDC} to see available commands')


def write():
    while RUNNING:
        message = input()
        if not message.startswith('!'):
            message = clr.bcolors.WARNING + message + clr.bcolors.ENDC
            info(message)
            broadcast(message)
        else:
            msg_ar = message.split()
            if msg_ar[0] not in COMMANDS:
                info('Unknown command\n')
            else:
                if msg_ar[0] == '!help':
                    print('Available commands:')
                    for command, action in COMMANDS.items():
                        print(clr.bcolors.OKCYAN + f'{command}: ' + clr.bcolors.ENDC + action)
                elif msg_ar[0] == '!stop':
                    stop()
                elif msg_ar[0] == '!show-demo':
                    try:
                        nick = msg_ar[1]
                        x_res = msg_ar[2]
                        y_res = msg_ar[3]
                        VSSERVER.run()
                        index = nicknames.index(nick)
                        client = clients[index]
                        send(client, f'--showdemo {str(x_res)} {str(y_res)}')
                    except:
                        info('Incorrect command format')
                elif msg_ar[0] == '!stop-demo':
                    try:
                        nick = msg_ar[1]
                        index = nicknames.index(nick)
                        client = clients[index]
                        send(client, '--stopdemo')
                        # info('Trying to stop the server..')
                        try:
                            VSSERVER.stop()
                        except:
                            pass
                    except:
                        info('Incorrect command format')


def stop():
    # global RUNNING
    # RUNNING = False

    broadcast(f'{clr.bcolors.FAIL}The server has been stopped by administrator.'
              f'Please type anything in the shell to kill the tread and raise an exception!{clr.bcolors.ENDC}')
    broadcast(DISCONNECT_MESSAGE)

    try:
        server.close()
        exit(0)
    except:
        info('Huston, we got some troubles..')


start_thread = threading.Thread(target=start)
write_thread = threading.Thread(target=write)

start_thread.start()
write_thread.start()