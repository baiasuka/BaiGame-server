from models import db
from sqlalchemy import func


class UserModel(db.Model):
    __tablename__ = 't_user_gallery'
    id = db.Column(db.BIGINT, primary_key=True)
    account = db.Column(db.VARCHAR(32), nullable=False, comment='账号')
    password = db.Column(db.SMALLINT, nullable=False, comment='密码')
    update_time = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    create_time = db.Column(db.DATETIME, default=func.now(), nullable=False)
