# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, JSON, text, Index
from sqlalchemy.dialects.mysql import BIGINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
