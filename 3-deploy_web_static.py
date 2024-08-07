#!/usr/bin/python3
# Creates and distributes an archive to your web servers
# using the function deploy
from datetime import datetime
import os.path
from fabric.api import run, env, local, put, task, runs_once

"""Set the remote host"""
env.hosts = ["34.227.94.151", "52.201.220.15"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

env.roledefs = {
    'hosts': [env.hosts[0]],
}


@runs_once
@task
def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    size = os.path.getsize(file)
    print(f"web_static packed: {file} -> {size}Bytes)")
    return file


@task
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
    print("New version deployed!")
    return True


@task
def deploy():
    """Calls the do_pack function store path to created archive
    Call the do_deploy function with the path
    Return: False if no archive is created, value of do_deploy on success
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
