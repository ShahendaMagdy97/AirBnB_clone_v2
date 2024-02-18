#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static"""

from fabric.api import *
from datetime import datetime


@task
def do_pack():
    """archive web_static"""
    try:
        f_current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = f'web_static_{f_current_time}.tgz web_static'
        local("mkdir -p versions")
        local(f"tar -cvzf versions/{file_name} web_static")
        return "versions/"
    except Exception as e:
        return None
