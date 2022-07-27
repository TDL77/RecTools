#  Copyright 2022 MTS (Mobile Telesystems)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# pylint: disable=wrong-import-position

"""
Recommendation models (:mod:`rectools.models`)
===========================================

Convenient wrappers for popular recommendation
algorithms (ItemKNN, ALS, LightFM), also some custom
implementations.

=============================
Models
------
`models.ImplicitALSModel`
`models.ImplicitItemKNNModel`
`models.RandomModel`
=============================
"""

from .implicit_als import ImplicitALSWrapperModel
from .implicit_knn import ImplicitItemKNNWrapperModel
from .lightfm import LightFMWrapperModel
from .popular import PopularModel
from .popular_in_category import PopularInCategoryModel
from .pure_svd import PureSVDModel
from .random import RandomModel

try:
    from .dssm import DSSMModel
except ImportError:  # pragma: no cover
    from ..compat import DSSMModel  # type: ignore
try:
    from .spotlight import SpotlightFactorizationWrapperModel
except ImportError:  # pragma: no cover
    from ..compat import SpotlightFactorizationWrapperModel  # type: ignore

__all__ = (
    "ImplicitALSWrapperModel",
    "ImplicitItemKNNWrapperModel",
    "SpotlightFactorizationWrapperModel",
    "LightFMWrapperModel",
    "PopularModel",
    "PopularInCategoryModel",
    "PureSVDModel",
    "RandomModel",
    "DSSMModel",
)