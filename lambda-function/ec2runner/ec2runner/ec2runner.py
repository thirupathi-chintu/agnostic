# Author Dariush Azimi
# Date Nov 1, 2018
# Print a list of ec2 instances for a project tag (project tag is optional)
# pipenv install pylint --d
# Example:
# pipenv run python ec2runner/ec2runner.py --project=spider (in this case
# the project tag is set to spider on the ec2 instances)
# Adding botocore to use the exception block to catch the state of the intance

import boto3
import botocore
import click

session = boto3.Session(profile_name='ec2runner')
ec2 = session.resource('ec2')


def filter_instances(project):
    instances = []
    if project:
        filters = [{'Name': 'tag:project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances


def has_pending_snapshot(volume):
    snapshots = list(volume.snapshots.all())
    return snapshots and snapshots[0].state == 'pending'


@click.group()
def cli():
    """ec2runner manages snapshots"""


@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""


@snapshots.command('list')
@click.option('--project', default=None, 
              help="only volumes for project (tag project:<name>)")
@click.option('--all', 'list_all', default=False, is_flag=True, 
              help="List all snapshots for each volume, not just the most recent one for project (tag project:<name>)")
def list_snapshots(project, list_all):
    '''
    List snapshots
    pipenv run python ec2runner/ec2runner.py snapshots list
    pipenv run python ec2runner/ec2runner.py snapshots list --all
    pipenv run python ec2runner/ec2runner.py snapshots list --help
    '''

    instances = filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(', '.join((
                    s.id,
                    v.id,
                    i.id,
                    s.progress,
                    s.start_time.strftime("%c"),
                    s.encrypted and "Encrypted" or "Not Encrypted"
                )))
                # Only show the most recent successful snap
                # pipenv run python ec2runner/ec2runner.py snapshots list
                if s.state == 'completed' and not list_all: break
    return


@cli.group('volumes')
def volumes():
    """Commands for volumes"""


@volumes.command('list')
@click.option('--project', default=None, help="only volumes for project (tag project:<name>)")
def list_volumes(project):
    '''
    List volumes
    '''

    instances = filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            print(', '.join((
                v.id,
                i.id,
                v.state,
                str(v.size) + "GiB",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))
    return


@cli.group('instances')
def instances():
    """ Commands for instances"""


@instances.command('snapshot', help="Create snapshots of all volumes")
@click.option('--project', default=None, help="only intances for project (tag project=<name>)")
def create_snapshot(project):
    ''' Create snapshots for ec2 instances
        Examples, list instances, start instances and take snap
        pipenv run python ec2runner/ec2runner.py instances list
        pipenv run python ec2runner/ec2runner.py instances start
        pipenv run python ec2runner/ec2runner.py instances snapshot --project="spider"

    '''
    instances = filter_instances(project)

    for i in instances:
        print("stopping {0}... ".format(i.id))
        i.stop()
        i.wait_until_stopped()
        # wait for the instances to stop befor taking snapshots
        for v in i.volumes.all():
            if has_pending_snapshot(v):
                print("   Skipping {0}, snapshot already in progress".format(v.id))
                continue

            print("   +++ Creating snapshot of {0}".format(v.id))
            v.create_snapshot(Description="Created by snapshot_analyzer 2018v1101")
        # restart the instance once the snapshot has started
        print("starting {0}...".format(i.id))
        i.start()
        # We don't need to wait for the snapshot to complete
        # Once the snapshot process has started
        # Its safe to start the instance
        # wait till the intance is running to make sure
        # one of our instances are stopped at any given datetime A combination of a date and a time. Attributes: ()
        # if in prod, and instances are servicing client, you want to make sure
        # you kick off the snapshot for one instance datetime A combination of a date and a time.

    print("Job's done!")
    return


@instances.command('list')
@click.option('--project', default=None, help="only intances for project (tag project=<name>)")
def list_instances(project):
    '''
    List EC2 instances
    '''
    instances = filter_instances(project)
    for i in instances:
        # if there is an instance with no tags, retrun an empty list
        tags = {t['Key']: t['Value'] for t in i.tags or []}
        print(' '.join((
            tags.get('Name', '<no name>'),
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('project', '<no project>')
        )))

    return


@instances.command('stop')
@click.option('--project', default=None, help="only instance for project (tag project=<name>")
def stop_instances(project):
    "Stop Ec2 instances"
    instances = filter_instances(project)
    for i in instances:
        try:
            if i.state['Name'] == 'stopped':
                print("Instance {0}. is already stopped".format(i.id))
            else:
                print(" Stopping {0}... ".format(i.id))
                i.stop()
        except botocore.exceptions.ClientError as e:
            print(" Could not stop {0} ".fromat(i.id) + str(e))
            continue

    return


@instances.command('start')
@click.option('--project', default=None, help="only instance for project (tag project=<name>")
def start_instances(project):
    "Start Ec2 instances"
    instances = filter_instances(project)
    for i in instances:
        try:
            if i.state['Name'] == 'running':
                print("Instance {0}. is already running".format(i.id))
            else:
                i.start()
        except botocore.exceptions.ClientError as e:
            print("Could not start {0}. ".format(i.id) + str(e))
            continue

    return


@instances.command('reboot')
@click.option('--project', default=None, help="only instance for project (tag project=<name>")
def reboot_instances(project):
    "Reboot Ec2 instances"
    ''' Check instance state to make sure it is running.
         if instance is stopped, start instance, otherwise stop and then start.
         AWS throttle the API access so, If you reboot multiple instances at once this will create a bit of problem. 
        You might want to put a sleep for like 5 seconds between each attempt
    '''

    instances = filter_instances(project)
    for i in instances:
        print(i)
        try:
            if i.state['Name'] == 'stopped':
                print("Instance {0}... is stopped".format(i.id))
                print("Starting {0}... starting...".format(i.id))
                i.start()
                i.wait_until_running()
                print("Started {0}. ".format(i.id))

            elif i.state['Name'] == 'pending':
                print("pending.... {0}. ".format(i.id))
                i.wait_until_running()
                i.stop()
                i.wait_until_stopped()
            elif i.state['Name'] == 'stopping':
                print("stopping.... {0}. ".format(i.id))
                i.wait_until_stopped()
                i.start()
            else:
                print("Stopping {0}... is stopping".format(i.id))
                i.stop()
                i.wait_until_stopped()
                print("Stopped {0}. ".format(i.id))
                print("Starting {0}... starting...".format(i.id))
                i.start()
                print("Started {0}. ".format(i.id))

        except botocore.exceptions.ClientError as e:
            print("Error rebooting {0}. ".format(i.id) + str(e))
            continue
    return


if __name__ == '__main__':
    cli()
