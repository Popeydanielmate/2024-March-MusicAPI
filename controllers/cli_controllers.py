from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.group import Group

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
    
    db.session.commit()
    
    print("Tables seeded")