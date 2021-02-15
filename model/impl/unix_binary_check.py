from shutil import which
from typing import Optional

from model.abstract.binary_check import BinaryChecker


class UnixBinaryChecker(BinaryChecker):

    def is_binary_installed(self, name: str) -> bool:
        """Check whether `name` is on PATH and marked as executable."""

        print(f'Checking binary {name} on *nix system')
        return which(name) is not None

    def get_binary_path(self, name: str) -> Optional[str]:
        if self.is_binary_installed(name):
            path = which(name)
            print(f'Found binary in {path}')
            return path
        else:
            return None
