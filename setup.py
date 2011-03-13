from setuptools import setup, find_packages, Command
import os, subprocess, sys

class RunTests(Command):
    description = "Run the test suite from the tests dir."
    user_options = []
    extra_env = {}

    def run(self):
        for env_name, env_value in self.extra_env.items():
            os.environ[env_name] = str(env_value)

        setup_dir = os.path.abspath(os.path.dirname(__file__))

        try:
            from nose.core import TestProgram
            import nosedjango
            import pstat_plugin
        except ImportError:
            print 'nose, nosedjango and pstat_plugin are required to run this test suite'
            sys.exit(1)
        os.chdir(setup_dir)

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


setup(
    name='NoseDjangoPstat',
    version='0.0.1',
    author='Jason Ward',
    author_email = 'jason.ward@policystat.com',
    description = 'A simple nose plugin for our test setup',
    install_requires='nose>=0.11',
    url = "https://github.com/jlward/nosedjango-pstat",
    license = 'GNU LGPL',
    packages = find_packages(),
    zip_safe = False,
    cmdclass = {'nosetests': RunTests},
    include_package_data = True,
    entry_points = {
        'nose.plugins': [
            'pstat_plugin = pstat_plugin:PstatPlugin',
            ]
        }
    )


