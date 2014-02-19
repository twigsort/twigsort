#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # this sets your settings, which is in mysite.settings.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","twigsort.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
