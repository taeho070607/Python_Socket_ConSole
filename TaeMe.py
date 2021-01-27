from time import sleep
import socket
import speedtest
class TaeMe():
    name = []
    a = None
    pink='\033[95m'
    black='\033[30m'
    Red='\033[31m'
    green='\033[32m'
    yellow='\033[33m'
    def __init__(self,fun):
        TaeMe.name.append([fun.__name__,fun])
    def search(self,Taeget):
        for i,x in self.name:
            if i in Taeget:
                return x
    def run(self,color="",ConSoleTime=0.125,ConSolePost="/",ConSoleValue="=",Host="127.0.0.1",Port=8080):

        # 접속할 서버 주소입니다. 여기에서는 루프백(loopback) 인터페이스 주소 즉 localhost를 사용합니다.
        HOST = Host

        # 클라이언트 접속을 대기하는 포트 번호입니다.
        PORT = Port

        # 소켓 객체를 생성합니다.
        # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 포트 사용중이라 연결할 수 없다는
        # WinError 10048 에러 해결를 위해 필요합니다.
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
        # HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
        # 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다.
        # PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.
        server_socket.bind((HOST, PORT))

        # 서버가 클라이언트의 접속을 허용하도록 합니다.
        server_socket.listen()

        # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
        client_socket, addr = server_socket.accept()
        # 무한루프를 돌면서
        while True:
            # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
            data = client_socket.recv(1024)
            # 빈 문자열을 수신하면 루프를 중지합니다.
            if not data:
                break
            def print(value):
                client_socket.sendall(value.encode())
            TaeMe.a = data.decode()
            fun = TaeMe.search(self=TaeMe, Taeget=TaeMe.a)
            if len(TaeMe.a.split(ConSolePost)) > 1:
                for x, i in enumerate(TaeMe.a.split(ConSolePost)):
                    if x is not 0:
                        console = i.split(ConSoleValue)
                        if console[0] == "value":
                            fun = TaeMe.search(self=TaeMe, Taeget=TaeMe.a.split(ConSolePost)[0])
                            print(color + fun(console[1], content=TaeMe.a, color=color))
            elif "ConSoleColor" in TaeMe.a:
                if str(TaeMe.a.split(ConSoleValue)[1]) == "pink":
                    print("ConSoleColor -> pink")
                    color = TaeMe.pink
                if str(TaeMe.a.split(ConSoleValue)[1]) == "black":
                    print("ConSoleColor -> black")
                    color = TaeMe.black
                if str(TaeMe.a.split(ConSoleValue)[1]) == "green":
                    print("ConSoleColor -> green")
                    color = TaeMe.green
                if str(TaeMe.a.split(ConSoleValue)[1]) == "red":
                    print("ConSoleColor -> red")
                    color = TaeMe.Red
                if str(TaeMe.a.split(ConSoleValue)[1]) == "yellow":
                    print("ConSoleColor -> yellow")
                    color = TaeMe.yellow
            elif "ConSoleTime" in TaeMe.a:
                ConSoleTime = float(TaeMe.a.split(ConSoleValue)[1])
                print("ConSoleTime -> " + str(float(TaeMe.a.split(ConSoleValue)[1])))
            elif "ConSolePost" in TaeMe.a:
                ConSolePost = str(TaeMe.a.split(ConSoleValue)[1])
                print("ConSolePost -> " + str(TaeMe.a.split(ConSoleValue)[1]))
            elif "ConSoleValue" in TaeMe.a:
                ConSoleValue = str(a.split(ConSoleValue)[1])
                print("ConSoleValue -> " + str(TaeMe.a.split(ConSoleValue)[1]))
            elif "help" in TaeMe.a:
                for x, i in TaeMe.name:
                    print("-" + x + " ")
            else:
                if fun(content=TaeMe.a, color=color) is not None:
                    print(color + fun(content=TaeMe.a, color=color))
            sleep(ConSoleTime)
            # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)

        # 소켓을 닫습니다.
        client_socket.close()
        server_socket.close()
    def client_run(self,Host="127.0.0.1",Port=8080):
        HOST = Host
        # 서버에서 지정해 놓은 포트 번호입니다.
        PORT = Port


        # 소켓 객체를 생성합니다.
        # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
        client_socket.connect((HOST, PORT))
        while True:
            a = input(">")
            # 메시지를 전송합니다.
            client_socket.sendall(a.encode())

            # 메시지를 수신합니다.
            data = client_socket.recv(1024)
            print(data.decode())

        # 소켓을 닫습니다.
        client_socket.close()
