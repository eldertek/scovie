import os
import shutil
import subprocess
import sys
from pathlib import Path

import tomli
from bx_py_utils.path import assert_is_dir, assert_is_file
from django.test import SimpleTestCase
from django_tools.unittest_utils.project_setup import check_editor_config
from django_yunohost_integration.test_utils import assert_project_version
from packaging.version import Version

import scovie


PACKAGE_ROOT = Path(scovie.__file__).parent.parent
assert_is_dir(PACKAGE_ROOT)
assert_is_file(PACKAGE_ROOT / 'pyproject.toml')


def assert_file_contains_string(file_path, string):
    with file_path.open('r') as f:
        for line in f:
            if string in line:
                return
    raise AssertionError(f'File {file_path} does not contain {string!r} !')


def poetry_check_output(*args):
    poerty_bin = shutil.which('poetry')
    assert_is_file(poerty_bin)
    output = subprocess.check_output(
        (poerty_bin,) + args,
        text=True,
        env=os.environ,
        stderr=subprocess.STDOUT,
        cwd=str(PACKAGE_ROOT),
    )
    return output


class ProjectSetupTestCase(SimpleTestCase):
    def test_code_style(self):
        subprocess.check_call([sys.executable, '-m', 'darker', '--color'])

    def test_version(self):
        current_version = scovie.__version__

        if not Version(current_version).is_prerelease:
            assert_project_version(
                current_version=current_version,
                github_project_url='https://github.com/jedie/scovie',
            )

        pyproject_toml_path = Path(PACKAGE_ROOT, 'pyproject.toml')
        pyproject_toml = tomli.loads(pyproject_toml_path.read_text(encoding='UTF-8'))
        pyproject_version = pyproject_toml['tool']['poetry']['version']
        self.assertEqual(pyproject_version, current_version)

    def test_poetry_check(self):
        output = poetry_check_output('check')
        assert output == 'All set!\n'

    def test_check_editor_config(test):
        check_editor_config(package_root=PACKAGE_ROOT)

    def test_mypy(self):
        subprocess.check_call(['mypy', PACKAGE_ROOT])
