class AssetService:
    def __init__(self, asset_repository):
        self.asset_repository = asset_repository

    def add_asset(self, asset):
        self.asset_repository.save(asset)

    def get_asset(self, id):
        return self.asset_repository.find_by_id(id)

    def get_all_assets(self):
        return self.asset_repository.find_all()

    def delete_asset(self, id):
        self.asset_repository.delete(id)
