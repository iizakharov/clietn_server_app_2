import sys
import log.server_log_config
import log.client_log_config
import logging

# метод определения модуля, источника запуска.
if sys.argv[0].find('client') == -1:  # если не клиент то сервер!
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')  # ну, раз не сервер, то клиент


def log(func_to_log):
    def log_wrapper(*args, **kwargs):
        logger.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args} , {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}')
        result = func_to_log(*args, **kwargs)
        return result
    return log_wrapper
