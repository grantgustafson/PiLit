import logging, logging.config
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGING_DIR = os.path.normpath(os.path.join(CURR_DIR, 'logs'))
assert os.path.isdir(LOGGING_DIR)


DB_URI = 'sqlite:///db.db'

engine =create_engine(DB_URI)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
HOSTS_PATH = 'hosts.txt'
OPC_PORT = 7890

LOG_CONFIG = {'version': 1,
              'formatters': {
                  'request': {
                      'format': '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
                  },
                  'listener': {
                      'format': '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
                  }
              },
              'handlers': {
                  'stdout': {
                      'class': 'logging.StreamHandler',
                      'formatter': 'request',
                      'stream': 'ext://sys.stdout'
                  },
                  'stream': {
                      'class': 'logging.StreamHandler',
                      'formatter': 'request',
                  },
                  'log': {
                      'class': 'logging.handlers.TimedRotatingFileHandler',
                      'formatter': 'listener',
                      'filename': os.path.join(LOGGING_DIR, 'log'),
                      'when': 'midnight',
                  },
              },
              'loggers': {
                  'logger': {
                      'level': 'DEBUG',
                      'handlers': ['log', 'stdout'],
                  },
              }
            }
logging.config.dictConfig(LOG_CONFIG)
LOGGER = logging.getLogger('logger')

def rel_path(path):
    return os.path.join(CURR_DIR, path)
