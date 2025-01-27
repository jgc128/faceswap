#!/usr/bin/env python3
""" The master faceswap.py script """
import gettext
import sys

from lib.cli import args as cli_args
from lib.config import generate_configs


# LOCALES
_LANG = gettext.translation("faceswap", localedir="locales", fallback=True)
_ = _LANG.gettext


if sys.version_info[0] < 3:
    raise Exception("This program requires at least python3.7")
if sys.version_info[0] == 3 and sys.version_info[1] < 7:
    raise Exception("This program requires at least python3.7")


_PARSER = cli_args.FullHelpArgumentParser()


def _bad_args(*args):  # pylint:disable=unused-argument
    """ Print help to console when bad arguments are provided. """
    print(cli_args)
    _PARSER.print_help()
    sys.exit(0)


def _main():
    """ The main entry point into Faceswap.

    - Generates the config files, if they don't pre-exist.
    - Compiles the :class:`~lib.cli.args.FullHelpArgumentParser` objects for each section of
      Faceswap.
    - Sets the default values and launches the relevant script.
    - Outputs help if invalid parameters are provided.
    """
    generate_configs()

    subparser = _PARSER.add_subparsers()
    cli_args.ExtractArgs(subparser, "extract", _("Extract the faces from pictures or a video"))
    cli_args.TrainArgs(subparser, "train", _("Train a model for the two faces A and B"))
    cli_args.ConvertArgs(subparser,
                         "convert",
                         _("Convert source pictures or video to a new one with the face swapped"))
    cli_args.GuiArgs(subparser, "gui", _("Launch the Faceswap Graphical User Interface"))
    cli_args.InsertArgs(subparser,
                        "insert",
                        _("Convert source pictures or video to a new one using pre-defined faces"))

    _PARSER.set_defaults(func=_bad_args)
    arguments = _PARSER.parse_args()
    arguments.func(arguments)


if __name__ == "__main__":
    _main()
