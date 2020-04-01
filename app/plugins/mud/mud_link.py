from socket import *
import time

class TCPClient:
  def __init__(self, host='mud.pkuxkx.com', port=8080, coding='gbk'):
    self.HOST = host
    self.PORT = port
    self.BUFSIZ = 4096
    self.ADDRESS = (self.HOST, self.PORT)
    self.coding = coding
    self.tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    self.tcpClientSocket.connect(self.ADDRESS)

  def send(self, msg):
    self.tcpClientSocket.send(msg.encode(self.coding, 'ignore') + b'\n')
    return self.receive()

  def receive(self):
    result = ""
    while True:
      time.sleep(2)
      data = self.tcpClientSocket.recv(self.BUFSIZ)
      result += data.decode(self.coding, 'ignore')
      if len(data) < self.BUFSIZ:
        break

    return result