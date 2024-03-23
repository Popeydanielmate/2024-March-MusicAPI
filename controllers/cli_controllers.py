from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.group import Group
from models.media import Media

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")
    
@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")
    
@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            email="popeyadmin@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]
    
    db.session.add_all(users)
    
    groups = [
        Group(
            group_name="The Popeys",
            genre="Indie/Rock/Alternative",
            biography="The Popeys formed in Sydney in 2005 and begun playing the local pub circuit until catching the attention of a famous record label",
            discography="Self titled- 2006, Album 2- 2010, Album 3- 2014, Album 4- 2019"
        )
    ]

    db.session.add_all(groups)
    
    the_popeys_group = Group.query.filter_by(group_name='The Popeys').first()

    if the_popeys_group:
        media = [
            Media(
                title="Song no.1",
                release_date="02-03-2006",
                duration="4.30",
                group_id=the_popeys_group.id
            ),
            Media(
                title="Song no.2",
                release_date="05-07-2010",
                duration="3.52",
                group_id=the_popeys_group.id
            ),
            Media(
                title="Song no.3",
                release_date="30-08-2014",
                duration="4.43",
                group_id=the_popeys_group.id
            ),
            Media(
                title="Song no.4",
                release_date="05-10-2019",
                duration="3.27",
                group_id=the_popeys_group.id
            )
        ]
    
        db.session.add_all(media)
    
        db.session.commit()
    
    else:
        print("The Popeys group not found")
    
    print("Tables seeded")
