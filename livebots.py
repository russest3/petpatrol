import urllib2
import serial
import threading

class message:
    def __init__(self, defaultUrl, robotId):
        self.url = defaultUrl + robotId + '.html'
        print(self.url)
        self.string = ''

    def request(self):
        req = urllib2.Request(self.url)
        response =  urllib2.urlopen(req)
        html = response.read()
        html=html.strip()
        html=html.rstrip()
        html=html.lstrip()
        self.string = str(html)
        return self.string

class robot:
    def __init__(self, portName):
        self.port = serial.Serial(portName, 9600)

    def send(self, message):
        if self.port.isOpen():
            self.port.write(message.encode("ascii"))

class livebot:     
    def __init__(self, robotId, portName):
        self.msg = message('http://livebots.cc/Robot/Message/', robotId)
        self.bot = robot(portName)
        self.lastMessage = ''
        self.loop()
        
    def loop(self):
        threading.Timer(0.5, self.loop).start()
        message = self.msg.request()
        if message != self.lastMessage:
            print(message)
            self.bot.send(message)
            self.lastMessage = message
