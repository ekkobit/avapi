import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


def license():
    with open('LICENSE') as f:
        return f.read()


setuptools.setup(name='avapi',
                 version='0.1.4',
                 description='Get data from Alpha Vantage into python.',
                 long_description=readme(),
                 long_description_content_type="text/markdown",
                 classifiers=[
                        'Development Status :: 3 - Alpha',
                        'License :: OSI Approved :: MIT License',
                        'Programming Language :: Python :: 3',
                        'Topic :: Office/Business :: Financial :: Investment',
                        ],
                 url='http://github.com/olemola/vantage',
                 author='Ole Olaussen',
                 author_email='ole@ekkobit.com',
                 license='MIT',
                 license_file=license(),
                 packages=setuptools.find_packages(),
                 test_suite='nose.collector',
                 tests_require=['nose'],
                 install_requires=[
                        'pandas', 'requests',
                        ],
                 include_package_data=True,
                 )
