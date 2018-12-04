# by www.zhangyi.studio@gmail.com
# 2018-12-08

import common

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

    def SETUP(self):
        """Causes the server to allocate resources for a stream and start
            an RTSP session.
        """
        print(self.url)
        print("state=",self.state)

    def PLAY(self):
        """ Starts data transmission on a stream allocated via SETUP.
        """
        pass

    def PAUSE(self):
        """Temporarily halts a stream without freeing server resources.
        """
        pass

    def TEARDOWN(self):
        """Frees resources associated with the stream. The RTSP session
            ceases to exist on the server.
        """
        pass


if __name__ == "__main__":
    url = "www.baidu.com"
    client = rtsp_client(url)
    client.SETUP()