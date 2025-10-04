class CommunityMarketplace:
    def __init__(self):
        self.plugins = []
    
    def submit_plugin(self, plugin_data):
        plugin = {
            "id": f"plugin_{len(self.plugins) + 1}",
            "name": plugin_data["name"],
            "developer": plugin_data["developer"]
        }
        self.plugins.append(plugin)
        return plugin

marketplace = CommunityMarketplace()
