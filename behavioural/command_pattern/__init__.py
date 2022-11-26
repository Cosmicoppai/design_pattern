"""
File System Utility example
"""

from abc import ABC, abstractmethod


class FileSystemReceiver(ABC):

    @abstractmethod
    def openfile(self, filename: str):
        ...

    @abstractmethod
    def writefile(self, filename: str, content: str | bytes):
        ...

    @abstractmethod
    def closefile(self):
        ...


class WindowsFileSystemReceiver(FileSystemReceiver):
    def openfile(self, filename: str):
        print("opening file")

    def writefile(self, filename: str, content: str | bytes):
        print("writing file")

    def closefile(self):
        print("closing file")


class Command(ABC):

    @abstractmethod
    def execute(self):
        ...


class OpenFileCommand(Command):

    def __init__(self, file_name: str, fs: FileSystemReceiver):
        self.file_system = fs
        self.file_name = file_name

    def execute(self):
        self.file_system.openfile(file_name)


class CloseFileCommand(Command):
    def __init__(self, fs: FileSystemReceiver):
        self.fs = fs

    def execute(self):
        self.fs.closefile()


class WriteFileCommand(Command):
    def __init__(self, file_name: str, content: str | bytes, fs: FileSystemReceiver):
        self.fs = fs
        self.file_name: str = file_name
        self.content: str | bytes = content

    def execute(self):
        self.fs.writefile(file_name, content)


class Invoker:
    def __init__(self, command: Command):
        self.command = command

    def execute(self):
        self.command.execute()

