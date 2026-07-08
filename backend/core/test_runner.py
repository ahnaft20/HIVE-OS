import subprocess


class TestRunner:

    def __init__(self):

        self.results = []

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

            report = {

                "command": command,

                "success": result.returncode == 0,

                "stdout": result.stdout,

                "stderr": result.stderr,

            }

            self.results.append(report)

            return report

        except Exception as e:

            report = {

                "command": command,

                "success": False,

                "stdout": "",

                "stderr": str(e),

            }

            self.results.append(report)

            return report

    def history(self):

        return self.results