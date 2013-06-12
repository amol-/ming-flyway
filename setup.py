from setuptools import setup, find_packages

__version__ = 'undefined'

exec open('flyway/version.py')

setup(name='Flyway',
      version=__version__,
      description="Migration utilities for the Ming MongoDB mapping layer",
      long_description="""Migration utilities for the Ming MongoDB mapping layer""",
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='mongo, pymongo',
      author='Rick Copeland',
      author_email='rick@geek.net',
      url='http://merciless.sourceforge.net',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        "ming",
        "PasteScript",
      ],
      tests_require = [
        "nose",
      ],
      entry_points="""
      [flyway.test_migrations]
      a = flyway.tests.migrations_a
      b = flyway.tests.migrations_b

      [paste.paster_command]
      flyway = flyway.command:MigrateCommand
      """,
      test_suite='nose.collector'
      )
