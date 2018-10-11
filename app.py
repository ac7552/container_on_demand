import os.path
import tornado.web
import tornado.ioloop
import tornado_xstatic
from containers.containers_handler import ContainersHandler
from images.images_handler import ImagesHandler
import terminado
import docker
import logging


class WebSocketHandler(terminado.TermSocket):
    def initialize(self,term_manager):
        self.term_manager= terminado.SingleTermManager(shell_command=['sudo', 'docker' ,'exec' ,'-it', self.request.uri.split('/')[-1], 'sh'])
        self.term_name = ""
        self.size = (None, None)
        self.terminal = None

        self._logger = logging.getLogger(__name__)

class TerminalPageHandler(tornado.web.RequestHandler):
    def get(self,id):
        details=self.get_argument("details", None, True)
        return self.render("terminal.html", static=self.static_url,
                           xstatic=self.application.settings['xstatic_url'],
                           ws_url_path="/websocket")

if __name__ == '__main__':
    global app
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    handlers = [
                (r"/demo/(.*)", TerminalPageHandler),
                (r"/websocket/(.*)", WebSocketHandler, {'term_manager': None}),
                (r"/v1/containers/", ContainersHandler, {"client" : client}),
                (r"/v1/images/", ImagesHandler,  {"client" : client}),
                (r'/node_modules/(.*)', tornado.web.StaticFileHandler, {'path': './static/node_modules'}),
                (r"/xstatic/(.*)", tornado_xstatic.XStaticFileHandler,
                     {'allowed_modules': ['termjs']})
               ]
    app = tornado.web.Application(handlers,
                       xstatic_url = tornado_xstatic.url_maker('/xstatic/'))
    # Serve at http://0.0.0.0:3009/
    app.listen(3009)
    tornado.ioloop.IOLoop.instance().start()
