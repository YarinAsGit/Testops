
import re

from checks.base import BaseCheck

# Register all types of checks in a dict. The key is the command name as in TestopsFile.
# The value will be Check class itself which must be BaseCheck type
REGISTERED_CHECKS = {}


def validate_sub_command_name(sub_command_name: str) -> bool:
    """
    Validate command name contains only letters, numbers or dashes, otherwise raise exception.
    """
    return bool(re.match("^[A-Za-z0-9-]*$", sub_command_name))


def register_check(*, sub_command: str):
    """
    Decorator to register all the existing checks.
    Command name use for the TestopsFile. A valid command name should contain letters, numbers and dashes ONLY.
    """
    validate_sub_command_name(sub_command)

    def deco(klass: BaseCheck):
        if sub_command in REGISTERED_CHECKS:
            raise Exception(f"{sub_command} already registered")
        assert isinstance(klass, BaseCheck), f"{klass} isn't a standard BaseCheck"
        REGISTERED_CHECKS[sub_command] = {'cls': klass, 'params': klass.get_params_list()}
        return klass

    return deco
