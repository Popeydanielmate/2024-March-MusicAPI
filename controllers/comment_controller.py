from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.media import Media
from models.comment import Comment, comment_schema

comments_bp = Blueprint('comments', __name__, url_prefix="/<int:media_id>/comments")

@comments_bp.route("/", methods=["POST"])
@jwt_required()
def create_comment(media_id):
    body_data = request.get_json()
    media = Media.query.get(media_id)
    if media:
        comment = Comment(
            message=body_data.get('message'),
            user_id=get_jwt_identity(),
            media=media
        )
        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 201
    else:
        return {"error": f"Media with id {media_id} doesn't exist"}, 404
    
@comments_bp.route("/<int:comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(media_id, comment_id):
    comment = Comment.query.get(comment_id)
    if comment and comment.media.id == media_id:
        db.session.delete(comment)
        db.session.commit()
        return {"message": f"Comment with id {comment_id} has been deleted"}
    else:
        return {"error": f"Comment with id {comment_id} not found in media with id {media_id}"}, 404
    
@comments_bp.route("/<int:comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_comment(media_id, comment_id):
    body_data = request.get_json()
    comment = Comment.query.filter_by(id=comment_id, media_id=media_id).first()
    if comment:
        comment.message = body_data.get('message', comment.message)
        db.session.commit()
        return comment_schema.dump(comment)
    else:
        return {"error": f"Comment with id {comment_id} not found in media with id {media_id}"}, 404
