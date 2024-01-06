# -*- coding: utf-8 -*-
# -*- python -*-
# ex: set filetype=python:
import sys

from twisted.application import service
from buildbot.master import BuildMaster
from twisted.python.log import ILogObserver, FileLogObserver

basedir = "/data/buildbot"
configfile = "master.cfg"

application = service.Application("buildmaster")
application.setComponent(ILogObserver, FileLogObserver(sys.stdout).emit)

m = BuildMaster(basedir, configfile, umask=None)
m.setServiceParent(application)
