import os, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateTable
from config import DB_URI
engine = create_engine(DB_URI)
from models.module import Module

schemas = [Module]
schemas = map(lambda s: CreateTable(s.__table__).compile(engine), schemas)
schemas = map(lambda s: '{};\n\n'.format(str(s).strip()), schemas)

for schema in schemas:
    print schema
