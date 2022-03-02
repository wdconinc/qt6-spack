# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Qt6quick3d(CMakePackage):
    """A new module and API for defining 3D content in Qt Quick."""

    url      = "https://github.com/qt/qtquick3d/archive/refs/tags/v6.2.3.tar.gz"

    maintainers = ['wdconinc', 'sethrj']

    version('6.2.3', sha256='35d06edbdd83b7d781b70e0bada18911fa9b774b6403589d5b21813a73584d80')

    generator = 'Ninja'

    depends_on('cmake@3.16:', type='build')
    depends_on('ninja', type='build')
    depends_on("pkgconfig", type='build')
    depends_on("python", when='@5.7.0:', type='build')

    versions = ['6.2.3']
    for v in versions:
        depends_on('qt6declarative@{}'.format(v), when='@{}'.format(v))

    def patch(self):
        import shutil
        vendor_dir = join_path(self.stage.source_path, 'src/3rdparty')
        vendor_deps_to_keep = ['xatlas']
        with working_dir(vendor_dir):
            for dep in os.listdir():
                if os.path.isdir(dep):
                    if dep not in vendor_deps_to_keep:
                        shutil.rmtree(dep)

    def cmake_args(self):
        args = []
        return args
