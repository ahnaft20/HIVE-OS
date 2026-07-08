from pathlib import Path


class DeploymentManager:

    def __init__(self):

        self.deployments = []

    def prepare(
        self,
        project_directory,
        target,
    ):

        project = Path(project_directory)

        if target.lower() == "vercel":

            (project / "vercel.json").write_text(
"""{
    "version":2
}
""",
                encoding="utf-8",
            )

        elif target.lower() == "railway":

            (project / "railway.json").write_text(
"""{
    "$schema":"https://railway.app/railway.schema.json"
}
""",
                encoding="utf-8",
            )

        elif target.lower() == "render":

            (project / "render.yaml").write_text(
"""services:
  - type: web
""",
                encoding="utf-8",
            )

        elif target.lower() == "netlify":

            (project / "netlify.toml").write_text(
"""[build]
publish="dist"
""",
                encoding="utf-8",
            )

        self.deployments.append(
            {
                "target": target,
                "status": "Prepared",
            }
        )

    def history(self):

        return self.deployments