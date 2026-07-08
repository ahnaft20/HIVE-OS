class ExpertRouter:

    def __init__(self):

        self.specialists = {}

    def build_team(self, prompt):

        text = prompt.lower()

        self.specialists = {

            "backend": False,
            "frontend": False,
            "database": False,
            "security": False,
            "devops": False,
            "mobile": False,
            "ai": False,
            "testing": False,
            "documentation": True,

        }

        if any(x in text for x in [
            "website",
            "web",
            "api",
            "backend",
            "server",
            "django",
            "fastapi",
            "flask",
            "node",
        ]):

            self.specialists["backend"] = True

        if any(x in text for x in [
            "react",
            "frontend",
            "ui",
            "ux",
            "dashboard",
            "landing",
            "nextjs",
        ]):

            self.specialists["frontend"] = True

        if any(x in text for x in [
            "database",
            "mysql",
            "postgres",
            "mongodb",
            "sql",
        ]):

            self.specialists["database"] = True

        if any(x in text for x in [
            "security",
            "authentication",
            "login",
            "jwt",
            "oauth",
        ]):

            self.specialists["security"] = True

        if any(x in text for x in [
            "docker",
            "deployment",
            "aws",
            "azure",
            "vercel",
            "railway",
        ]):

            self.specialists["devops"] = True

        if any(x in text for x in [
            "android",
            "ios",
            "flutter",
            "react native",
        ]):

            self.specialists["mobile"] = True

        if any(x in text for x in [
            "ai",
            "llm",
            "machine learning",
            "deep learning",
            "rag",
            "agent",
        ]):

            self.specialists["ai"] = True

        self.specialists["testing"] = True

        return self.specialists