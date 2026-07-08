from pathlib import Path


class DockerManager:

    def create(self, project_directory):

        dockerfile = Path(project_directory) / "Dockerfile"

        dockerfile.write_text(

"""FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r backend/requirements.txt

EXPOSE 8000

CMD ["python","backend/main.py"]
""",

            encoding="utf-8",

        )

        compose = Path(project_directory) / "docker-compose.yml"

        compose.write_text(

"""version: '3.9'

services:

  hive:

    build: .

    ports:

      - "8000:8000"
""",

            encoding="utf-8",

        )

        return [

            str(dockerfile),

            str(compose),

        ]