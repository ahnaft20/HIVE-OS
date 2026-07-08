from pathlib import Path


class BugFixer:

    def attempt_fix(
        self,
        filepath,
    ):

        file = Path(filepath)

        if not file.exists():

            return "Skipped"

        text = file.read_text(
            encoding="utf-8",
        )

        fixed = text.replace(
            "\t",
            "    ",
        )

        file.write_text(
            fixed,
            encoding="utf-8",
        )

        return "Formatting checked"