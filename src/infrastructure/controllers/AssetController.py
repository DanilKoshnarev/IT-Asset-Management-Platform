class AssetController:
    def __init__(self, manage_asset):
        self.manage_asset = manage_asset

    def add_asset(self, id, name, type, status):
        self.manage_asset.create_asset(id, name, type, status)

    def get_asset(self, id):
        return self.manage_asset.view_asset(id)

    def get_all_assets(self):
        return self.manage_asset.view_all_assets()

    def delete_asset(self, id):
        self.manage_asset.remove_asset(id)
