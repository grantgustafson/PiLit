import logging, logging.config
import os
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGING_DIR = os.path.normpath(os.path.join(CURR_DIR, 'logs'))
assert os.path.isdir(LOGGING_DIR)

MODULE_SCHEMA_PATH = 'schema/module_schema.json'
MODULE_FILE_PATH = 'modules.json'

HOSTS_PATH = 'hosts.txt'

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
