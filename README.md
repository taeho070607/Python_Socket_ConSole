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
#ConSoleSetting
  ```
  ConSoleTime = 0
  ConSoleValue = =
  ConSolePost = /
  ConSoleError = None
  ConSoleColor =
  ```
