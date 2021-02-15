from abc import ABCMeta, abstractmethod
from typing import Optional


class BinaryChecker:
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_binary_installed(self, name: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_binary_path(self, name: str) -> Optional[str]:
        raise NotImplementedError
