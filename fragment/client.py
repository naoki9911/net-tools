import sys
import socket

PORT = 51820

dst_addr = sys.argv[1]
send_size = int(sys.argv[2])
print("dst_addr={} send_size={} ".format(dst_addr, send_size), end='')

buf = bytes([(send_size >> 8) & 0xFF, send_size & 0xFF])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1.0)
s.bind(("0.0.0.0", 0))

success = False
for i in range(0, 3):
    try:
        s.sendto(buf, (dst_addr, PORT))
        print("Sent. ", end='')
        buf = s.recv(send_size)
        print("Recv.(size={})".format(len(buf)))
        success = True
        break
    except socket.timeout:
        print("Retrying... ", end='')
        continue

if success:
    sys.exit(0)
else:
    print("Cannot receive response(size={})".format(send_size))
    sys.exit(1)
