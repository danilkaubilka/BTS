from client2server import client2server

class tracker:
    def run(tracklog):
        c2s=client2server()
        while True:
            status=c2s.getStatus()
            dx=int(status)&0x0fff
            code = int(status)&0xff00000000000 // 16 ** 11
            time = int(status)&0xffffff00000 // 16 ** 5

            if(dx>2048):
                dx=dx-4096
            tracklog.write("Received %d \n" % (dx), 'Code %d' % bin(code), 'Time %d' % time)
            if(abs(int(dx))<500):
             if(abs(int(dx))<10):
                c2s.moveStop()
             else:
                speed=50
                if(int(dx)>0):
                    c2s.moveLeft(speed)
                else:
                    c2s.moveRight(speed)
        c2s.__finit__