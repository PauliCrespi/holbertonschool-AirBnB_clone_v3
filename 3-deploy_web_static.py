#!/usr/bin/python3
# task 3


from 1-pack_web_static.py import do_pack()
from 2-do_deploy_web_static.py import do_deploy(archive_path)
env.hosts = ['web-01.paulinacrespihs.tech', 'web-02.paulinacrespihs.tech']


def deploy():
    """func"""
    path = do_pack()
    if path is None:
        return False
    return (do_deploy(archive_path))
