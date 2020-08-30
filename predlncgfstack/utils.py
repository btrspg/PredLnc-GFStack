import pkg_resources


def get_resource(species='Human'):
    if species not in ['Human', 'Mouse']:
        raise ValueError('species can only be Human or Mouse, not ' + str(species))
    return pkg_resources.resource_filename(__name__, '{species}_model/'.format(species=species))
