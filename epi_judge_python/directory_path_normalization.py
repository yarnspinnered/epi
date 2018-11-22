from test_framework import generic_test


def shortest_equivalent_path(path):
    s = []
    root = False
    if path[0] == "/":
        path = path[1:]
        root = True
    for p in path.split("/"):
        if p == "." or p == "":
            continue
        elif p == ".." and len(s) > 0 and s[-1] != "..":
            s.pop()
        else:
            s.append(p)

    return ("/" if root else "") + "/".join(s)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
