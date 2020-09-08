from setuptools import setup

scripts = ['PredLnc-GFStack.py']
setup(
    name='PredLnc-GFStack-wrapper',
    version='0.1.0',
    packages=['predlncgfstack'],
    url='',
    scripts=scripts,
    license='',
    include_package_data=True,
    package_data={'': ['Human_model/*', 'Mouse_model/*','bin/*']},
    author='CHEN Yuelong',
    author_email='yuelong.chen.btr@gmail.com',
    description='''
This is a wrapper of PredLnc-GFStack algorithm. Download from original source, [https://github.com/BioMedicalBigDataMiningLab/PredLnc-GFStack/](https://github.com/BioMedicalBigDataMiningLab/PredLnc-GFStack/), would be perfect.

This wrapper is just for myself easy use.

Almost whole codes were from [https://github.com/BioMedicalBigDataMiningLab/PredLnc-GFStack/](https://github.com/BioMedicalBigDataMiningLab/PredLnc-GFStack/). I just modified the structure and install setup.py for myself easier use.

    '''
)
