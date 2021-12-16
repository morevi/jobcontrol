from invoke import task, run

@task
def check(ctx):
    '''Check entity syntax'''
    run('python -m compileall src/*.py')

@task
def test(ctx):
    '''Run tests with ward'''
    run('ward', pty=True)

@task
def docker_build(ctx):
    '''Build image'''
    run('docker build -t morevi/jobcontrol .')

@task
def docker_push(ctx):
    '''Push container'''
    run('docker push morevi/jobcontrol', pty=True)

@task
def docker_run(ctx):
    '''Run tests with docker and ward'''
    run('docker run -t -v `pwd`:/app/test morevi/jobcontrol', pty=True)
