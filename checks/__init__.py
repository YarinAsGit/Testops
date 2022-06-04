
import re

from checks.base import BaseCheck

# Register all types of checks in a dict. The key is the command name as in TestopsFile.
# The value will be Check class itself which must be BaseCheck type
registered_checks = {}


def validate_command_name(command_name: str) -> bool:
    """
    Validate command name contains only letters, numbers or dashes, otherwise raise exception.
    """
    return bool(re.match("^[A-Za-z0-9-]*$", command_name))


def register_check(*, command: str):
    """
    Decorator to register all the existing checks.
    Command name use for the TestopsFile. A valid command name should contain letters, numbers and dashes ONLY.
    """
    validate_command_name(command)

    def deco(klass: BaseCheck):
        if command in registered_checks:
            raise Exception(f"{command} already registered")
        assert isinstance(klass, BaseCheck)
        registered_checks[command] = {'cls': klass, 'params': klass.get_params_list()}
        return klass

    return deco
