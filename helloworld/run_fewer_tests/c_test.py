# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.run_fewer_tests import c as mod


def test_run() -> None:
    mod.run()
