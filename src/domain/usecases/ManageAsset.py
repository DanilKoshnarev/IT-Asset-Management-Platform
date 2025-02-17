from src.domain.entities.Asset import Asset

class ManageAsset:
    def __init__(self, asset_service):
        self.asset_service = asset_service

    def create_asset(self, id, name, type, status):
        asset = Asset(id, name, type, status)
        self.asset_service.add_asset(asset)

    def view_asset(self, id):
        return self.asset_service.get_asset(id)

    def view_all_assets(self):
        return self.asset_service.get_all_assets()

    def remove_asset(self, id):
        self.asset_service.delete_asset(id)
