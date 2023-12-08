from Controller import Controller
from Storage import Storage


class Factory():
    def create(app):
        storage = Storage()
        controller = Controller()
        storage_version = controller.get_version(storage)
        storage_help = controller.get_help(storage)

        return app(help=storage_help, version=storage_version)