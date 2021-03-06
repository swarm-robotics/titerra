# Copyright 2021 John Harwell, All rights reserved.
#
#  This file is part of TITERRA.
#
#  TITERRA is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  TITERRA is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with
#  TITERRA.  If not, see <http://www.gnu.org/licenses/

"""Extensions to
:class:`~sierra.plugins.platform.rosrobot.platform_generators.PlatformExpDefGenerator`
common to all TITAN scenarios which use ROS with real robots.

"""
# Core packages
import re

# 3rd party packages
from sierra.core.xml import XMLLuigi
from sierra.plugins.platform.rosrobot.generators.platform_generators import PlatformExpDefGenerator
from sierra.plugins.platform.rosrobot.generators.platform_generators import PlatformExpRunDefUniqueGenerator
from sierra.core import utils

# Project packages
from titerra.projects.common.generators import utils as tiutils
from titerra.projects.common.variables import exp_setup


class BaseScenarioGenerator(PlatformExpDefGenerator):
    def __init__(self, *args, **kwargs) -> None:
        PlatformExpDefGenerator.__init__(self, *args, **kwargs)


class ForagingScenarioGenerator(BaseScenarioGenerator):
    """
    Generates XML changes for foraging. Because we are working with real robots,
    there is no arena setup to do with SIERRA (i.e., you have to manually setup
    the environment).
    """

    def __init__(self, *args, **kwargs) -> None:
        BaseScenarioGenerator.__init__(self, *args, **kwargs)

    def generate(self) -> XMLLuigi:
        exp_def = super().generate()

        # Generate and apply time definitions for TITAN
        tiutils.generate_time(exp_def, self.cmdopts, self.spec)

        return exp_def


class ExpRunDefUniqueGenerator(PlatformExpRunDefUniqueGenerator):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def generate(self, exp_def: XMLLuigi):
        super().generate(exp_def)

        tiutils.generate_random(exp_def,
                                "./params/controllers/*",
                                self.random_seed)

        tiutils.generate_output(exp_def,
                                "./params/controllers/*",
                                self.run_output_path)


def gen_generator_name(scenario_name: str) -> str:
    res = re.search('[SDQPR][SSSLN]', scenario_name)
    assert res is not None, f"Bad block distribution in {scenario_name}"
    abbrev = res.group(0)

    return abbrev + 'Generator'


__api__ = [
    'BaseScenarioGenerator',
    'ForagingScenarioGenerator',
]
