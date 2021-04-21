import os
import sys

def execute_from_command_line(argv):
    """Execute commands"""
    os.system("/QOpenSys/pkgs/bin/python3 {}.py ".format(argv[1]))

def main():
    """Run administrative tasks."""
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()