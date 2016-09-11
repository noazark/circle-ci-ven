import sys

expected = '2.7.12'
version = '.'.join(str(x) for x in sys.version_info[0:3])

assert version == expected, 'expected python version to be %s, but is actually %s' % (expected, version)
