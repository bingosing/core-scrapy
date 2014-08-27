#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义数据库模型实体
Desc : 
"""

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text

from settings import DATABASE

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))


def create_news_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


# 定义新闻实体
class News(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "news"
    # 主键
    id = Column(String, primary_key=True)
    # 新闻分类
    category = Column('category', String, nullable=True)
    # 新闻链接地址
    link = Column('link', String, nullable=True)
    # 新闻来源
    location = Column('location', String, nullable=True)
    # 新闻标题
    title = Column('title', String, nullable=True)
    # 正文
    content = Column('content', Text, nullable=True)

