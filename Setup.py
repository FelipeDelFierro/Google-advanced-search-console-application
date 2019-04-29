from setuptools import setup,find_packages
 
setup(name="Scraping Google Search Results",  
      version="0.1",  
      description="This Script let you create an advanced search in google and export the results in a csv file",
      author="Felipe Del Fierro",
      Business="Here Technologies",
      author_email='felipe.delfierro@here.com',
      license="Here Technologies",
      packages=find_packages(),
      install_requires=[i.strip() for i in open("requirements.txt").readlines()],
)