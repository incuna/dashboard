from fabric.api import cd, env, run, sudo

env.user = 'incuna'
env.group = 'www-data'
env.path = '/var/www/dashboard.incuna.com/'
env.branch = 'master'
env.project_short_name = 'dashboard'
env.hosts = ['braekel.incuna.com']
env.supervisor_name = 'dashboard'

def update(pip = False, build_static = False, migrate = False):
    with cd(env.path):
        run('git fetch')
        changed_files = run('git status --rev .:tip')

        run('git checkout %s' % env.branch)

        if "requirements.txt" in changed_files or pip:
            print "pip"
            pip = True
            run('bin/pip install -r requirements.txt')

        if "/media/" in changed_files or build_static or pip:
            print 'build_static'
            run('bin/python ght/manage.py build_static --noinput', pty=True)

        if "/migration/" in changed_files or migrate or pip:
            print "migrate"
            run('bin/python ght/manage.py migrate')

        if changed_files:
            # Could do it that we don't restart if only templates change?
            sudo('supervisorctl restart %s:* ' % (env.supervisor_name,))

