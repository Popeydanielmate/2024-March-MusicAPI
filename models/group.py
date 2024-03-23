from marshmallow import fields
from init import db, ma 


class Group(db.Model):
    __tablename__ = "groups"
    
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    biography = db.Column(db.Text)
    discography = db.Column(db.Text)
    
    media = db.relationship('media', back_populates='group')
    
class GroupSchema(ma.Schema):
    
    id = ma.auto_field()
    group_name = ma.String(required=True)
    genre = ma.String(required=True)
    biography = ma.String(required=True)
    discography = ma.String(required=True)
    
class GroupSchema(ma.Schema):
    media = fields.List(fields.Nested('MediaSchema'))
    class Meta:
        fields = ('id', 'group_name', 'genre', 'biography', 'discography', 'media')
        ordered = True        