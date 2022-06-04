
import json

from decimal import Decimal

from .base import CheckParam


class StrParam(CheckParam):

    def __init__(self, *args, **kwargs):
        super().__init__(param_type=str, *args, **kwargs)


class IntParam(CheckParam):

    def __init__(self, *args, **kwargs):
        super().__init__(param_type=int, *args, **kwargs)


class DecimalParam(CheckParam):

    def __init__(self, *args, **kwargs):
        super().__init__(param_type=Decimal, *args, **kwargs)


class ListParam(CheckParam):
    """
    List param with sub_type optional, sub_type make sure all the elements in the list has this type.
    For example, we need a list of string, parse function will validate it.
    Notice: sub_type must be a callable type that returns the sanitized data, like str,int,Decimal, etc, etc...
    """

    def __init__(self, sub_type=None, *args, **kwargs):
        super().__init__(param_type=list, *args, **kwargs)
        self.sub_type = sub_type

    def parse(self, raw_val: str):
        """
        Parse the list string using json.loads
        """
        raw_loads = json.loads(raw_val)
        data = []
        assert isinstance(raw_loads, list), f"{raw_val} is not list"
        if self.sub_type:
            for elem in raw_loads:
                data.append(self.sub_type(elem))

        return data
