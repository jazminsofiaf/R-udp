from rudp.rudp_socket import RudpSocket
import time

CLI_SEND_ADDR = ('127.0.0.1', 5000)
SV_RECV_ADDR = ('127.0.0.1', 9001)
BUFSIZE = 1024
IS_CLIENT = True

def main():
    print('init client')

    rudp = RudpSocket(CLI_SEND_ADDR)
    rudp.sendto(b'start', SV_RECV_ADDR)
    data, addr = rudp.recvfrom(BUFSIZE)

    for i in range(100):
        rudp.sendto('msg {}'.format(i), SV_RECV_ADDR)

    rudp.sendto(b'fin', SV_RECV_ADDR)
    data, addr = rudp.recvfrom(BUFSIZE)

    time.sleep(7)
    rudp.close()

    print('end client')

main()
