# -*- coding: utf-8 -*-
"""
    sphinxcontrib.vhdldomain
    ~~~~~~~~~~~~~~~~~~~~~~~~

    VHDL Domain

    :copyright: Copyright 20202 by Dan Chianucci <dan.chianucci@gmail.com>
    :license: MIT, see LICENSE for details.
"""

from sphinx.domains import Domain


class VHDLDomain(Domain):
    pass


def setup(app):
    app.add_domain(VHDLDomain)
