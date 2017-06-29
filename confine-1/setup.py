from setuptools import setup

setup(name='confine',
      version='01',
      description='identifying disease module',
      url='https://github.com/asherameli/confine',
      author='Asher Ameli',
      author_email='aameli@bwh.harvard.edu',
      license='SharmaLab - Channing Division of Network Medicine',
      packages=['confine'],
      zip_safe=False,
      include_package_data = True,
      long_description=open('read_ME.txt').read())

