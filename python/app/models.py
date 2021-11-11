from datetime import datetime
from sqlalchemy import create_engine 
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base
from flask_bcrypt import (
    generate_password_hash,
    check_password_hash
)
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
)
from sqlalchemy import (
    Column,
    String,
    Integer, 
    Boolean,
    ForeignKey,
    DateTime,
    ARRAY
)

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property() 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200),nullable=False)
    username = Column(String(200),nullable=False)
    email = Column(String(200),nullable=False,unique=True)
    password = Column(String(300),nullable=False)
    phone = Column(String(30),nullable=True)
    website = Column(String(100),nullable=True)
    bio = Column(String(500),nullable=True)
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow)
    posts = relationship('Post', primaryjoin='User.id == foreign(Post.user_id)')

    def set_password(self,password:str)->None:
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self,password:str)->bool:
        return check_password_hash(self.password, password)

    def __repr__(self)->str:
        return f"id: {self.id}, Username: {self.name}"

class Post(Base):
    __tablename__ = 'posts' 
    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(200),nullable=False,unique=True)
    category = Column(String(100),nullable=False) 
    content = Column(String,nullable=False)
    likes = Column(Integer,nullable=True,default=0)
    tags = Column(ARRAY(String),nullable=True,default=[])
    user_id = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow)
    comments = relationship('Comment', primaryjoin='Post.id == foreign(Comment.post_id)')

    def __repr__(self)->str:
        return f"Post: {self.title}"

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True,autoincrement=True)
    comment = Column(String,nullable=False) 
    user_id = Column(Integer,ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"Comment: {self.comment}"