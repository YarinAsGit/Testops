
import os

from pathlib import Path

from checks import register_check
from checks.base import BaseCheck
from checks.params import StrParam, ListParam


@register_check(sub_command='env-var')
class EnvVarCheck(BaseCheck):
    """
    Check if an environment variable exists on the running machine
    """
    var_name = StrParam(required=True)
    var_value = StrParam()

    def preform_check(self) -> None:
        assert os.getenv(self.var_name) is not None, f"Env Var{self.var_name} is not exists"
        if self.var_value:
            assert os.getenv(self.var_name) == self.var_value, f"Env Var {self.var_name}" \
                                                               f" is not equal to {self.var_value}"


@register_check(sub_command='dirs-exists')
class DirsExistCheck(BaseCheck):
    """
    Check if dirs exists on the running machine
    """
    dirs = ListParam(required=True, sub_type=Path)

    def preform_check(self) -> None:
        for directory_path in self.dirs:
            assert directory_path.is_dir(), f"{directory_path.name} is not a directory"


@register_check(sub_command='files-exists')
class FilesExistCheck(BaseCheck):
    """
    Check if files exists on the running machine
    """
    files = ListParam(required=True, sub_type=Path)

    def preform_check(self) -> None:
        for file_path in self.files:
            assert file_path.is_file(), f"{file_path.name} is not a file"
