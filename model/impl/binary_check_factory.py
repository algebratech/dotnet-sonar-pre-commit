from model.abstract.binary_check import BinaryChecker
from model.impl.unix_binary_check import UnixBinaryChecker
from model.impl.windows_binary_check import WindowsBinaryChecker
from model.os import OperatingSystemEnum


class BinaryCheckFactory:
    @staticmethod
    def get(os_enum: OperatingSystemEnum) -> BinaryChecker:
        if os_enum == OperatingSystemEnum.UNIX:
            return UnixBinaryChecker()
        else:
            return WindowsBinaryChecker()
