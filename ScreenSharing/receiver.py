import sys
import threading
from vidstream import StreamingServer

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('You have to specify your IPv4 address & quit key (optional)')
    exit()

print('\n\nTYPE "STOP" TO STOP THE SERVER')
SERVER_IP = sys.argv[1]

if len(sys.argv) == 3:
    qk = sys.argv[2]
else:
    qk = '`'
    print('WARNING! EXIT QEY BY DEFAULT IS "`"')
print('\n\nRUNNING SERVER')


server = StreamingServer(SERVER_IP, 9999, quit_key=qk)
th = threading.Thread(target=server.start_server)
th.start()

# Other Code
while input() != 'STOP':
    continue

# When You Are Done
server.stop_server()