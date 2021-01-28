from time import sleep
import socket
from _thread import *
class TaeMe():
    class System:
        output = print
    class ConSoleSizeError(Exception):
        def __init__(self):
            return super().__init__('ConSoleSize Limit Error ::::')
    name = []
    a = None
    pink='\033[95m'
    black='\033[30m'
    Red='\033[31m'
    green='\033[32m'
    yellow='\033[33m'
    def __init__(self,fun):
        self.name.append([fun.__name__,fun])
    def _add(self,fun):
        self.name.append([fun.__name__, fun])
    def search(self,Taeget: str=""):
        for i,x in self.name:
            if i in Taeget:
                return x
    def run(self,color: str="",ConSoleTime: float=0.125,ConSolePost: str="/",ConSoleValue: str="=",Host: str="127.0.0.1",Port: int=8080,Error: str=None):
        def threaded(client_socket, addr,color,ConSoleTime,ConSolePost,ConSoleValue,Error):
            self.System.output('Connected by :', addr[0], ':', addr[1])
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    try:
                        def print(value):
                            client_socket.sendall(value.encode())
                        self.a = data.decode()
                        fun = self.search(self=self, Taeget=self.a)
                        if len(self.a.split(ConSolePost)) > 1:
                            for x, i in enumerate(self.a.split(ConSolePost)):
                                if x is not 0:
                                    console = i.split(ConSoleValue)
                                    code = fun.__code__
                                    if console[0] == str(code.co_varnames[0]):
                                        fun = self.search(self=self, Taeget=self.a.split(ConSolePost)[0])
                                        print(color + fun(console[1], content=self.a, color=color))
                                    else:
                                        raise Exception()
                        elif "ConSoleColor" in self.a:
                            if str(self.a.split(ConSoleValue)[1]) == "pink":
                                print("ConSoleColor -> pink")
                                color = self.pink
                            if str(self.a.split(ConSoleValue)[1]) == "black":
                                print("ConSoleColor -> black")
                                color = self.black
                            if str(self.a.split(ConSoleValue)[1]) == "green":
                                print("ConSoleColor -> green")
                                color = self.green
                            if str(self.a.split(ConSoleValue)[1]) == "red":
                                print("ConSoleColor -> red")
                                color = self.Red
                            if str(self.a.split(ConSoleValue)[1]) == "yellow":
                                print("ConSoleColor -> yellow")
                                color = self.yellow
                        elif "ConSoleTime" in self.a:
                            ConSoleTime = float(self.a.split(ConSoleValue)[1])
                            print("ConSoleTime -> " + str(float(self.a.split(ConSoleValue)[1])))
                        elif "ConSolePost" in self.a:
                            ConSolePost = str(self.a.split(ConSoleValue)[1])
                            print("ConSolePost -> " + str(self.a.split(ConSoleValue)[1]))
                        elif "ConSoleValue" in self.a:
                            ConSoleValue = str(self.a.split(ConSoleValue)[1])
                            print("ConSoleValue -> " + str(self.a.split(ConSoleValue)[1]))
                        elif "ConSoleError" in self.a:
                            Error = str(self.a.split(ConSoleValue)[1])
                            print("ConSoleError -> " + str(self.a.split(ConSoleValue)[1]))
                        elif "help" in self.a:
                            send = []
                            content = ""
                            for x, i in self.name:
                                code = i.__code__
                                send.append("-" + x + " " + "varnames : " + str(code.co_varnames) + "\n")
                            for i in send:
                                content += i
                            print(content)
                        elif "ConSole" in self.a:
                            print("ConSoleTime = " + str(ConSoleTime) + "\n" + "ConSoleValue = " + str(
                                ConSoleValue) + "\n" + "ConSolePost = " + str(
                                ConSolePost) + "\n" + "ConSoleError = " + str(Error) + "\n" + "ConSoleColor = " + str(
                                color))
                        else:
                            if fun(content=self.a, color=color) is not None:
                                print(color + fun(content=self.a, color=color))
                        self.System.output(
                            "CLIENT_HOST:" + str(addr[0]) + " :: CONTENT:" + self.a + " :: " + "PORT:" + str(Port))
                    except:
                        if Error is None:
                            self.System.output(
                                "CLIENT_HOST:" + str(addr[0]) + " :: CONTENT:" + self.a + " :: " + "PORT:" + str(Port))
                            print("Can't Found '" + self.a + "' Command")
                        else:
                            self.System.output(
                                "CLIENT_HOST:" + str(addr[0]) + " :: CONTENT:" + self.a + " :: " + "PORT:" + str(Port))
                            print(Error)
                    sleep(ConSoleTime)
                except ConnectionResetError as e:
                    self.System.output('Disconnected by ' + addr[0], ':', addr[1])
                    break
            client_socket.close()
        HOST = Host
        PORT = Port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print('server start')
        while True:
            print('wait')
            client_socket, addr = server_socket.accept()
            start_new_thread(threaded, (client_socket, addr,color,ConSoleTime,ConSolePost,ConSoleValue,Error))
        server_socket.close()
    def client_run(self,Host: str="127.0.0.1",Port: int=8080):
        HOST = Host
        PORT = Port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        while True:
            a = input(">")
            if a == "exit":
                break
            client_socket.sendall(a.encode())
            data = client_socket.recv(1024)
            print(data.decode())
        # 소켓을 닫습니다.
        client_socket.close()
if __name__ == '__main__':
    ThisMain = TaeMe
    @ThisMain
    def index(content,color):
        return "Hello, This funtion is main function. maker_email=taeho070607@naver.com, word!"
    print(ThisMain.name)
    ThisMain.run(self=ThisMain,Port=8000,ConSoleTime=0)
