from flask import Blueprint, jsonify, request, abort
from main import db
from models.assets import Asset
from models.users import User
from schemas.asset_schema import asset_schema, assets_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

assets = Blueprint('assets', __name__, url_prefix="/assets")

# The GET route endpoint - get all the assets
@assets.route("/", methods=["GET"])
def get_assets():
    # get all the assets from the database table
    assets_list = Asset.query.all()
    # Convert the assets from the database into a JSON format and store them in result
    result = assets_schema.dump(assets_list)
    # return the data in JSON format
    return jsonify(result)

# The GET routes endpoint - get details on one asset
@assets.route("/<int:id>/", methods=["GET"])
def get_asset(id):
    asset = Asset.query.get(id)
    #return an error if the card doesn't exist
    if not asset:
        return abort(400, description= "asset does not exist")
    # Convert the cards from the database into a JSON format and store them in result
    result = asset_schema.dump(asset)
    # return the data in JSON format
    return jsonify(result)

# The GET routes endpoint - get manufacturer for asset
@assets.route('/manufacturer/<int:asset_id>', methods=["GET"])
def manufacturer_assets (asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'error': 'Asset not found'})
    manufacturer_dict_list = []
    for assettype in asset.asset_type_id:
        for manufacturer in assettype.manufacturer:
            manufacturer_dict = {'manufacturer_id': manufacturer.manufacturer_id, 'manufacturer_name': manufacturer.manufacturer_name,'manufacturer_contact_number': manufacturer.manufacturer_contact_number,'manufacturer_email': manufacturer.manufacturer_email}
            manufacturer_dict_list.append(manufacturer_dict)
    asset_dict = {'manufacturers': manufacturer_dict_list, 'asset_id': asset.asset_id, 'asset_name': asset.asset_name, 'serial_number':asset.serial_number }
    return jsonify(asset_dict)

# The GET routes endpoint - get asset_type for asset
@assets.route('/asset_type/<int:asset_id>', methods=["GET"])
def asset_type_assets (asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'error': 'Asset not found'})
    asset_type_dict_list = []
    for assettype in asset.asset_type_id:
        asset_type_dict = {'asset_type_id': assettype.asset_type_id, 'description': assettype.description}
        asset_type_dict_list.append(asset_type_dict)
    asset_dict = {'asset_type': asset_type_dict_list, 'asset_id': asset.asset_id, 'asset_name': asset.asset_name, 'serial_number':asset.serial_number }
    return jsonify(asset_dict)


# The POST route endpoint - add a asset
@assets.route("/", methods=["POST"])
def create_asset():
    #Create a new asset
    asset_fields = asset_schema.load(request.json)

    new_asset = Asset()
    new_asset.asset_name = asset_fields ["asset_name"]
    new_asset.serial_number = asset_fields["serial_number"]
    new_asset.date_purchased = asset_fields["date_purchased"]
    new_asset.employee_id = asset_fields["employee_id"]
    # not taken from the request, generated by the server
    new_asset.date = date.today()
    # add to the database and commit
    db.session.add(new_asset)
    db.session.commit()
    #return the asset in the response
    return jsonify(asset_schema.dump(new_asset))

# The PUT route endpoint - update asset details
@assets.route("/<int:id>/", methods=["PUT"])
# @jwt_required()
def update_asset(id):
    # #Create a new card
    asset_fields = asset_schema.load(request.json)
    # get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # find the asset
    asset = Asset.query.filter_by(id=id).first()
    #return an error if the asset doesn't exist
    if not asset:
        return abort(400, description= "Asset does not exist")
    # update the asset details with the given values
    asset.serial_number = asset_fields["serial_number"]
    asset.date_purchased = asset_fields["date_purchased"]
    asset.employee_id = asset_fields["employee_id"]
    # not taken from the request, generated by the server
    asset.date = date.today()
    # add to the database and commit
    db.session.commit()
    #return the asset in the response
    return jsonify(asset_schema.dump(asset))



# The DELETE route endpoint - delete a asset
@assets.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_asset(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # find the card
    asset = Asset.query.filter_by(asset_id=id).first()
    #return an error if the asset doesn't exist
    if not asset:
        return abort(400, description= "Card doesn't exist")
    #Delete the asset from the database and commit
    db.session.delete(asset)
    db.session.commit()
    #return the card in the response
    return jsonify(asset_schema.dump(asset))
