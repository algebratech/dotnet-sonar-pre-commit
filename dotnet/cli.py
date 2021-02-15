import subprocess
from argparse import Namespace

from model.abstract.binary_check import BinaryChecker


class DotnetCli:
    def __init__(self,
                 abstract_checker: BinaryChecker,
                 args: Namespace):
        self._abstract_checker = abstract_checker
        self._args = args

    def run_scan(self) -> int:
        print('Starting sonar scanner..')

        if not self._abstract_checker.is_binary_installed('dotnet'):
            print('Please install dotnet CLI first!')
            return -1

        status = self.run_begin()
        if status != 0:
            return status

        status = self.run_build()
        if status != 0:
            return status

        return self.run_end()

    def run_begin(self) -> int:
        process = subprocess.Popen(
            f'dotnet sonarscanner begin /k:{self._args.sonar_project_key} /d:sonar.login={self._args.sonar_token}'
            f' /o:{self._args.sonar_organization} /n:{self._args.sonar_project_name}',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        for line in process.stdout.readlines():
            print(line)
        return process.wait()

    def run_build(self) -> int:
        process = subprocess.Popen(
            f'dotnet build {self._args.sln_path}',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        for line in process.stdout.readlines():
            print(line)
        return process.wait()

    def run_end(self) -> int:
        process = subprocess.Popen(
            f'dotnet sonarscanner end /d:sonar.login={self._args.sonar_project_key}'
        )
        return process.wait()
