import os

class Logger:
    file_name = 'logs'

    @classmethod
    def log(cls, content: str = 'EMPTY_LOG'):
        with open(os.getcwd() + '/logs' + '/' + cls.file_name, 'a') as log_file:
            log_file.write(content + os.linesep)
