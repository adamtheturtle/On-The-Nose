from setuptools import setup, find_packages

version = '1.0'

setup(name='onTheNose',
      version=version,
      description="",
      long_description="",
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Adam Dangoor',
      author_email='adamdangoor@gmail.com',
      url='',
      license='',
      package_dir={'': 'packages'},
      packages=find_packages('packages', exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'web.py',
      ],
      )
