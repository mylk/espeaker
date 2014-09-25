#!/usr/bin/python3
from tinywebserver.server import Server
from tinywebserver.request import Request
from config import Config
from subprocess import Popen, DEVNULL, STDOUT

config = Config
server = Server
request = Request

# intercept the request
def on_request(request):
    if Request.has_data(request) and "espeak" in request["Data"]:
        # execute command and suppress output to terminal
        # for a greek voice add "-v mb-gr2" to the espeak command
        Process = Popen('espeak -a 200 "%s"' % (str(request["Data"]["espeak"])), shell=True, stdout=DEVNULL, stderr=STDOUT)

srv = server(config)
srv.start(on_request)
