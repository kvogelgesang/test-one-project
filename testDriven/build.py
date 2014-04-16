from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.pylint")
use_plugin("python.distutils")
use_plugin("python.pydev")
# use_plugin("python.integrationtest")

name = 'test-one-project'
version = '0.1.0'
summary = 'my python test project'

default_task = ["analyze", "publish"]


@init
def set_properties(project):
    project.set_property('dir_source_unittest_python', 'src/test')
    #project.set_property('dir_source_integrationtest_python', 'src/integrationtest/python/gomez2graphite')


@init(environments='teamcity')
def set_properties_for_teamcity_builds(project):
    import os
    project.version = '%s-%s' % (project.version, os.environ.get('BUILD_NUMBER', 0))
    project.default_task = ['install_dependencies', 'publish']
