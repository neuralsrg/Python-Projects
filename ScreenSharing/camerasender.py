import sys
from vidstream import CameraClient

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('You have to specify server IPv4 address & resolution (1920x1080) (optional)')
    exit()
print('\n\nTYPE "STOP" TO STOP THE SERVER')

RES = [1920, 1080]

SERVER_IP = sys.argv[1]
if len(sys.argv) == 3:
    RES = [int(i) for i in sys.argv[2].split('x')]


client = CameraClient(SERVER_IP, 9999, RES[0], RES[1])

client.start_stream()

while input() != 'STOP':
    continue

client.stop_stream()