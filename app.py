import sys
import logging.config

from flask import Flask

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': { 'format': '%(asctime)s - %(name)s - %(levelname)s - '
                      '%(message)s - [in %(pathname)s:%(lineno)d]'},
        'short': { 'format': '%(message)s' }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app-api.log',
            'maxBytes': 5000000,
            'backupCount': 10
        },
        'debug': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        },
       'console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG'
       },
    },
    'loggers': {
        'appapi': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True},
        'werkzeug': { 'propagate': True },
    },
    # 'root': { 'level': 'DEBUG', 'handlers': ['console'] }
}


app = Flask(__name__)
app.config['LOGGER_HANDLER_POLICY'] = 'always'      # 'always' (default), 'never',  'production', 'debug'
app.config['LOGGER_NAME'] = 'appapi'               # define which logger to use for Flask
app.logger                                          #  initialise logger

if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    app.debug = True

logging.config.dictConfig(LOGGING)

print(app.logger.name)

app.logger.debug('debug message')
app.logger.info('info message')
app.logger.warn('warn message')
app.logger.error('error message')
app.logger.critical('critical message')