
import re

from commands import COMMANDS


class FileParser:

    def __init__(self, content: str):
        self.content = content

    def _parse_file(self):
        """
         Parse the TestopsFile and executes the commands one by one.
        """
        # Clean empty lines and comments
        res = [line for line in self.content.split('\n') if bool(line) and not line.startswith('#')]
        for line in res:
            split_command_line = line.split(' ', 1)
            command_name, sub_command = split_command_line
            if command_name not in COMMANDS:
                raise Exception(f"{command_name} isn't a Command")

            # Executing the command
            COMMANDS[command_name].execute(sub_command)
