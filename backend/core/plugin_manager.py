class PluginManager:

    def __init__(self):

        self.plugins = {}

    def install(
        self,
        name,
        role,
        team,
    ):

        self.plugins[name] = {

            "role": role,

            "team": team,

            "enabled": True,

        }

    def uninstall(self, name):

        if name in self.plugins:

            del self.plugins[name]

    def enable(self, name):

        if name in self.plugins:

            self.plugins[name]["enabled"] = True

    def disable(self, name):

        if name in self.plugins:

            self.plugins[name]["enabled"] = False

    def enabled_plugins(self):

        return {

            name: plugin

            for name, plugin in self.plugins.items()

            if plugin["enabled"]

        }

    def export(self):

        return self.plugins