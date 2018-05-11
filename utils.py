OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


class ConfigException(Exception):
    """Handles the Exceptions concerning the Configuration file such as :
        - absence of the file
        - absence of one of the necessary fields
    """

    def __init__(self, error_message=None):
        if not error_message:
            error_message = 'The config file is missing some necessary fields'

    def __repr__(self):
        return colored_message(error_message, FAIL)


class CameraException(Exception):
    """Handles the Exceptions concerning the PiCamera"""

    def __init__(self, error_message=None):
        if not error_message:
            error_message = 'The camera cannot be loaded'

    def __repr__(self):
        return colored_message(error_message, FAIL)


def colored_message(s, color):
    return '{}{}{}'.format(color, s, ENDC)
