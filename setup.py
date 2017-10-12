from setuptools import setup, find_packages

requirements = open("requirements.txt").readlines()


setup(name="blackjack",
      setup_requires=['pbr>=1.9',
                      'setuptools>=17.1'],
      pbr=True,
      )
