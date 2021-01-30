from time import sleep
import socket
from _thread import *
import winsound
from gtts import gTTS
from playsound import playsound
import tkinter as tk
import os
class TaeMe():
    class System:
        output = print
    class ConSoleSizeError(Exception):
        def __init__(self):
            return super().__init__('ConSoleSize Limit Error ::::')
    class ConSoleReturnNone(Exception):
        def __init__(self):
            return super().__init__('None')
    name = []
    users=[]
    ban_users=[]
    max_users=None
    accumulate_users=[]
    event=False
    sound=True
    sound_frequency_No_expect = 300
    sound_duration_No_expect = 250
    sound_frequency_expect = 200
    sound_duration_expect = 250
    sound_frequency_max = 767
    sound_frequency_min = 37
    BanMessage: str = "You Are Banned On This Server"
    FullMessage: str = "Server Is Fulled"
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
    def run(self,color: str="",ConSoleTime: float=0.125,ConSolePost: str="/",ConSoleValue: str="=",Host: str="127.0.0.1",Port: int=8080,Error: str=None,Server: str=None,Admin: bool=False):
        # 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
        def threaded(client_socket, addr,color,ConSoleTime,ConSolePost,ConSoleValue,Error,Server,Admin):
            connect = gTTS(text=f"{addr[0]}님이 접속했습니다.",lang="ko")
            connect.save("connect.mp3")
            playsound("connect.mp3")
            os.remove("connect.mp3")
            ADMIN=False
            def print(value):
                client_socket.sendall(value.encode())
                return value
            self.System.output('Connected by :', addr[0], ':', addr[1])
            ok2: int=0
            if Admin is False and Server is not None:
                if addr[0] == Server:
                    ADMIN=True
                    self.users.append(addr[0])
                    self.accumulate_users.append(addr[0])
                else:
                    if self.max_users is None:
                        for i in self.ban_users:
                            if i == addr[0]:
                                ok2 += 1
                                print(self.BanMessage)
                                return 0
                        if ok2 is not 1:
                            self.users.append(addr[0])
                            self.accumulate_users.append(addr[0])
                    else:
                        if len(self.users) > self.max_users:
                            print(self.FullMessage)
                            return 0
                        else:
                            for i in self.ban_users:
                                if i == addr[0]:
                                    ok2 += 1
                                    print(self.BanMessage)
                                    return 0
                            if ok2 is not 1:
                                self.users.append(addr[0])
                                self.accumulate_users.append(addr[0])
            else:
                ADMIN = True
                if self.max_users is None:
                    for i in self.ban_users:
                        if i == addr[0]:
                            ok2 += 1
                            print(self.BanMessage)
                            return 0
                    if ok2 is not 1:
                        self.users.append(addr[0])
                        self.accumulate_users.append(addr[0])
                else:
                    if len(self.users) > self.max_users:
                        print(self.FullMessage)
                        return 0
                    else:
                        for i in self.ban_users:
                            if i == addr[0]:
                                ok2 += 1
                                print(self.BanMessage)
                                return 0
                        if ok2 is not 1:
                            self.users.append(addr[0])
                            self.accumulate_users.append(addr[0])
            # 클라이언트가 접속을 끊을 때 까지 반복합니다.
            while True:
                try:
                    # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    try:
                        self.a = data.decode()
                        admin = {"ConSoleAddr": addr,
                                 "ConSoleTime": ConSoleTime,
                                 "ConSolePost": ConSolePost,
                                 "ConSoleValue": ConSoleValue,
                                 "ConSoleColor": color,
                                 "ConSoleError": Error}
                        fun = self.search(self=self, Taeget=self.a)
                        try:
                            code = fun.__code__
                        except:
                            code = None
                        if len(self.a.split(ConSolePost)) > 1:
                            self.event=True
                            for x, i in enumerate(self.a.split(ConSolePost)):
                                if x is not 0:
                                    console = i.split(ConSoleValue)
                                    code = fun.__code__
                                    ok = 0
                                    value=console[1].split(",")
                                    for i in code.co_varnames:
                                        if i=="admin":
                                            ok+=1
                                            if console[0] == str(code.co_varnames[0]):
                                                fun = self.search(self=self, Taeget=self.a.split(ConSolePost)[0])
                                                print(color + fun(value, content=self.a, color=color,admin=admin))
                                            else:
                                                raise Exception()
                                    if ok is 0:
                                        if console[0] == str(code.co_varnames[0]):
                                            fun = self.search(self=self,Taeget=self.a.split(ConSolePost)[0])
                                            print(color + fun(value,content=self.a,color=color))
                                        else:
                                            raise Exception()
                        elif code is not None and len(code.co_varnames) > 2:
                            self.event = True
                            for i in code.co_varnames:
                                if i == "admin":
                                    print(fun(admin=admin,content=self.a,color=color))
                        elif "ConSoleColor" in self.a:
                            self.event = True
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
                            self.event = True
                            ConSoleTime = float(self.a.split(ConSoleValue)[1])
                            print("ConSoleTime -> " + str(float(self.a.split(ConSoleValue)[1])))
                        elif "ConSolePost" in self.a:
                            self.event = True
                            ConSolePost = str(self.a.split(ConSoleValue)[1])
                            print("ConSolePost -> " + str(self.a.split(ConSoleValue)[1]))
                        elif "ConSoleValue" in self.a:
                            self.event = True
                            ConSoleValue = str(self.a.split(ConSoleValue)[1])
                            print("ConSoleValue -> " + str(self.a.split(ConSoleValue)[1]))
                        elif "ConSoleError" in self.a:
                            self.event = True
                            Error = str(self.a.split(ConSoleValue)[1])
                            print("ConSoleError -> " + str(self.a.split(ConSoleValue)[1]))
                        elif "help" in self.a:
                            self.event = True
                            send = []
                            content = ""
                            for x, i in self.name:
                                code = i.__code__
                                send.append("-" + x + " " + "varnames : " + str(code.co_varnames) + "\n")
                            for i in send:
                                content += i
                            print(content)
                        elif "ConSole" in self.a:
                            self.event = True
                            print("ConSoleTime = " + str(ConSoleTime) + "\n" + "ConSoleValue = '" + str(
                                ConSoleValue) + "'\n" + "ConSolePost = '" + str(
                                ConSolePost) + "'\n" + "ConSoleError = '" + str(Error) + "'\n" + "ConSoleColor = " + str(
                                color))
                        elif ADMIN:
                            if "ServerByUsers" in self.a:
                                self.event = True
                                print(str(self.users))
                            elif "ServerByBanUsers" in self.a:
                                self.event = True
                                print(str(self.ban_users))
                            elif "ServerByAccumulate" in self.a:
                                self.event=True
                                print(str(self.accumulate_users))
                            elif "ServerByBanMessage" in self.a:
                                self.event = True
                                self.BanMessage = str(self.a.split(ConSoleValue)[1])
                                print("ConSoleError -> " + str(self.a.split(ConSoleValue)[1]))
                            elif "ServerByStatus" in self.a:
                                self.event = True
                                print("ServerByUsers(Online) = " + str(len(self.users))+"\n"+"ServerByBanUsers = "+str(len(self.ban_users))+"\n"+"ServerByAccumulateUsers = "+str(len(self.accumulate_users))+"\n"+"ServerByMaxUsers = "+str(self.max_users)+"\n"+"ServerByBanMessage = "+str(self.BanMessage)+"\n"+"ServerByFullUsersMessage = "+str(self.FullMessage))
                            elif "ServerByFullUsersMessage" in self.a:
                                self.event = True
                                self.FullMessage = str(self.a.split(ConSoleValue)[1])
                                print("ServerByFullUsersMessage -> " + str(self.a.split(ConSoleValue)[1]))
                            else:
                                value = print(color + fun(content=self.a, color=color))
                                if value is None:
                                    print(" ")
                        else:
                            value = print(color + fun(content=self.a, color=color))
                            if value is None:
                                print(" ")
                        self.event=False
                        self.System.output(
                            "CLIENT_HOST:" + str(addr[0]) + "|" + str(
                                addr[1]) + " :: CONTENT:" + self.a + " :: " + "PORT:" + str(Port))
                        if self.sound is True:
                            winsound.Beep(frequency=self.sound_frequency_No_expect, duration=self.sound_duration_No_expect)
                    except:
                        if Error is None:
                            self.event = False
                            self.System.output(
                                "CLIENT_HOST:" + str(addr[0]) + "|" + str(
                                    addr[1]) + " :: CONTENT:" + self.a + " :: " + "PORT:" + str(Port))
                            print(f"Can't Found '{self.a}' Command")
                        else:
                            self.event = False
                            self.System.output(
                                "CLIENT_HOST:" + str(addr[0]) + "|" + str(
                                    addr[1]) + " :: CONTENT:" + self.a + " :: " + "PORT:" + str(Port))
                            print(Error)
                        if self.sound is True:
                            winsound.Beep(frequency=self.sound_frequency_expect,duration=self.sound_duration_expect)
                    sleep(ConSoleTime)
                    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
                except ConnectionResetError as e:
                    self.System.output('Disconnected by ' + addr[0], ':', addr[1])
                    Wait = gTTS(text=f"{addr[0]}님이 접속을 종료했습니다.", lang='ko')
                    Wait.save("disconnect.mp3")
                    playsound("disconnect.mp3")
                    os.remove("disconnect.mp3")
                    self.users.remove(addr[0])
                    break

            client_socket.close()
        try:
            HOST = Host
            PORT = Port
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            # 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.
            ServerRun = gTTS(text='서버를 시작합니다.', lang='ko')
            ServerRun.save("ServerRun.mp3")
            playsound("ServerRun.mp3")
            os.remove("ServerRun.mp3")
            print("ServerRun ..........[O]")
            # 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.
            try:
                while True:
                    Wait = gTTS(text='대기중', lang='ko')
                    Wait.save("wait.mp3")
                    playsound("wait.mp3")
                    os.remove("wait.mp3")
                    print("wait ..........[O]")
                    client_socket, addr = server_socket.accept()
                    start_new_thread(threaded, (client_socket, addr,color,ConSoleTime,ConSolePost,ConSoleValue,Error,Server,Admin))
            except:
                print("Error[02]: Connect Fail")
                playsound("sound\\Nuclear.mp3")

            server_socket.close()
        except:
            print("Error[01]: ServerRun Fail")
            playsound("sound\\Nuclear.mp3")
    def display_run(self):
        global run
        run = False
        calc = tk.Tk()
        calc.geometry("300x300")
        calc.title("Socket_ConSole")
        def thread(event):
            global run
            if run:
                return 0
            else:
                run = True
                text.set("ServerStatus : True")
            def fun(event):
                self.run(self=self, Host=str(tk.Entry.get(display)), Port=int(tk.Entry.get(display2)),
                           Server=str(tk.Entry.get(display)))
            start_new_thread(fun, (event,))
        display = tk.Entry(calc, width=20)
        display2 = tk.Entry(calc, width=20)
        button = tk.Button(calc, text="ServerStart", width=20)
        label = tk.Label(calc, text="Host", width=10)
        label2 = tk.Label(calc, text="Port", width=10)
        text = tk.StringVar()
        label3 = tk.Label(calc, textvariable=text)
        text.set("ServerStatus : False")
        button.bind('<Button-1>', thread)
        label.pack()
        display.pack()
        label2.pack()
        display2.pack()
        label3.pack()
        button.pack()
        calc.mainloop()
    def client_run(self,Host: str="127.0.0.1",Port: int=8080):
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
            if a == "exit":
                break
             # 메시지를 전송합니다.
            client_socket.sendall(a.encode())

            # 메시지를 수신합니다.
            data = client_socket.recv(1024)
            print(data.decode())

                # 소켓을 닫습니다.
        client_socket.close()
    def display_client_run(self):
        global run
        run = False
        calc = tk.Tk()
        calc.geometry("300x300")
        calc.title("Socket_ConSole")
        def thread(event):
            global run
            if run:
                return 0
            else:
                run = True
                text.set("ConnectStatus : True")
            def fun(event):
                self.client_run(self=self, Host=str(tk.Entry.get(display)), Port=int(tk.Entry.get(display2)))
            start_new_thread(fun, (event,))
        display = tk.Entry(calc, width=20)
        display2 = tk.Entry(calc, width=20)
        button = tk.Button(calc, text="Connect", width=20)
        label = tk.Label(calc, text="Host", width=10)
        label2 = tk.Label(calc, text="Port", width=10)
        text = tk.StringVar()
        label3 = tk.Label(calc, textvariable=text)
        text.set("ConnectStatus : False")
        button.bind('<Button-1>', thread)
        label.pack()
        display.pack()
        label2.pack()
        display2.pack()
        label3.pack()
        button.pack()
        calc.mainloop()
class hello(TaeMe):
    None
if __name__ == '__main__':
    ThisMain = TaeMe
    @ThisMain
    def index(admin,content,color):
        return "Hello, This funtion is main function. maker_email=taeho070607@naver.com, word!"
    print(ThisMain.name)
    ThisMain.run(self=ThisMain,Port=8000,ConSoleTime=0)
