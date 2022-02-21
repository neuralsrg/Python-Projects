import sys
from vidstream import VideoClient

if len(sys.argv) != 3:
    print('You have to specify server IPv4 address & address to the .mp4 file')
    exit()


SERVER_IP = sys.argv[1]
VID_ADR = sys.argv[2]

print('\n\nTYPE "STOP" TO STOP THE SERVER')

client = VideoClient(SERVER_IP, 9999, VID_ADR)

client.start_stream()

while input() != 'STOP':
    continue

client.stop_stream()