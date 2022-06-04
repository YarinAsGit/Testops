
import socket

from checks import register_check
from checks.base import BaseCheck
from checks.params import ListParam


@register_check(command='local-open-ports')
class LocalOpenPortsCheck(BaseCheck):
    """
    Check if there's running ports on the local machine
    Gets list of ports as param
    """
    ports = ListParam(required=True, sub_type=int)

    def preform_check(self) -> None:
        for port in self.ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('120.0.0.1', port))
