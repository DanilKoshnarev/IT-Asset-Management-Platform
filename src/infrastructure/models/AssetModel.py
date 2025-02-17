from src.domain.repositories.AssetRepository import AssetRepository

class AssetModel(AssetRepository):
    def __init__(self):
        self.assets = []

    def save(self, asset):
        self.assets.append(asset)

    def find_by_id(self, id):
        return next((asset for asset in self.assets if asset.id == id), None)

    def find_all(self):
        return self.assets

    def delete(self, id):
        self.assets = [asset for asset in self.assets if asset.id != id]
