from src.domain.entities.Asset import Asset
from src.domain.repositories.AssetRepository import AssetRepository
from src.domain.services.AssetService import AssetService
from src.domain.usecases.ManageAsset import ManageAsset
from src.infrastructure.models.AssetModel import AssetModel
from src.infrastructure.controllers.AssetController import AssetController

def main():
    asset_repository = AssetModel()
    asset_service = AssetService(asset_repository)
    manage_asset = ManageAsset(asset_service)
    asset_controller = AssetController(manage_asset)

  
    asset_controller.add_asset("1", "Laptop", "Hardware", "Active")
    asset_controller.add_asset("2", "Office 365", "Software", "Active")

    
    for asset in asset_controller.get_all_assets():
        print(f"ID: {asset.id}, Name: {asset.name}, Type: {asset.type}, Status: {asset.status}")

    
    asset_controller.delete_asset("1")

    
    for asset in asset_controller.get_all_assets():
        print(f"ID: {asset.id}, Name: {asset.name}, Type: {asset.type}, Status: {asset.status}")

if __name__ == "__main__":
    main()
