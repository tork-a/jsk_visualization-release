#!/usr/bin/env python

# script to generate Github Action workflow config file

import argparse
import sys
from collections import defaultdict

def get_argument_parser():
    parser = argparse.ArgumentParser(description="Create .github/workflows/*.yml for Github Actions")
    add = parser.add_argument
    add('distros', nargs='+', help="distros to check on github actions")
    add('--verbose', '-v', action='store_true', default=False, help="show debug message")
    return parser

def main(sysargs):
    parser = get_argument_parser()
    args = parser.parse_args(sys.argv[1:])
    distros = args.distros
    verbose = args.verbose
    #
    program = ' '.join(sys.argv)

    for distro in distros:
        print("Generate {}.yml".format(distro))
        checkout = defaultdict(lambda: 'actions/checkout@v2',hydro='actions/checkout@v1')[distro]
        container = defaultdict(lambda: 'jskrobotics/ros-ubuntu:18.04',
                                hydro  = 'jskrobotics/ros-ubuntu:12.04',
                                indigo = 'jskrobotics/ros-ubuntu:14.04',
                                kinetic= 'jskrobotics/ros-ubuntu:16.04',
                                melodic= 'jskrobotics/ros-ubuntu:18.04',
                                noetic = 'jskrobotics/ros-ubuntu:20.04')[distro]
        with open('{}.yml'.format(distro), mode='w') as f:
            f.write('''# generated by `%(program)s`
# jsk_travis
on: [push, pull_request]

jobs:
  %(distro)s:
    runs-on: ubuntu-latest
    name: %(distro)s

    container: %(container)s

    steps:
      - name: Install latest git ( use sudo for ros-ubuntu, remove sudo for ubntu container), checkout@v2 uses REST API for git<2.18, which removes .git folder and does not checkkout .travis submodules
        run: sudo apt-get update && sudo apt-get install -y software-properties-common && sudo apt-get update && sudo add-apt-repository -y ppa:git-core/ppa && sudo apt-get update && sudo apt-get install -y git
      - name: Before Checkout # need for actoins/checkout with ros-ubuntu container
        run: sudo chown -R user:jenkins $RUNNER_WORKSPACE $HOME
      - name: Chcekout
        uses: %(checkout)s
      - name: Run jsk_travis
        uses: jsk-ros-pkg/jsk_travis@master
        with:
          ROS_DISTRO : %(distro)s
''' % locals())

    # python3 test
    print("Generate python3.yml")
    with open('python3.yml', mode='w') as f:
        f.write('''# generated by `%(program)s`
# jsk_travis
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    name: check_python3

    container: ubuntu:20.04

    steps:
      - name: Chcekout
        uses: actions/checkout@v2
      - name: Check Python3
        run: |
          apt update -q && apt install -y -q python3
          python3 -m compileall .
''' % locals())

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
