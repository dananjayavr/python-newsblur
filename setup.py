from setuptools import setup
from newsblur import __version__

long_description = open('README.rst').read()

setup(name='newsblur',
      version=__version__,
      py_modules=['newsblur'],
      description='API Wrapper library for newsblur.com',
      author='Dananjaya Ramanayake',
      author_email='dananjaya86@gmail.com',
      license='MIT',
      url='',
      long_description=long_description,
      platforms=['any'],
      classifiers=['Development Status :: 1 - Beta',
	           'Intended Audience :: Developers',
		   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
		   'Programming Language :: Python',
		   'Topic :: Internet :: WWW/HTTP :: News/RSS',
		  ]
      entry_points={'console_scripts':['newsblur=newsblur:main']},
      )
