import itertools


def is_release(version_tuple):
    if isinstance(version_tuple, str):
        version_tuple = convert_version(version_tuple)
    return all(version_tuple)


def convert_version(vstr):
    vc_list = [int(vs) for vs in vstr.split(".")]
    assert len(vc_list) >= 2 and len(vc_list) <= 5
    return tuple(vc_list)


def main():
    versions = ["1.0.0", "1.1.0", "1.2", "1.2.1", "1.2.0.2", "17.0", "17.1", "1.0.0.0.1", "1.0.0.1", "1.0.0.0", "1.0.0.0.0", "1.0.0.0.1"]
    c_versions = []
    for vstr in versions:
        print(convert_version(vstr), "is release: ", is_release(vstr))
        c_versions.append(convert_version(vstr))
    combi = itertools.permutations(c_versions, 2)
    for a,b in combi:
        print(f"{a} > {b}: ", a>b)

if __name__ == '__main__':
    main()
