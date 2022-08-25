#!/usr/bin/python3
# task2
from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_deploy(archive_path):
    """distributes archive"""
    if archive_path is None:
        return False
    fname = archive_path.split("/")[-1]
    fnnoext = fname.split(".")[0]
    folder = "/data/web_static/releases/"
    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}{}'.format(folder, fnnoext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fname, folder, fnnoext))
        run('rm /tmp/{}'.format(fname))
        run('mv {}{}/web_static/* {}{}/'.format(folder, fnnoext, folder, fnnoext))
        run('rm -rf {}{}/web_static'.format(folder, fnnoext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(folder, fnnoext))
        return True
    except:
        return False
