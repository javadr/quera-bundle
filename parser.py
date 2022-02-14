#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configargparse as argparse
import sys
import tempfile
import uuid

def parse_args(args=None):
    """
    Parse the arguments/options passed to the program on the command line.
    """

    parse_kwargs = {
        "description": 'Set the default languages for an assignment of the quera platform.'
    }
    parser = argparse.ArgParser(**parse_kwargs)

    # Basic options
    group_basic = parser.add_argument_group('Basic options')

    group_basic.add_argument(
        'assignment_num',
        action='store',
        help='number of assignment to be edited (the nnnn in https://quera.org/course/assignments/nnnnn/problems)')

    group_basic.add_argument(
        '-u',
        '--username',
        dest='username',
        action='store',
        help='username that you use to login to quera')

    group_basic.add_argument(
        '-p',
        '--password',
        dest='password',
        action='store',
        help='password required to login in quera')

    group_basic.add_argument(
        '--config',
        dest='config',
        action='store_true',
        default=False,
        help='Ask the user for the desired languages')

    group_basic.add_argument(
        '--key',
        dest='key',
        action='store',
        default=str(uuid.getnode()),
        help='key used to make the saved password unreadable')

    # Final parsing of the options
    args = parser.parse_args(args)

    if not args.assignment_num:
        parser.print_usage()
        sys.exit(1)

    args.parser = parser
    return args
