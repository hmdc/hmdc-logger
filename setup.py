from distutils.core import setup

setup(name='HMDCLogger',
      version='1.1',
      author='Bradley Frank',
      author_email='bfrank@hmdc.harvard.edu',
      url='https://github.com/hmdc/hmdc-logger',
      description='Wrapper for the logging module.',
      license='GPLv2',
      packages=['hmdclogger'],
      requires=['inspect','logging','os','sys']
)
