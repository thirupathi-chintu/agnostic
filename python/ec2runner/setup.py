from setuptools import setup

setup(
    name="ec2runner-2018",
    version="2018-11-01-0.1",
    author="Dariush Azimi",
    author_email="azimid@gmail.com",
    description="ec2runner-2018 is a tool to manage AWS EC2 snapshots, list,stop,start intances and show related volumes",
    license="GPLv3+",
    packages=['ec2runner'],
    url="https://github.com/dariushazimi/ec2runner",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        ec2runner=ec2runner.ec2runner:cli
        '''

)
