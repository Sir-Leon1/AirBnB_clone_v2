#!/usr/bin/python3
# Fabrfile to generate a .tgz archive from the contents of web_static
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)

    if os.path.isdir("version") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    size = os.path.getsize(file)
    print(f"web_static packed: {file} -> {size}Bytes)")
    return file
