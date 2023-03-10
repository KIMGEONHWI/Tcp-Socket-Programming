import socket

HOST = '127.0.0.1' #접속할 서버 주소=> 서버에서 설정한 서버ip
PORT = 8888 #서버에서 지정해 놓은 포트번호

#소켓 객체를 생성
#주소 체계로 IPv4, 소켓 타입으로 TCP 사용
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버 accept()에 연결요청.
#지정한 host와 port를 사용하여 서버에 접속
client_socket.connect((HOST, PORT))

#무한 루프 돌기
while True:
    message = input('message:') #서버로 보낼 메세지 입력
    client_socket.sendall(message.encode())	#서버로 메세지를 전송

    data = client_socket.recv(1024)  #서버로부터 데이터를 수신
    print('Received', data.decode()) #읽은 데이터 복호화
    if message=='/end':              #/end입력시 서버, 클라이언트 모두 종료
        break

client_socket.close() #소켓 닫기