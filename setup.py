from setuptools import setup, find_packages

setup(name='django-geocoder',
      version='0.1',
      description='Python geocoder wrapper for Django',
      url='https://github.com/jestocke/django-geocoder',
      author='Jestocke',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'django>=1.8',
          'geocoder==1.15.1',
          'django-memoize==1.3.1'
      ],
      zip_safe=False)