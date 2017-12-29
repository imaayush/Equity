import cherrypy
import os
from routes import BhavCopy

port = int(os.environ.get("PORT", 5000))
cherrypy.config.update({'server.socket_port': port,
                        'server.socket_host': '0.0.0.0'})
if __name__ == '__main__':
    cherrypy.quickstart(BhavCopy())
