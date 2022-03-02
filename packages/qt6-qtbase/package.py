# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Qt6Qtbase(CMakePackage):
    """Qt Base (Core, Gui, Widgets, Network, ...)"""

    homepage = "https://www.qt.io"
    url      = "https://github.com/qt/qtbase/archive/refs/tags/v6.2.3.tar.gz"

    maintainers = ['wdconinc', 'sethrj']

    version('6.2.3', sha256='2dd095fa82bff9e0feb7a9004c1b2fb910f79ecc6111aa64637c95a02b7a8abb')

    generator = 'Ninja'

    depends_on('cmake@3.16:', type='build')
    depends_on('ninja', type='build')
    depends_on("pkgconfig", type='build')
    depends_on("python", when='@5.7.0:', type='build')

    # Dependencies, then variant- and version-specific dependencies
    depends_on('at-spi2-core')
    depends_on('dbus')
    depends_on('double-conversion')
    depends_on('fontconfig')
    depends_on("freetype")
    depends_on("harfbuzz")
    depends_on("jpeg")
    depends_on('libdrm')
    depends_on('libjpeg')
    depends_on("libmng")
    depends_on('libproxy')
    depends_on("libtiff")
    depends_on('libxkbcommon')
    depends_on("libxml2")
    depends_on('libxrender')
    depends_on('gl')
    depends_on('pcre2+multibyte')
    depends_on("sqlite")
    depends_on("zlib")
    depends_on("zstd")
    depends_on("icu4c")

    def patch(self):
        import shutil
        vendor_dir = join_path(self.stage.source_path, 'src/3rdparty')
        vendor_deps_to_keep = [
            'blake2', 'easing', 'forkfd', 'freebsd',
            'icc', 'md4', 'md4c', 'md5', 'rfc6234',
            'sha1', 'sha3', 'tinycbor', 'VulkanMemoryAllocator',
        ]
        with working_dir(vendor_dir):
            for dep in os.listdir():
                if os.path.isdir(dep):
                    if dep not in vendor_deps_to_keep:
                        shutil.rmtree(dep)

    def cmake_args(self):
        args = [
            self.define('FEATURE_system_doubleconversion', True),
            self.define('FEATURE_system_freetype', True),
            self.define('FEATURE_system_harfbuzz', True),
            self.define('FEATURE_system_jpeg', True),
            self.define('FEATURE_system_libb2', False),
            self.define('FEATURE_system_pcre2', True),
            self.define('FEATURE_system_png', True),
            self.define('FEATURE_system_proxies', True),
            self.define('FEATURE_system_sqlite', True),
            self.define('FEATURE_system_textmarkdownreader', False),
            self.define('FEATURE_system_zlib', True),
        ]
        return args
