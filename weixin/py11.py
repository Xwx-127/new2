import logging


class GetLog:
    def get_log(self,level,msg):
        my_logger = logging.getLogger('ss')
        my_logger.setLevel('DEBUG')
        fh = logging.StreamHandler()
        f_str = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s")
        fh.setLevel('DEBUG')
        fh.setFormatter(f_str)
        my_logger.addHandler(fh)

        if level == 'debug':
            my_logger.debug(msg)
        elif level == 'info':
            my_logger.info(msg)
        elif level == 'warning':
            my_logger.warning(msg)
        elif level == 'error':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.get_log('debug',msg)

    def info(self,msg):
        self.get_log('info',msg)

    def warnning(self,msg):
        self.get_log('warnning',msg)

    def error(self,msg):
        self.get_log('error',msg)

    def critical(self,msg):
        self.get_log('critical',msg)

if __name__ == '__main__':
    my_log = GetLog()
    my_log.debug('88978hhhh')