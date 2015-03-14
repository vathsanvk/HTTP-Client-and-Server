import string,time,cgi

from os import curdir,sep

import os.path

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
   # if(os.path.exists("D:/localhost" + filename)):
       try:
            file=open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file.read())
            file.close()
            return
       except IOError:
            self.send_error(404,'File Not Found')


    def do_PUT(self):
         length = int(self.headers['Content-Length'])
         file = self.rfile.read(length)
         path = "D:/"
         file_name=self.path.decode('string_escape')
         completePath = os.path.join(path, file_name)
         new_file = open(completePath,"w")
         new_file.write(file) 
         self.send_response(200)

        

def main():
    try:
        server=HTTPServer(('127.0.0.1',80), RequestHandler)
        print 'Server Started' 
        print 'Type Ctrl + C to shutdown the server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Control C recieved - Shutting down the server'
        server.socket.close()

if __name__ == '__main__':
    main() 
    
