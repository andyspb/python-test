'''
Created on May 6, 2017

@author: andy
'''

import SimpleHTTPServer
import SocketServer

def main():
    PORT = 8000
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    
    print "serving at port", PORT
    httpd.serve_forever()

if __name__ == '__main__':
    main()