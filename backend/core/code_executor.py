import subprocess
from pathlib import Path


class CodeExecutor:

    def __init__(self):
        self.logs = []

    def run(
        self,
        command,
        cwd=None,
    ):

        try:

            result = subprocess.run(
                command,
                cwd=cwd,
                shell=True,
                capture_output=True,
                text=True,
            )

            output = {

                "command": command,

                "returncode": result.returncode,

                "stdout": result.stdout,

                "stderr": result.stderr,

            }

            self.logs.append(output)

            return output

        except Exception as e:

            output = {

                "command": command,

                "returncode": -1,

                "stdout": "",

                "stderr": str(e),

            }

            self.logs.append(output)

            return output

    def history(self):

        return self.logs