'''
Created on May 6, 2017

@author: andy

Updated by DogeSec, 9/28/17
'''

import http.server as httpserver
import socketserver

def main(x):
    PORT = x
    Handler = httpserver.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    
    print ("serving at port: ", PORT)
    httpd.serve_forever()

if __name__ == '__main__':
    try:
      user_choice = input("Enter a port or press enter: ")
      if user_choice == '':
        main(8000)
      else:
        main(int(user_choice))
    except KeyboardInterrupt:
      quit()
