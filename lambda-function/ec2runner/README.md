# ec2runner script to start, stop instances and manage snaps
Build with :heart:

AWS: Manage AWS Ec2 instance snapshots, start and stop instances, display the list of instances along with volumes and snapshots.

## About:pencil2:

This project uses boto3 to manage AWS EC2 instances and snapshots.

## Configuring :wrench:

ec2runner uses the configuration file created by the AWS cli. e.g.

`aws configure --profile ec2runner`

## Installing ec2runner 2018 as a package
#TODO

`pip3 install
https://github.com/dariushazimi/ec2runner/blob/master/dist/ec2runner_2018-2018_11_01_0.1-py3-none-any.whl
`

To verify that is installed

` pip3 show ec2runner-2018`


## Running :rocket:
### Updated

` ec2runner instances list`
` ec2runner instances stop`
` ec2runner instances start`
```
Commands:
  instances  Commands for instances
  snapshots  Commands for snapshots
  volumes    Commands for volumes
  ```

--Old setup
To run the script

`pipenv run python ec2runner/ec2runner.py <command> <subcommand>--project=PROJECTNAME`

*command* is instances, volumes, or snapshots
*subcommand*  - depends on the command
*project* is optional 

the list of commands to run:
-   list   List ec2 instances
-   start  Start Ec2 instances
-   stop   Stop Ec2 instances

Options:
~ --help  Show this message and exit.



Each command has its own help as well.:
`pipenv run python ec2runner/ec2runner.py list --help`

Usage:
ec2runner.py-list [OPTIONS]
List Ec2 instances
Options:

project Dariush Only instances for project (tag Project:Dariush)
help            Only this message and exit.

## Examples - Latest version
 Start instances with taged with project "spider"
```
 pipenv run python ec2runner/ec2runner.py start --project=spider
 pipenv run python ec2runner/ec2runner.py --help
 pipenv run python ec2runner/ec2runner.py instances --help
 pipenv run python ec2runner/ec2runner.py instances list --help
 pipenv run python ec2runner/ec2runner.py instances stop --help
 pipenv run python ec2runner/ec2runner.py instances stop
 pipenv run python ec2runner/ec2runner.py instances stop --project=spider
 pipenv run python ec2runner/ec2runner.py volumes list

 ```

 #### :rotating_light:Update: List ec2 snapshots with volumes:rotating_light:

  ```
  pipenv run python ec2runner/ec2runner.py snapshots list
  ```
  Output:
```  
snap-008d7, vol-06ffb, i-09e2b, 100%, Fri Nov  2 02:31:11 2018, Not Encrypted
```

### Instance Lifecycle

![aws instance lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/instance_lifecycle.png)

### Note: 
boto3 list the snapshots in chronological order with the most recent one at the top.

The latest commit will show the most recent sussessful snap
```
pipenv run python ec2runner/ec2runner.py snapshots list
pipenv run python ec2runner/ec2runner.py snapshots list --all
pipenv run python ec2runner/ec2runner.py instances snapshot
pipenv run python ec2runner/ec2runner.py snapshots list --help
```
More updates to come.

code is never finished only abandoned :art:
### How to package your code 
Install setup tools with -d since you only need it for development
`pipevn install -d setuptools`

Next we create a `setup.py` file.
`setup.py` file essentially tells setuptools how to build your package
It does this by creating a function called setup

here is the `setup.py` file

```
from setuptools import setup

setup(
    name="ec2runner-2018",
    version="2018-11-01-0.1",
    author="Dariush Azimi",
    author_email="my email addr",
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
```
Save the file.
Next we need to generate a wheel file
Here is how to create the wheel file

` pipenv run python setup.py bdist_wheel`

Take a look inside the dist folder
`ls -al dist`

The wheel file is a python code that lets your script run
Now that we have the package we can install it like any other package `pip3 install ec2runner_2018-2018_11_01_0.1-py3-none-any.whl`

To see that is installed on your system do:
`pip3 show ec2runner-2018`

Now you can run 
` ec2runner instances list`

Now that you have the wheel file you can install it on any machine that has python3, even windows.
All done in a few simple steps

[<img src="https://github.com/dariushazimi/ec2runner/blob/master/ec2-diagram-20181113172010.svg">]()