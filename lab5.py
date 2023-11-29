"""
Module: lab5.py
"""

from typing import Union

class File():
    """
    File class represents a file with certain characteristics.
    """

    def __init__(self, name, extension, size) -> None:
        self.name = name
        self.extension = extension
        self.size = size

    def get_info(self):
        """
        Get information about the file.
        """
        return f"File: {self.name}.{self.extension}, Size: {self.size} bytes"

    def __str__(self):
        return f"Your file: {self.name}.{self.extension}, Size: {self.size} bytes"

    def __repr__(self):
        return f"File({self.name}, {self.extension}, {self.size})"
 
    def __del__(self):
        print(f"Your file: {self.name}.{self.extension} deleted.")

class Folder():
    """
    Folder class represents a folder containing files and subfolders.
    """

    def __init__(self, path) -> None:
        self._path = path
        self._objects = []

    def get_path(self):
        return self._path
    
    def get_objects(self):
        return self._objects

    def add_object(self, _object: Union[File, 'Folder']) -> None:
        """
        Add a file or subfolder to the folder.
        """
        self._objects.append(_object)

    def get_tree(self) -> str:
        """
        Generate a tree structure of files and subfolders within the folder.
        """
        for _object in self._objects:
            if isinstance(_object, File):
                yield f"{self._path}/{_object.name}.{_object.extension} # {_object.size}"
            elif isinstance(_object, Folder):
                for _subobject in _object.get_tree():
                    yield f"{self._path}/{_subobject}"

if __name__ == "__main__" :
    file1 = File("lab5", "py", 67)

    print(file1.get_info())
    print(file1.__str__())
    print(file1.__repr__())


    new_file = File("doc", "txt", 56)
    new_file2 = File("lol", "pdf", 100500)
    new_folder = Folder("home")
    new_folder.add_object(new_file)
    new_folder.add_object(file1)

    file2 = File("lab2", "txt", 100)
    folder = Folder("root")
    folder.add_object(file2)
    folder.add_object(new_folder)
    folder.add_object(new_file2)

    print(">>>>>>>>>>>>>>>>")
    for ob in folder.get_tree():
        print(ob)
