import sys

import pkg_resources


def get_resource(species='Human'):
    if species not in ['Human', 'Mouse']:
        raise ValueError('species can only be Human or Mouse, not ' + str(species))
    return pkg_resources.resource_filename(__name__, '{species}_model/'.format(species=species))


def get_txcdspredict():
    return pkg_resources.resource_filename(__name__, 'bin/txCdsPredict')


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
