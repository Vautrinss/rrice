from setuptools import setup

setup(name='rrice',
      version='0.2',
      description='RRice Package',
      url='https://github.com/Vautrinss/rrice',
      author='Pierre LARMANDE & Baptiste VAUTRIN',
      author_email='baptiste.vautrin@gmail.com',
      license='ICTLAB',
      packages=['rrice'],
      install_requires=[
          'requests', 'bs4', 'pandas', 'gzip', 'os' ,'json', 'sys', 

      ],
      download_url='https://github.com/Vautrinss/rrice.git',
      zip_safe=False)
