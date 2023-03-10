import socket

#서버의 아이피 포트 정보
HOST = '127.0.0.1'  #접속할 서버 주소
PORT = 8888         #서버 포트번호로 클라이언트 접속을 대기하는 번호

#서버 소켓 오픈(객체 생성), 클라이언트를 받을 준비
#주소 체계로 IPv4, 소켓 타입으로 TCP사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #포트 사용중이라 연결할 수 없다는 에러 방지

#bind:설정한 소켓에 HOST(ip)와 PORT를 붙여주는 것
#즉, 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용
server_socket.bind((HOST, PORT))
                                   


server_socket.listen() #이제 클라이언트가 접속 준비 완료(접속 허용)

print('서버 시작') 

#accept 상태로 대기, client의 접속을 기다리다 요청시 처리.
#client와 1:1통신할 소켓과 연결된 상대방의 주소 반환
client_socket, addr = server_socket.accept()

print('Connected by', addr) #접속한 클라이언트 주소

#무한루프 돌기
while True:
    data = client_socket.recv(1024)   #클라이언트가 보낸 메시지를 수신하기 위해 대기
    message = data.decode()               #읽은 데이터를 복호화
    print('Received from', addr, message) #수신받은 문자열을 출력
    client_socket.sendall(data)	      #클라이언트로부터 받은 메시지 다시 전송=>메아리 효과
    if message=='/end':                   #/end입력시 서버, 클라이언트 모두 종료
        break
        
server_socket.close() #소켓 닫기