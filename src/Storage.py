import os

class Storage:
    def __init__(self):
        self.version = None
        self.help = None
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.read_version()
        self.read_help()

    def read_version(self):
        with open(os.path.join(self.root_dir, '..', 'docs', 'version.txt'), 'r') as f:
            self.version = f.readline()

    def get_version(self):
        return self.version

    def read_help(self):
        with open(os.path.join(self.root_dir, '..', 'docs', 'help.txt'), 'r') as f:
            self.help = f.read()

    def get_help(self):
        return self.help