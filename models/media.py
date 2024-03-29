from marshmallow import fields

from init import db, ma

class Media(db.Model):
    __tablename__ = 'media'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    release_date = db.Column(db.String(20))
    duration = db.Column(db.String(10))
    
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    
    group = db.relationship('Group', back_populates='media')
    comments = db.relationship('Comment', back_populates='media', cascade='all, delete')
    
class MediaSchema(ma.Schema):
    group_id = fields.Nested('GroupSchema', only = ['group_name'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['media']))
    class Meta:
        fields = ('id', 'title', 'release_date', 'duration', 'group_id', 'comments') 
        ordered = True
        
media_schema = MediaSchema()
medias_schema = MediaSchema(many=True)
            
            
    