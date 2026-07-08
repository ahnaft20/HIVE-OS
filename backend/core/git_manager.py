import subprocess


class GitManager:

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

            log = {

                "command": command,

                "success": result.returncode == 0,

                "stdout": result.stdout,

                "stderr": result.stderr,

            }

            self.logs.append(log)

            return log

        except Exception as e:

            log = {

                "command": command,

                "success": False,

                "stdout": "",

                "stderr": str(e),

            }

            self.logs.append(log)

            return log

    def history(self):

        return self.logs