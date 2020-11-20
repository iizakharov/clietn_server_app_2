from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker

from config.dict import *
import datetime


class ServerStorage:
    class AllUsers:
        def __init__(self, username):
            self.name = username
            self.last_login = datetime.datetime.now()
            self.id = None

    class UsersOnline:
        def __init__(self, user_id, ip_address, port, login_online):
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_online = login_online
            self.id = None

    class LoginHistory:
        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
            self.port = port

    def __init__(self):
        self.database_engine = create_engine(SERVER_DATABASE, echo=False, pool_recycle=7200)

        self.metadata = MetaData()

        users_table = Table('Users', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('name', String, unique=True),
                            Column('last_login', DateTime)
                            )
        online_users_table = Table('UsersOnline', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('user', ForeignKey('Users.id'), unique=True),
                                   Column('ip_address', String),
                                   Column('port', Integer),
                                   Column('login_time', DateTime)
                                   )
        user_login_history = Table('Login_history', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('name', ForeignKey('Users.id')),
                                   Column('date_time', DateTime),
                                   Column('ip', String),
                                   Column('port', String)
                                   )

        self.metadata.create_all(self.database_engine)

        mapper(self.AllUsers, users_table)
        mapper(self.UsersOnline, online_users_table)
        mapper(self.LoginHistory, user_login_history)

        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        self.session.query(self.UsersOnline).delete()
        self.session.commit()

    def user_login(self, username, ip_address, port):
        print(username, ip_address, port)

        rez = self.session.query(self.AllUsers).filter_by(name=username)

        if rez.count():
            user = rez.first()
            user.last_login = datetime.datetime.now()
        else:
            user = self.AllUsers(username)
            self.session.add(user)
            self.session.commit()

        new_online_user = self.UsersOnline(user.id, ip_address, port, datetime.datetime.now())
        self.session.add(new_online_user)

        history = self.LoginHistory(user.id, datetime.datetime.now(), ip_address, port)
        self.session.add(history)

        self.session.commit()

    def user_logout(self, username):
        user = self.session.query(self.AllUsers).filter_by(name=username).first()
        self.session.query(self.UsersOnline).filter_by(user=user.id).delete()
        self.session.commit()

    def users_list(self):
        query = self.session.query(
            self.AllUsers.name,
            self.AllUsers.last_login,
        )
        return query.all()

    def online_users_list(self):
        query = self.session.query(
            self.AllUsers.name,
            self.UsersOnline.ip_address,
            self.UsersOnline.port,
            self.UsersOnline.login_time
        ).join(self.AllUsers)
        return query.all()

    def login_history(self, username=None):
        query = self.session.query(self.AllUsers.name,
                                   self.LoginHistory.date_time,
                                   self.LoginHistory.ip,
                                   self.LoginHistory.port
                                   ).join(self.AllUsers)
        if username:
            query = query.filter(self.AllUsers.name == username)
        return query.all()


if __name__ == '__main__':
    test_db = ServerStorage()
    test_db.user_login('Vasya', '10.0.0.1', 8888)
    test_db.user_login('Kolya', '192.168.132.109', 8080)
    print(test_db.online_users_list())
    test_db.user_logout('client_1')
    print(test_db.online_users_list())
    test_db.login_history('client_1')
    print(test_db.users_list())
