from invoke import task, run

@task
def check(ctx):
    '''Check app.py syntax'''
    run('python -m py_compile app.py')
