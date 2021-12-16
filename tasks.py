from invoke import task, run

@task
def check(ctx):
    '''Check entity syntax'''
    run('python -m compileall src/*.py')

@task
def test(ctx):
    '''Run tests with ward'''
    run('ward', pty=True)
