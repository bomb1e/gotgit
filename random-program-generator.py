#!/usr/bin/env python

from __future__ import print_function

import random
import uuid

from pgen import pgen_opts, ProgGenerator
from pygen.cgen import CodeGenerator

unique = str(uuid.uuid4()) + '.py'

if __name__ == "__main__":
    pgen = ProgGenerator(pgen_opts, random.Random())

    m = pgen.generate()

    cgen = CodeGenerator()

    output = cgen.generate(m)

file = open(unique, 'w')
file.write(output)
file.close()
