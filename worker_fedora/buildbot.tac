# -*- coding: utf-8 -*-
# -*- python -*-
# ex: set filetype=python:

import os
import sys

from buildbot_worker.bot import Worker
from twisted.application import service
from twisted.python.log import ILogObserver, FileLogObserver

basedir = "/data/buildbot"

application = service.Application("buildbot-worker")
application.setComponent(ILogObserver, FileLogObserver(sys.stdout).emit)

buildmaster_host = os.environ.get("BUILDMASTER", "localhost")
port = int(os.environ.get("BUILDMASTER_PORT", 9989))
workername = os.environ.get("WORKERNAME", "docker")
passwd = os.environ.get("WORKERPASS")

keepalive = 600
umask = None
maxdelay = 300
allow_shutdown = None
maxretries = 10
delete_leftover_dirs = False
protocol = "pb"

s = Worker(
    buildmaster_host,
    port,
    workername,
    passwd,
    basedir,
    keepalive,
    umask=umask,
    maxdelay=maxdelay,
    protocol=protocol,
    allow_shutdown=allow_shutdown,
    maxRetries=maxretries,
    delete_leftover_dirs=delete_leftover_dirs,
)
s.setServiceParent(application)
