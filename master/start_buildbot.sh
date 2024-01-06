#!/bin/bash

buildbot upgrade-master buildbot
exec twistd --pidfile= -ny /data/buildbot/buildbot.tac
