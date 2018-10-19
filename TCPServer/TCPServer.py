# coding=utf-8
# !/usr/bin/env python
 
from socket import *
from time import ctime
import threading
import time
 
HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)
 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
socks = []  # 放每个客户端的socket
 
 
def handle():
    while True:
        for s in socks:
            try:
                data = s.recv(BUFSIZ)  # 到这里程序继续向下执行
            except:
                continue
            if not data:
                print('断开连接:',s.getpeername())
                socks.remove(s)
                continue
            for ss in socks:    #收到信息后群发
                ss.send(data)
  
t = threading.Thread(target=handle)  # 子线程

if __name__ == '__main__':
    t.start()
    print('等待连接...')
    while True:
        clientSock, addr = tcpSerSock.accept()
        print('连接来自:', addr)
        clientSock.setblocking(0)
        socks.append(clientSock)
 
 
