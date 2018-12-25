import socket
import io
import time
import picamera
import struct

def record():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.AF_INET, socket.SOCK_STREAM
    client.connect(('192.168.0.10', 8004))
    connection = client_socket.makefie('wb')

    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.start_preview()
            camera.framerate = 20
            time.sleep(2)
            start = time.time()
            stream = io.BytesIO()
        
            for frame in camera.capture_continuous(stream, 'jpeg'):
                connection.write(struct.pack('<L', stream.tell()))
                connection.flush()
                stream.seek(0)
                connection.write(stream.read())
                if time.time()-start > 300:
                    break
                streak.seek(0)
                stream.truncate()
            connection.write(struct.pack('<L', 0))
    finally:
        connection.close()
        client.close()
        
#record()
'''
            connection.write(struct.pack('<L', 0))
            camera.resolution = (640, 480)
            camera.framerate = 24
            camera.start_preview()
            time.sleep(2)
            camera.start_recording(connection, format = 'h246')
            camera.wait_recording(60)
            camera.stop_recording()
            connection.write(struct.pack('<L', 0))

        
'''