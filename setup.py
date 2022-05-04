import setuptools

setuptools.setup {
  include_package_data = True,
  name='mycalc_pypi',
  version='0,0,1',
  description = 'oss-dev my calculator_pypi',
  author='rvjst',
  author_email='heyans93@gmail.com',
  url = "https://github.com/rvjst/test_pypi/new/main",
  download_url='https://github.com/rvjst/test_pypi/releases/tag/v0.0.1.zip",
  install_requires=["pytest"],
  long_description = 'oss-dev calculator python module',
  long_description_content_type = 'text/markdown',
  classifiers=[
     "Programming Language :: Python :: 3",
     "Operating System :: OS Independent",
  ],
}
  
