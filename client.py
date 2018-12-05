# by www.zhangyi.studio@gmail.com
# 2018-12-08

import common
import urlparse
import socket

class rtsp_state:
    """enum state
    """
    INIT = 0
    SETUP = 1
    PLAY = 2
    PAUSE = 3
    TEARDOWN = 4

class rtsp_client:
    """rtsp client class
    """
    def __init__(self,url):
        self.url = url
        self.state = rtsp_state.INIT
        self.seqNum = 1
        urls = urlparse.urlparse(self.url)
        if urls.scheme != 'rtsp' :
            return -1

        url_port = urls.netloc.split(':')
        self.ip = url_port[0]
        self.port = int(url_port[1])
        print url_port

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((self.ip,self.port))


    def OPTIONS(self):
        """ get support function
        """
        Header = self.getHeader('OPTIONS')
        self.socket.sendall(Header)
        data =  self.socket.recv(1024)
        print data
        return 'ok'
        # self.socket.close()  

    def DESCRIBE(self):
        """ get sdp info
        """
        Header = self.getHeader('DESCRIBE')
        self.socket.sendall(Header)
        data =  self.socket.recv(1024)
        print data
        return 'ok'


    def SETUP(self):
        """Causes the server to allocate resources for a stream and start
            an RTSP session.
        """
        Header = self.getHeader('SETUP')
        self.socket.sendall(Header)
        data =  self.socket.recv(1024)
        print data
        return 'ok'

    def PLAY(self):
        """ Starts data transmission on a stream allocated via SETUP.
        """
        Header = self.getHeader('PLAY')
        self.socket.sendall(Header)
        data =  self.socket.recv(1024)
        print data
        return 'ok'

    def PAUSE(self):
        """Temporarily halts a stream without freeing server resources.
        """
        Header = self.getHeader('PAUSE')

    def TEARDOWN(self):
        """Frees resources associated with the stream. The RTSP session
            ceases to exist on the server.
        """
        Header = self.getHeader('TEARDOWN')
    

    def getHeader(self,param,m='audio',type='unicast',port='1112-1113'):
        """compose request header
        """
        Header = ''
        if len(param) == 0 :
            return -1
        self.seqNum += 1
        if param == 'SETUP' :
            Header += param + ' ' + self.url + '/track1 ' + 'RTSP/1.0 \r\n'
        if param == 'PLAY' :
            Header += param + ' ' + self.url + '/ ' + 'RTSP/1.0 \r\n'
        else:
            Header += param + ' ' + self.url + ' ' + 'RTSP/1.0 \r\n'
        Header += 'CSeq:' + ' ' + str(self.seqNum) + ' ' + '\r\n'
        if param == 'DESCRIBE' :
            Header += 'Accept: application/sdp \r\n'
        if param == 'SETUP' :
            Header += 'Transport: RTP/AVP;' + type +';client_port=1112-1113'
        Header += 'User-Agent: Python RTSP Client \r\n'
        Header += '\r\n'
        print Header

        return Header



    def start(self):
        ret = self.OPTIONS()
        if ret != 'ok' :
            return -1
        
        ret = self.DESCRIBE()
        if ret != 'ok' :
            return -2
        
        ret = self.SETUP()
        if ret != 'ok' :
            return -3
        ret = self.PLAY()
        if ret != 'ok' :
            return -4



if __name__ == "__main__":
    url = "rtsp://192.168.21.80:8554/test.mp3"
    client = rtsp_client(url)
    client.start()
