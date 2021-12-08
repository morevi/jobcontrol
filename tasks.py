from invoke import task, run

@task
def check(ctx):
    '''Check entity syntax'''
    run('python -m py_compile src/horario.py')
