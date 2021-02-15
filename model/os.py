from enum import Enum
import platform


class OperatingSystemEnum(Enum):
    UNIX = 1
    WINDOWS = 2


class OperatingSystem:
    def __init__(self):
        plt = platform.system()
        if plt == 'Windows':
            self._os = OperatingSystemEnum.WINDOWS
        else:
            self._os = OperatingSystemEnum.UNIX

    @property
    def family(self) -> OperatingSystemEnum:
        return self._os
