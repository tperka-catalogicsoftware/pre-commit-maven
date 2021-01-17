from __future__ import print_function

import os.path

from pre_commit_maven.utils import shell
from pre_commit_maven.utils.shell import ExecutionResult


class Colours:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def get_maven_path(cwd: str, shell_runner=shell):
    path = ""
    mvn_wrapper_path = os.path.join(cwd, "mvnw")
    if shell_runner.exists_file(mvn_wrapper_path):
        path = mvn_wrapper_path
    else:
        path = "mvn"
    return path


def execute_goals(goals: list, cwd: str, shell_runner=shell):
    assert goals is not None and len(goals) > 0, "goals not specified"
    cmd = [get_maven_path(cwd, shell_runner), "-B"] + goals
    return shell_runner.execute(cmd, cwd=cwd)


def print_error(execution_result: ExecutionResult, print_fn=print):
    for line in execution_result.stdout.splitlines():
        if line.startswith("[ERROR]"):
            print_fn(f"{Colours.FAIL}{line}{Colours.ENDC}")
