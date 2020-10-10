from setuptools import setup, find_packages

setup(
    name='mtapy',
    version='0.0.1',
    description='A library for multi-touch attribution',
    author='Takuya Kitazawa',
    author_email='k.takuti@gmail.com',
    license='MIT',
    url='https://github.com/takuti/mtapy',
    packages=find_packages(exclude=['*tests*']),
    install_requires=['numpy'],
)
