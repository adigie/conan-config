#!/usr/bin/env python

import itertools
import os

archs = ["cortex-m0", "cortex-m0plus", "cortex-m3", "cortex-m4", "cortex-m7"]
build_types = ["Debug", "Release"]

template = """
[settings]
os=Generic
arch={}
compiler=gcc
compiler.version=8
build_type={}

[options]

[build_requires]
cortex-m-toolchain/0.1.0@adigie/testing

[env]
"""

for (arch, build_type) in itertools.product(archs, build_types):
    path = os.path.join("profiles", "{}-{}".format(arch, build_type.lower()))
    with open(path, "w") as profile:
        print(template.format(arch, build_type), file=profile)