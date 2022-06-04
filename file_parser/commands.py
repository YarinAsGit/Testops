
import re

from checks import REGISTERED_CHECKS


COMMANDS = {}


def validate_command_line_name(command_name: str) -> bool:
    """
    Validate command name contains only capital letters and underscore, otherwise raise exception.
    """
    return bool(re.match("^[A-Z_]*$", command_name))


def command_line(name: str):
    """
    Decorator that collects all the file commands into a dict.
    The key is a string represent the command name and the value is a BaseCommand class.
    """
    validate_command_line_name(name)

    def deco(klass: BaseCommand):
        if name in COMMANDS:
            raise Exception(f"Command {name} already exists")
        assert isinstance(klass, BaseCommand), f"{klass} isn't a standard BaseCommand"
        COMMANDS[name] = klass
        return klass

    return deco


class BaseCommand:

    @staticmethod
    def execute(sub_command: str):
        """
        Validate command input is valid, otherwise raise exception
        """
        raise NotImplementedError


@command_line(name='RUN_CHECK')
class RunCheckCommand(BaseCommand):

    @staticmethod
    def execute(sub_command: str):
        pass
