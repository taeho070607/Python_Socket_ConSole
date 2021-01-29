# Python_Socket_ConSole
파이썬 소켓을 더욱 쉽게 사용할수 있도록 만든 코드입니다.
  ```
  TaeMe = TaeMe.TaeMe
  @TaeMe
  def 원하는 명령어(content,color):
    ''':content 소켓으로 받은 내용을 content에 저장한다
       :color 설정한 색깔을 저장한다.'''
    return 출력하고싶은 내용
  TaeMe.run(self=TaeMe,Host=자신의 호스트 ip(str),Port=원하는 포트(int))
  #기본ip는 127.0.0.1 기본 포트는 8080
  만약 client 의 ConSoleSetting 정보를 얻고싶다면(다만 admin은 dic 자료형이다. ex)admin['ConSoleTime'])
  @TaeMe
  def 원하는 명령어(admin,content,color):
    ''':content 소켓으로 받은 내용을 content에 저장한다
       :color 설정한 색깔을 저장한다.'''
    return 출력하고싶은 내용
   한 함수가 받을수있는 최대의 인자수는 4개다.(그중에서 contnet,color,admin 을 재외한 나머지 인자는 꼭 맨앞에 써줘야한다.)
   def 원하는 명령어(받고싶은 인자 이름(꼭 맨앞),admin,content,color):
    ''':content 소켓으로 받은 내용을 content에 저장한다
       :color 설정한 색깔을 저장한다.'''
    return 출력하고싶은 내용
  None을 return하면 " "이 보내진다.
  ```  
  
이런식으로 사용하면된다.
  ```
  fun = TaeMe.search(self=TaeME,Target=찾기원하는 명령어 함수(str))
  fun()
  ```
이런식으로 다른함수(명령어)를 찾고 호출할수도 있다.
Client쪽 코드는 이렇다.
  ```
  TaeMe = TaeMe.TaeMe
  TaeMe.client_run(self=TaeMe,Host=자신의 호스트 ip(str),Port=원하는 포트(int))
  ```
명령어 종류 확인:help
알아서 셋팅(기본)된다.
#ConSoleSetting(기본)
  ```
  ConSoleTime = 0
  ConSoleValue = =
  ConSolePost = /
  ConSoleError = None
  ConSoleColor =
  ```
#ConSoleSettinf command
  ```
  ConSoleColor 콘솔컬러를 결정한다.(pink='\033[95m',black='\033[30m',Red='\033[31m',green='\033[32m',yellow='\033[33m')
  ConSoleTime 콘솔 응답 간격을 정한다.
  ConSolePost 나눌때 어떤 방식으로 나눌지 ex)next/value=10 여기서 /이 ConSolePost 이다.
  ConSoleValue '='를 다른 문자로 변경 ex)ConSoleTime=10 여기서 '10'이 ConSoleValue
  ConSoleError 예외(명령어를 찾지못할때) 어떤 멘트가 나오게할지
  help 명령어 목록
  ConSole 콘솔 세팅 정보
  ```
#TaeMe.run function varnames
  ```
  self,color: str="",ConSoleTime: float=0.125,ConSolePost: str="/",ConSoleValue: str="=",Host: str="127.0.0.1",Port: int=8080,Error: str=None,Server: list=None,Admin: bool=False
  ```
#TaeMe class varnames
  ```
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
  ```
#TaeMe.search function varnames
  ```
  self,Taeget: str=""
  ```
#ServerByStatus command
  ```
  ServerByStatus 커맨드를 실행할경우 접속중인유저 누적유저들 밴유저들 마지막으로 밴 메시지를 볼수있다.
  ServerByUsers 서버에 접속중인 유저목록
  ServerByBanUsers 서버에 밴된 유저목록
  ServerByAccumulate 누적된 유저 목록
  ServerByFullUsersMessage 서버가 꽉차고 들어온 클린트에게 띄울 메시지
  ServerByBanUsers 밴된 클린트에게 띄울 메시지
  ```
