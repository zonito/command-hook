"""Hook to run command before commit."""
# pylint: disable=C0325

import argparse
import subprocess
import sys


def main(argv=None):
    """Init method."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--command', type=str, required=True, help='command to execute')
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)
    subp = subprocess.Popen(args.command.split(), stdout=subprocess.PIPE)
    subp.wait()
    if subp.returncode == 1:
        print('Catchall for general errors')
    elif subp.returncode == 2:
        print('Misuse of shell builtins (according to Bash documentation)')
    elif subp.returncode == 126:
        print('Command invoked cannot execute')
    elif subp.returncode == 127:
        print('Command not found.')
    elif subp.returncode == 128:
        print('Invalid argument to exit')
    elif subp.returncode == 130:
        print('Script terminated by Control-C')
    elif subp.returncode >= 255:
        print('Exit status out of range')
    return subp.returncode > 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
