import logging
import logging.config
import os.path


DEFAULT_LOGGING_CONFIG = {
    'level': logging.INFO,
    'disable_existing_loggers': False,
}


def setup_logging(
        config_path="logging.yaml",
        config_path_env="LOG_CFG_PATH"
):
    """Setup the python logger

    Args:
        config_path (str): Path to a default config file
        config_path_env (str): Env variable to specify alternate logging config
    """
    config_override = os.getenv(config_path_env, None)
    config_path = config_path if not config_override else config_override

    if os.path.exists(config_path):
        import yaml

        with open(config_path, "rt") as yaml_file:
            config = yaml.load(yaml_file.read())

        logging.config.dictConfig(config)

    else:
        logging.basicConfig(**DEFAULT_LOGGING_CONFIG)


class LogProducer(object):
    """Simple class to add in class-oriented logging"""
    def __init__(self, subname=None):
        logger_name = ".".join([
            self.__class__.__module__,
            self.__class__.__name__
        ])

        if subname:
            logger_name += " ({})".format(subname)
        self._log = logging.getLogger(logger_name)