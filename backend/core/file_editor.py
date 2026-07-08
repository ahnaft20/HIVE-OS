from pathlib import Path


class FileEditor:

    def __init__(self):
        pass

    def create_file(
        self,
        filepath,
        content="",
    ):

        file = Path(filepath)

        file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file.write_text(
            content,
            encoding="utf-8",
        )

    def read_file(
        self,
        filepath,
    ):

        file = Path(filepath)

        if not file.exists():
            return ""

        return file.read_text(
            encoding="utf-8",
        )

    def overwrite(
        self,
        filepath,
        content,
    ):

        Path(filepath).write_text(
            content,
            encoding="utf-8",
        )

    def append(
        self,
        filepath,
        content,
    ):

        with open(
            filepath,
            "a",
            encoding="utf-8",
        ) as f:

            f.write(content)

    def replace(
        self,
        filepath,
        old,
        new,
    ):

        text = self.read_file(filepath)

        text = text.replace(
            old,
            new,
        )

        self.overwrite(
            filepath,
            text,
        )

    def rename(
        self,
        old_path,
        new_path,
    ):

        Path(old_path).rename(new_path)

    def delete(
        self,
        filepath,
    ):

        file = Path(filepath)

        if file.exists():
            file.unlink()