from http.server import HTTPServer, BaseHTTPRequestHandler
import time

from ctypes import *
mydll = cdll.LoadLibrary("./dll/SampleDLL.dll")

# import ctypes as c
# mydll = c.CDLL('./dll/SampleDLL.dll')
# AddNumber = mydll['AddNumber']
# AddNumber.argtypes = (c.c_int, c.c_int)
# AddNumber.restype = c.c_int
a = 1
b = 2

HOST = '192.168.0.15'
PORT = 9999


class KLWS(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(
            bytes("<html><body><h1>KinderLabs WebServer</h1></body></html>", 'utf-8'))
        print(mydll.AddNumber(a, b))
        # print(AddNumber(a, b))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', 'utf-8'))


server = HTTPServer((HOST, PORT), KLWS)
print('KinderLabs WebServer Running.....')

server.serve_forever()
server.server_close()
print('KinderLabs WebServer Stopped....!')
