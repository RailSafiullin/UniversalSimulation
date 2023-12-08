class Controller:
    def get_version(self, storage):
        return storage.get_version()
    
    def get_help(self, storage):
        return storage.get_help()