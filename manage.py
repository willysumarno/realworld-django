#!/usr/bin/env python

import os
import sys


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realworld.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as e:
        raise ImportError("Couldn't import Django.") from e
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
