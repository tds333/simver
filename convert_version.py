import itertools

def to_number(vs):
    if vs in "abc":
        assert len(vs) == 1
        vn = -16 + int(vs, 16)
    else:
        vn = int(vs)
    return vn


def is_release(vstr):
    if "a" in vstr or "b" in vstr or "c" in vstr:
        return False
    return True


def convert_version(vstr):
    vc_list = [to_number(vs) for vs in vstr.split(".", 4)]
    if len(vc_list) > 2 and vc_list[2] < 0: # fill up cal versions
        vc_list.insert(2, 0)
    while len(vc_list) < 5:
        vc_list.append(0)
    return tuple(vc_list)


def main():
    versions = ["1.0.0", "1.1.0", "1.2", "17.0", "1.0.0.c.1", "1.0.c.0", "1.0.a", "1.0.0.b"]
    c_versions = []
    for vstr in versions:
        print(convert_version(vstr), "is release: ", is_release(vstr))
        c_versions.append(convert_version(vstr))
    combi = itertools.permutations(c_versions, 2)
    for a,b in combi:
        print(f"{a} > {b}: ", a>b)

if __name__ == '__main__':
    main()
