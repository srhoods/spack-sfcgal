# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Openscenegraph(CMakePackage):
    """OpenSceneGraph is an open source, high performance 3D graphics toolkit
       that's used in a variety of visual simulation applications."""

    homepage = "http://www.openscenegraph.org"
    url      = "https://github.com/openscenegraph/OpenSceneGraph/archive/OpenSceneGraph-3.2.2.tar.gz"

    version('3.6.3',     sha256='51bbc79aa73ca602cd1518e4e25bd71d41a10abd296e18093a8acfebd3c62696')
    version('3.6.2',     sha256='762c6601f32a761c7a0556766097558f453f23b983dd75bcf90f922e2d077a34')
    version('3.6.1',     sha256='777429556818184588ee5f2351fe262f105539bfc4393c373bc933025bd16a33')
    version('3.6.0',     sha256='6f57134ea74a39f1c7b24c285e6278cf906c47f6c681573b86d12173a466efed')
    version('3.5.10',    sha256='344e76b92eecd10a324e7920c6a0fa7521de69a9cd5c75f5386756b4510781be')
    version('3.5.9',     sha256='e18bd54d7046ea73525941244ef4f77b38b2a90bdf21d81468ac3874c41e9448')
    version('3.2.3',     sha256='a1ecc6524197024834e1277916922b32f30246cb583e27ed19bf3bf889534362')
    version('3.2.2',     sha256='df68b85999de545885e2deb1723a97c248534cf428732fd8d8f9e18bf14986d1')

    variant('shared', default=True, description='Builds a shared version of the library')

    depends_on('cmake@2.8.7:', type='build')
    depends_on('qt')
    depends_on('zlib')
    depends_on('xrandr')

    def cmake_args(self):
        spec = self.spec

        shared_status = 'ON' if '+shared' in spec else 'OFF'

        args = [
            '-DDYNAMIC_OPENSCENEGRAPH={0}'.format(shared_status),
            '-DDYNAMIC_OPENTHREADS={0}'.format(shared_status),
            '-DZLIB_INCLUDE_DIR={0}'.format(spec['zlib'].prefix.include),
            '-DZLIB_LIBRARY={0}/libz.{1}'.format(spec['zlib'].prefix.lib,
                                                 dso_suffix),
            '-DBUILD_OSG_APPLICATIONS=OFF',
            '-DOSG_NOTIFY_DISABLED=ON',
            '-DLIB_POSTFIX=',
        ]

        # NOTE: This is necessary in order to allow OpenSceneGraph to compile
        # despite containing a number of implicit bool to int conversions.
        if spec.satisfies('%gcc'):
            args.extend([
                '-DCMAKE_C_FLAGS=-fpermissive',
                '-DCMAKE_CXX_FLAGS=-fpermissive',
            ])

        return args