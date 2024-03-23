from flask import Blueprint, request, jsonify
from init import db, ma
from models.group import Group, GroupSchema
from models.user import User

groups_bp = Blueprint('groups', __name__, url_prefix='/group')

@groups_bp.route('/', methods=['GET'])
def get_group_details():
    group = Group.query.first()  # Fetch the single group
    if group:
        return jsonify({
            "group_name": group.group_name,
            "genre": group.genre,
            "biography": group.biography,
            "discography": group.discography,
            "id": group.id
        })
    else:
        return jsonify({"error": "Group not found"}), 404

# Route to update the group (only accessible by admin users)
@groups_bp.route('/', methods=['PUT'])
def update_group():
    # Extract group data from the request body
    group_data = request.json
    # Check if the user making the request is an admin
    user_id = request.headers.get('user-id')  # Assuming the user ID is sent in the request headers
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return jsonify({"error": "Only admin users can edit the group information"}), 403
    
    group = Group.query.first()
    if group:
        group.group_name = group_data.get('group_name', group.group_name)
        group.genre = group_data.get('genre', group.genre)
        group.biography = group_data.get('biography', group.biography)
        group.discography = group_data.get('discography', group.discography)
        db.session.commit()
        group_schema = GroupSchema()
        return group_schema.jsonify(group)
    else:
        return jsonify({"error": "Group not found"}), 404



