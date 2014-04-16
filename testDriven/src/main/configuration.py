__author__ = 'kvogelgesang'

import os

class SetEnv(object):

    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resources_dir = path + "/../src/resources/"
        self.resources_dir = resources_dir