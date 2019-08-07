from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

def license():
    with open('LICENSE') as f:
        return f.read()

setup(name='avapi',
      version='0.1',
      description='Convert json data files from Alpha Vantage to Pandas data frames.',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7.3',
        'Topic :: Data Processing :: Finance',
      ],
      url='http://github.com/olemola/vantage',
      author='Ole Olaussen',
      author_email='olemolaussen@gmail.com',
      license='MIT',
      license_file = license(),
      packages=setuptools.find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[
          'json', 'pandas', 'requests', 'os',
      ],
      include_package_data=True,
      )
