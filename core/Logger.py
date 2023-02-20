import os

class Logger:
    @classmethod
    def log(cls, content: str = 'EMPTY_LOG', file = 'logs'):
        with open(os.getcwd() + '/logs' + '/' + file, 'a') as log_file:
            log_file.write(content + os.linesep)
