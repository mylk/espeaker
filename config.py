import sys
import os

server_path = os.path.abspath(os.path.dirname(sys.argv[0]))

class Config:
    hostname = "localhost"
    port = 8000
    project_dir = server_path
    root_dir = server_path + "/www"
