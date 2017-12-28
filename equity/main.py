import cherrypy
from routes import BhavCopy

if __name__ == '__main__':
    cherrypy.quickstart(BhavCopy())
