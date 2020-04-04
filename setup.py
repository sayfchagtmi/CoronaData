from setuptools import setup, find_packages


setup(
    name='CoronaData',
    version='1.0',
    description='Testing installation of Package',
    author='Sayf Chagtmi',
    author_email='sayfchagtmi@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'bs4'
    ],
    entry_points='''
        [console_scripts]
        CoronaData=corona.main:run
    '''

)
