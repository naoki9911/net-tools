import socket

PORT = 51820

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", PORT))
print("Listening...")

while True:
    message, addr = s.recvfrom(2)
    if len(message) < 2:
        continue

    send_size = int(message[0]) << 8 | int(message[1])
    print(send_size)
    send_buf = bytearray()
    for i in range(0, send_size):
        send_buf.append(i&0xFF)
    s.sendto(send_buf, addr)
