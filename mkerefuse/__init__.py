__version__ = '0.0.0-testing'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
