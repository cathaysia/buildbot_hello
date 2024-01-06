# -*- coding: utf-8 -*-
# -*- python -*-

from buildbot.plugins import steps, util, worker

WORKER_INFO = worker.Worker("worker_fedora", "pass")


def get_worker():
    factory = util.BuildFactory()
    # check out the source
    factory.addStep(
        steps.Git(
            repourl="https://github.com/buildbot/hello-world.git", mode="incremental"
        )
    )
    # run the tests (note that this will require that 'trial' is installed)
    factory.addStep(
        steps.ShellCommand(command=["trial", "hello"], env={"PYTHONPATH": "."})
    )
    return util.BuilderConfig(
        name="runtests", workernames=["worker_fedora"], factory=factory
    )
