'''
Created on May 6, 2017

@author: andy
'''

import http.server as httpserver
import socketserver

def main():
    PORT = 8000
    Handler = httpserver.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    
    print ("serving at port: ", PORT)
    httpd.serve_forever()

if __name__ == '__main__':
    main()