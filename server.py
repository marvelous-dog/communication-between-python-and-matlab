#使用TCP协议
#服务器端

import socket
import time
import threading
from PIL import Image
import numpy as np
import wave
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#创建了一个基于IPv4的socket
ip=input('Pleas input the server IP addres and port.\n')
port=int(input(''))
s.bind(('127.0.0.1',8001))
#监听端口
s.listen(5)
#监听端口，5表示等待连接的最大数量
print('waiting for connection...')



def word():
    sock.send(('This is the outcome.').encode('utf-8'))
    print(len(('This is the outcome.').encode('utf-8')))
def picture():
    im=Image.open('lena.jpg')
    mes=np.asarray(im)
    print(len(mes))
    sock.send(mes)
def music():
    file=open('你曾是少年.wav','rb')
    mes=file.read()
    sock.send(mes)
    print(len(mes))
def tcplink(sock,addr):
    print('Accept new connection from %s:%s' %addr)
    sock.send(b'Welcome!')
    data=sock.recv(1024)
    if data.decode('utf-8')=='word':
        word()
    if data.decode('utf-8')=='picture':
        picture()
    if data.decode('utf-8')=='music':
        music()
    sock.close()
    print('Connection from %s:%s cloosed.'%addr)

while True:
    sock,addr=s.accept()
    #接受一个新的连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    #创建一个线程来处理
    t.start()
    
