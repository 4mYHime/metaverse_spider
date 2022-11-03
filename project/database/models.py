# coding: utf-8
from sqlalchemy import Column, DateTime, JSON, text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Announcement18Art(Base):
    __tablename__ = 'announcement_18art'
    __table_args__ = (
        {'comment': '公告-18art'}
    )

    id = Column(BIGINT, primary_key=True)
    type = Column(TINYINT, nullable=False, comment="公告类型")
    type_name = Column(VARCHAR(512), nullable=False, comment="公告类型名称")
    title = Column(VARCHAR(512), nullable=False, comment="公告标题")
    cover = Column(VARCHAR(512), nullable=False, comment="公告配图地址")
    content = Column(JSON, nullable=False, comment="公告内容JSON")
    content_type = Column(VARCHAR(12), nullable=False, comment="公告内容类型，object/html")
    is_delete = Column(TINYINT, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Announcement42verse(Base):
    __tablename__ = 'announcement_42verse'
    __table_args__ = (
        {'comment': '公告-42verse'}
    )

    id = Column(BIGINT, primary_key=True)
    type_name = Column(VARCHAR(512), nullable=False, comment="公告类型名称")
    title = Column(VARCHAR(512), nullable=False, comment="公告标题")
    content = Column(JSON, nullable=False, comment="公告内容JSON")
    content_type = Column(VARCHAR(12), nullable=False, comment="公告内容类型，object/html")
    is_delete = Column(TINYINT, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AnnouncementIbox(Base):
    __tablename__ = 'announcement_ibox'
    __table_args__ = (
        {'comment': '公告-ibox'}
    )

    id = Column(BIGINT, primary_key=True)
    type = Column(TINYINT, nullable=False, comment="公告类型")
    type_name = Column(VARCHAR(512), nullable=False, comment="公告类型名称")
    title = Column(VARCHAR(512), nullable=False, comment="公告标题")
    content = Column(JSON, nullable=False, comment="公告内容JSON")
    content_type = Column(VARCHAR(12), nullable=False, comment="公告内容类型，object/html")
    is_delete = Column(TINYINT, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AnnouncementLingjingsj(Base):
    __tablename__ = 'announcement_lingjingsj'
    __table_args__ = (
        {'comment': '公告-lingjingsj'}
    )

    id = Column(BIGINT, primary_key=True)
    type_name = Column(VARCHAR(512), nullable=False, comment="公告类型名称")
    title = Column(VARCHAR(512), nullable=False, comment="公告标题")
    content = Column(JSON, nullable=False, comment="公告内容JSON")
    content_type = Column(VARCHAR(12), nullable=False, comment="公告内容类型，object/html")
    is_delete = Column(TINYINT, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AnnouncementShuzimart(Base):
    __tablename__ = 'announcement_shuzimart'
    __table_args__ = (
        {'comment': '公告-shuzimart'}
    )

    id = Column(BIGINT, primary_key=True)
    type = Column(TINYINT, nullable=False, comment="公告类型")
    type_name = Column(VARCHAR(512), nullable=False, comment="公告类型名称")
    title = Column(VARCHAR(512), nullable=False, comment="公告标题")
    content = Column(JSON, nullable=False, comment="公告内容JSON")
    content_type = Column(VARCHAR(12), nullable=False, comment="公告内容类型，object/html")
    is_delete = Column(TINYINT, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AnnouncementTheone(Base):
    __tablename__ = 'announcement_theone'
    __table_args__ = (
        {'comment': '公告-theone'}
    )

    id = Column(VARCHAR(512), primary_key=True)
    type_name = Column(VARCHAR(512), nullable=False, comment="公告类型名称")
    title = Column(VARCHAR(512), nullable=False, comment="公告标题")
    cover = Column(VARCHAR(512), nullable=False, comment="公告配图地址")
    content = Column(JSON, nullable=False, comment="公告内容JSON")
    content_type = Column(VARCHAR(12), nullable=False, comment="公告内容类型，object/html")
    is_delete = Column(TINYINT, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
