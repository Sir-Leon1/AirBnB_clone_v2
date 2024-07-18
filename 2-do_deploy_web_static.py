#!/usr/bin/python3
# Fabrfile to generate a .tgz archive from the contents of web_static
import os.path
from fabric.api import local, run, env, put


"""Set the remote host"""
env.hosts = ["34.227.94.151", "52.201.220.15"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if (
        run(
            "sudo rm -rf /data/web_static/releases/{}/".format(name)
        ).failed
        is True
    ):
        return False
    if (
        run(
            "sudo mkdir -p /data/web_static/releases/{}/".format(name)
        ).failed
        is True
    ):
        return False
    if (
        run(
            "sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                file, name
            )
        ).failed
        is True
    ):
        return False
    if run("sudo rm -rf /tmp/{}".format(file)).failed is True:
        return False
    if (
        run(
            "sudo mv /data/web_static/releases/{}/web_static/*"
            " /data/web_static/releases/{}/".format(name, name)
        ).failed
        is True
    ):
        return False
    if (
        run(
            "sudo rm -rf /data/web_static/releases/{}/web_static".format(
                name
            )
        ).failed
        is True
    ):
        return False
    if run("sudo rm -rf /data/web_static/current").failed is True:
        return False
    if (
        run(
            "sudo ln -sf /data/web_static/releases/{}/"
            " /data/web_static/current".format(
                name
            )
        ).failed
        is True
    ):
        return False
    return True
