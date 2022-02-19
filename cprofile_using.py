#!/usr/bin/env python3
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e2)))"
)
