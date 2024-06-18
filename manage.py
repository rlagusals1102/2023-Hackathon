from os import environ
from sys import argv

def main():
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'military_project.settings')

    from django.core.management import execute_from_command_line
    execute_from_command_line(argv)

if __name__ == '__main__':
    main()
