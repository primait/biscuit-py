from setuptools import setup


def get_version():
    return open('biscuit/_version.py').readline().strip().strip('"')


setup(
    name='biscuit-py-prima',
    version=get_version(),
    description='biscuit-py decrypts secrets managed by Biscuit.',
    long_description=open('README.rst').read(),
    author='Doug Coker',
    author_email='dcoker@gmail.com',
    url='https://github.com/primait/biscuit-py',
    include_package_data=False,
    license='https://www.apache.org/licenses/LICENSE-2.0',
    packages=[
        'biscuit'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7'
    ],
    zip_safe=False,
    install_requires=[
        'boto3>=1.11.12',
        'libnacl>=1.7.1',
        'cryptography>=2.8',
        'pyyaml>=5.1,<5.3'
    ],
    test_suite='tests.biscuit_test',
    entry_points={
        'console_scripts': [
            'biscuitpy=biscuit.__main__:main'
        ]
    },
)
