#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers using the function do_deploy.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Distributes an archive to web servers."""

    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        path_no_ext = '/data/web_static/releases/' + archive_name.split('.')[0]

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path_no_ext))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, path_no_ext))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}'.format(path_no_ext, path_no_ext))
        run('rm -rf {}/web_static'.format(path_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path_no_ext))

        return True

    except Exception as e:
        return False

