from flask import Blueprint, request, jsonify
from init import db, ma
from models.media import Media, MediaSchema

media_bp = Blueprint('media', __name__, url_prefix='/media')

@media_bp.route('/', methods=['GET'])
def get_media_details():
    media = Media.query.all() 
    if media:
        media_schema = MediaSchema(many=True)
        return media_schema.jsonify(media)
    else:
        return jsonify({"error": "Media not found"}), 404

@media_bp.route('/', methods=['PUT'])
def update_media():
    media_data = request.json
    
    media = Media.query.first()
    if media:
        media.title = media_data.get('title', media.title)
        media.release_date = media_data.get('release_date', media.release_date)
        media.duration = media_data.get('duration', media.duration)
        media.group_id = media_data.get('group_id', media.group_id)

        db.session.commit()
        media_schema = MediaSchema()
        return media_schema.jsonify(media)
    else:
        return jsonify({"error": "Media not found"}), 404
