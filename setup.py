from setuptools import setup, find_packages

requirements = open("requirements.txt").readlines()


setup(name="blackjack",
      version="0.0.1",
      author="Oz N Tiram",
      author_email='oz.tiram@gmail.com',
      url="https://github.com/oz123/blackjack",
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      install_requires=requirements,
      entry_points={
          'console_scripts': ["blackjack=blackjack.cli:main"],
        }
      )