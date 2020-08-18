from abc import ABCMeta, abstractmethod
from dependency_injector import providers, containers


class Writer(metaclass=ABCMeta):
    """
    Interface of writers
    """
    @abstractmethod
    def write(self):
        pass


class FileWriter(Writer):
    """
    Specific writer for files
    """
    def __init__(self):
        self.files_written = 0

    def write(self):
        self.files_written += 1


class DatabaseWriter(Writer):
    """
    Specific writer for DB
    """
    def __init__(self):
        self.tables_written = 0

    def write(self):
        self.tables_written += 1


class Editor:
    """
    It saves data, it doesn't need to know where
    """
    def __init__(self, writer):
        """
        Injecting writer
        :param writer: Writer
        """
        self.writer = writer

    def save(self):
        self.writer.write()


class Writers(containers.DeclarativeContainer):
    """
    Container for services of writers
    """
    file_writer = providers.Factory(FileWriter)
    database_writer = providers.Factory(DatabaseWriter)


class Editors(containers.DeclarativeContainer):
    """
    Container for services of editors
    """
    file_editor = providers.Factory(Editor, writer=Writers.file_writer)
    database_editor = providers.Factory(Editor, writer=Writers.database_writer)
