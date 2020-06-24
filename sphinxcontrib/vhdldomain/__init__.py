"""
    sphinxcontrib.vhdldomain
    ~~~~~~~~~~~~~~~~~~~~~~~~

    VHDL Domain

    :copyright: Copyright 20202 by Dan Chianucci <dan.chianucci@gmail.com>
    :license: MIT, see LICENSE for details.
"""

import pbr.version

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo('vhdldomain').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    return {'version': __version__, 'parallel_read_safe': True}
