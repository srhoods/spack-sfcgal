# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Author: Steven Rhoods <git@rhoods.com>

from spack import *


class Sfcgal(CMakePackage):
    """SFCGAL is a C++ wrapper library around CGAL with the aim of
       supporting ISO 191007:2013 and OGC Simple Features for 3D operations.
    """
    homepage = "http://www.sfcgal.org/"
    url      = "https://github.com/Oslandia/SFCGAL/archive/v1.3.7.tar.gz"

    version('1.3.7', sha256='30ea1af26cb2f572c628aae08dd1953d80a69d15e1cac225390904d91fce031b')
    version('1.3.5', sha256='e36937d1d8421134c601e80a42bd535b1d9d7e7dd5bdf4da355e58942ba56006')
    version('1.3.4', sha256='87b49359eb2d88dae5f622e66e90f5efc40b675ca7885ad0cd62455803ef305f')
    version('1.3.3', sha256='57e0237b328b519ef0e274f0a24b4c266e9d5541214a3911bd68fe861a01240c')
    version('1.3.2', sha256='1ae0ce1c38c728b5c98adcf490135b32ab646cf5c023653fb5394f43a34f808a')
    version('1.3.1', sha256='37671101381eb10e0896bba3543c0c6d94fbb80e2ef49497f37ec80aef12860b')
    version('1.3.0', sha256='7ed35439fc197e73790f4c3d1c1750acdc3044968769239b2185a7a845845df3')
    version('1.2.2', sha256='dae7de4c7e1b4ef2a51c55f7d201a6d8049b518caac14f4033fd2d43f14eb031')
    version('1.2.1', sha256='928875941be8e9072698f35c1b9a119fed7cad11f71ef0785d49e0d03b765119')
    version('1.2.0', sha256='aeab3ddd7b4eff2b9b6b365ca1731de693d7a788914d4190f444ef59dead5a47')

    variant('examples', default=False,
            description='Build SFCGAL examples')

    variant('tests', default=False,
            description='Build unit, garden and regress tests')

    variant('bench', default=False,
            description='Build benchmarks')

    variant('osg', default=False,
            description='Compile with OpenSceneGraph support')

    depends_on('cmake')

    depends_on('cgal@4.13+core', when='@1.3.2:1.3.7')
    depends_on('cgal@4.7+core', when='@1.2.1:1.3.1')
    depends_on('cgal@4.6.3+core', when='@1.2.0')

    depends_on('mpfr')
    depends_on('gmp')
#    depends_on('boost@1.61.0')
    depends_on('boost@1.66.0')

    depends_on('openscenegraph', when='+osg')

    def cmake_args(self):
        spec = self.spec

        return [
            '-DSFCGAL_BUILD_EXAMPLES:BOOL=%s' %
            ('YES' if '+examples' in spec else 'NO'),
            '-DSFCGAL_BUILD_TESTS:BOOL=%s' %
            ('YES' if '+tests' in spec else 'NO'),
            '-DSFCGAL_BUILD_BENCH:BOOL=%s' %
            ('YES' if '+bench' in spec else 'NO'),
            '-DSFCGAL_WITH_OSG:BOOL=%s' %
            ('YES' if '+osg' in spec else 'NO'),
        ]