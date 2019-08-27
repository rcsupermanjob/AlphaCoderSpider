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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=['requests', 'flask']
)
