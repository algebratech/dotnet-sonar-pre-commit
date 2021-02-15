import distutils.spawn
from typing import Optional

from model.abstract.binary_check import BinaryChecker


class WindowsBinaryChecker(BinaryChecker):

    def is_binary_installed(self, name: str) -> bool:
        print(f'Checking binary {name} on Windows')
        return distutils.spawn.find_executable(name) is not None

    def get_binary_path(self, name: str) -> Optional[str]:
        if self.is_binary_installed(name):
            path = distutils.spawn.find_executable(name)
            print(f'Found binary in {path}')
            return path
        else:
            return None
