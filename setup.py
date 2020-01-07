from setuptools import setup

setup(name='crosswalk',
      version='0.0.0',
      description='robust spline package',
      url='https://github.com/zhengp0/crosswalk',
      author='Peng Zheng',
      author_email='zhengp@uw.edu',
      license='MIT',
      packages=['crosswalk'],
      package_dir={'crosswalk': 'src/crosswalk'},
      install_requires=['numpy',
                        'scipy',
                        'pytest',
                        'ipopt',
                        'limetr',
                        'xspline'],
      zip_safe=False)