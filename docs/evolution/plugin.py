#
# Copyright (c) 2013-2018 Quarkslab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

from .skeleton import Skeleton

from lib.plugins import PluginBase, PluginLoadError
from lib.irma.common.utils import IrmaProbeType

class SkeletonPlugin(PluginBase, Skeleton):

    # =================
    #  plugin metadata
    # =================
    _plugin_name_ = "Skeleton"
    _plugin_display_name_ = Skeleton._name
    _plugin_author_ = "IRMA (c) Quarkslab"
    _plugin_version_ = "1.0.0"
    _plugin_category_ = "custom"
    _plugin_description_ = "Plugin skeleton"
    _plugin_dependencies_ = []
    _mimetype_regexp = None

    # =============
    #  constructor
    # =============

    def __init__(self):
        self.module = Skeleton()
