from init import db, ma
from marshmallow import fields
from datetime import datetime

class Comment(db.Model):
    __tablename__ = "comments"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey("media.id"), nullable=False)
    
    user = db.relationship('User', back_populates='comments')
    media = db.relationship('Media', back_populates='comments')
    
# Comment schema
class CommentSchema(ma.Schema):
    
    user = fields.Nested('UserSchema', only=['name', 'email'])
    
    media = fields.Nested('MediaSchema', exclude=['comments'])
    
    class Meta:
        fields = ('id', 'title', 'body', 'timestamp', 'user', 'media')
        
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

