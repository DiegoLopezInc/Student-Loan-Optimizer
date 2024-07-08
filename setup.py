from setuptools import Extension, setup

module = Extension('my_extension', sources=['my_extension.c'])

setup(
  name='MyCustomDataStructure',
  version='0.1.0',
  ext_modules=[module]
)
