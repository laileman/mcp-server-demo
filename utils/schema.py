from sqlalchemy import create_engine
from utils.model import UserModel, GroupModel, Base
from sqlalchemy.orm import sessionmaker


# mysql client
class MysqlClient:
    def __init__(self, host, port, user, password, database):
        self.engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        )

    @property
    def session(self):
        return sessionmaker(bind=self.engine, autoflush=False, autocommit=False)()

    # create user
    def create_user(self, name, age):
        session = self.session
        user_id = session.query(UserModel).count() + 1
        data = UserModel(
            id=user_id,
            name=name,
            age=age,
        )
        session.add(data)
        session.commit()
        session.close()
        return user_id

    # search all users
    def search_all_users(self):
        session = self.session
        users = session.query(UserModel).all()
        session.close()
        return [{"id": user.id, "name": user.name, "age": user.age} for user in users]

    # search a user
    def search_user(self, name):
        session = self.session
        user = session.query(UserModel).filter(UserModel.name == name).first()
        session.close()
        return {"id": user.id, "name": user.name, "age": user.age}

    # create group
    def create_group(self, name):
        session = self.session
        group_id = session.query(GroupModel).count() + 1
        data = GroupModel(name=name, id=group_id)
        session.add(data)
        session.commit()
        session.close()
        return group_id

    # search all groups
    def search_all_groups(self):
        session = self.session

        data = session.query(GroupModel).all()
        session.close()
        return [{"id": group.id, "name": group.name} for group in data]

    # search a group
    def search_group(self, name):
        session = self.session

        group = session.query(GroupModel).filter(GroupModel.name == name).all()
        session.close()
        return {"id": group.id, "name": group.name}

    # search all table
    def search_all_table(self):
        tables = Base.metadata.tables.keys()
        return [table for table in tables]


mysqlClient = MysqlClient("localhost", 3306, "root", "password", "mydb")
Base.metadata.create_all(mysqlClient.engine)
