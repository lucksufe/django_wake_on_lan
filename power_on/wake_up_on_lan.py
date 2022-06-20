import socket


def wake(mac):
    # Transform to magic packet
    data = ''.join(['FFFFFFFFFFFF', mac * 16])  # Magic packet string
    send_data = bytes.fromhex(data)  # String to bytes

    # Broadcast via socket
    destination = ('255.255.255.255', 9)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(send_data, destination)
