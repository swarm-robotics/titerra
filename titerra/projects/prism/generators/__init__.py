# Copyright 2021 John Harwell, All rights reserved.
#
#  This file is part of SIERRA.
#
#  SIERRA is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  SIERRA is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with
#  SIERRA.  If not, see <http://www.gnu.org/licenses/

# Core packages
import sys

# 3rd party packages

# Common TITAN packages to lift into 'prism.generators' namespace
from projects.common.generators import scenario_generator_parser
from projects.common.generators import exp_generators

# Do the lifts
sys.modules['projects.prism.generators.scenario_generator_parser'] = scenario_generator_parser
sys.modules['projects.prism.generators.exp_generators'] = exp_generators
