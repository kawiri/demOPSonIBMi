import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import DbSettings

dbS = DbSettings()
SYSTEM = dbS.DATABASES['Db2fori']['HOST']
UID = dbS.DATABASES['Db2fori']['USER']
PWD = dbS.DATABASES['Db2fori']['PASSWORD']
DBNAME = dbS.DATABASES['Db2fori']['NAME'] 

conn_string = "ibmi://{}:{}@{}/{}".format(UID, PWD, SYSTEM, DBNAME)
engine = sa.create_engine(conn_string, echo=True)
Base = declarative_base()
dbS.Validate()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    PASSWORD = Column(String(128), nullable=False)
    last_login = Column(TIMESTAMP, nullable=True)
    is_superuser = Column(Integer, nullable=True)
    username = Column(String(150) , nullable=False)
    first_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=True)
    email = Column(String(254), nullable=False)
    is_staff = Column(Integer, nullable=True)
    is_active = Column(Integer, nullable=True)
    date_joined = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return "<User(username='%s', email='%s', password='%s')>" % (
            self.username, self.email, self.pwd)

class Profile(Base):
    __tablename__='profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(None, ForeignKey('users.id'))
    website = Column(String(80), nullable=True)
    biography = Column(String(200), nullable=True)
    phone_number = Column(String(10), nullable=True)
    address = Column(String(80), nullable=True)
    city = Column(String(60))
    country = Column(String(60))
    sex = Column(Integer, nullable=False, default=0)
    created = Column(TIMESTAMP, nullable=True)
    modified = Column(TIMESTAMP, nullable=True)
    photo = Column(String(100), nullable=True)

    user = relationship("User", back_populates="profiles")

    def __repr__(self):
        return "<Profile(website='%s', biography='%s', phone_number='%s',  address='%s', city='%s', country='%s')>" % (
                self.website, self.biography, self.phone_number, self.address, self.city, self.country)

User.profiles = relationship(
    "Profile", order_by=Profile.id, back_populates="users")
Base.metadata.create_all(engine)
dbS.Adjust()