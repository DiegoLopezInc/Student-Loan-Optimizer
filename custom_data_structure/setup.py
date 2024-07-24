from setuptools import Extension, setup

module = Extension('my_extension', sources=['customDataStructure.c'])

setup(
  name='MyCustomDataStructure',
  version='0.1.0',
  ext_modules=[module]
)