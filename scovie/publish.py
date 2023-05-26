"""
    Helper to publish this Project to PyPi
"""

from pathlib import Path

from poetry_publish.publish import poetry_publish
from poetry_publish.utils.subprocess_utils import verbose_check_call

import scovie


PACKAGE_ROOT = Path(scovie.__file__).parent.parent


def publish():
    """
    Publish to PyPi
    Call this via:
        $ poetry run publish
    """
    verbose_check_call('make', 'test')  # don't publish if tests fail
    verbose_check_call('make', 'lint')  # don't publish if code style wrong

    poetry_publish(package_root=PACKAGE_ROOT, version=scovie.__version__)
