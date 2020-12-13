from setuptools import setup

setup(
    name='AlphaCoderSpider',
    version='0.0.1',
    packages=['AlphaCoderSpider'],
    url='https://github.com/rcsupermanjob/AlphaCoderSpider',
    license='GPLv3',
    author='rcsuperman',
    author_email='',
    description='An AlphaCoder Spider',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['httpx', 'flask', 'loguru', 'parse']

)
