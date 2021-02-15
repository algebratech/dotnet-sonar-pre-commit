import argparse
from typing import Optional, Sequence

from dotnet.cli import DotnetCli
from model.impl.binary_check_factory import BinaryCheckFactory
from model.os import OperatingSystem


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument(
        '--sln-path', dest='sln_path'
    )
    parser.add_argument(
        '--sonar-project-key', dest='sonar_project_key'
    )
    parser.add_argument(
        '--sonar-project-name', dest='sonar_project_name'
    )
    parser.add_argument(
        '--sonar-organization', dest='sonar_organization'
    )
    parser.add_argument(
        '--sonar-token', dest='sonar_token'
    )
    parser.add_argument(
        '--sonar-branch', action='store_const', dest='sonar_branch', const='main', default='main'
    )

    args = parser.parse_args(argv)

    binary_checker = BinaryCheckFactory.get(OperatingSystem().family)
    cli = DotnetCli(abstract_checker=binary_checker, args=args)

    return cli.run_scan()


if __name__ == '__main__':
    exit(main())
