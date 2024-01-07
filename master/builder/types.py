# -*- coding: utf-8 -*-
from buildbot.process.factory import (
    BasicBuildFactory,
    BasicSVN,
    BuildFactory,
    CPAN,
    Distutils,
    GNUAutoconf,
    QuickBuildFactory,
    Trial,
)
from buildbot.process.properties import Interpolate

from buildbot.steps.cmake import CMake
from buildbot.steps.shell import ShellCommand
from buildbot.steps.source.git import Git
