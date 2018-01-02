import itertools
    
LETTER_DICT = {"dev": -4, "a": -3, "b": -2, "rc": -1}

def to_number(vs):
    if vs in LETTER_DICT:
        return LETTER_DICT[vs]
    return int(vs)


def is_release(vstr):
    vc_list = vstr.split(".", 4)
    if len(vc_list) > 3:
        return False
    return True


def convert_version(vstr):
    vc_list = [to_number(vs) for vs in vstr.split(".")]
    assert len(vc_list) >= 2 and len(vc_list) <= 5
    if len(vc_list) == 4: # fill up cal versions
        assert vc_list[2] < 0
        vc_list.insert(2, 0)
    while len(vc_list) < 5:
        vc_list.append(0)
    return tuple(vc_list)


def main():
    versions = ["1.0.0", "1.1.0", "1.2", "1.2.dev.2", "17.0", "1.0.0.rc.1", "1.0.rc.0", "1.0.a.0", "1.0.0.b.0", "1.0.0.dev.1"]
    c_versions = []
    for vstr in versions:
        print(convert_version(vstr), "is release: ", is_release(vstr))
        c_versions.append(convert_version(vstr))
    combi = itertools.permutations(c_versions, 2)
    for a,b in combi:
        print(f"{a} > {b}: ", a>b)

if __name__ == '__main__':
    main()
