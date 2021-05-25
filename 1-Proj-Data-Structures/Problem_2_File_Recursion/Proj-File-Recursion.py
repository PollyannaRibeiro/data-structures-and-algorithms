import os


def find_files(suffix, path):
    output = []

    if len(path) == 0:
        print("error: the path is empty")
        return None

    if not os.path.isdir(path):
        print("error: invalid path")
        return None

    if os.path.isdir(path):
        list = os.listdir(path)

        for item in list:
            current_path = os.path.join(path, item)

            if os.path.isfile(current_path):
                if current_path.endswith(suffix):
                    output.append(current_path)
            elif os.path.isdir(current_path):
                output += find_files(suffix, current_path)

    return output

# test

print("Pass" if (find_files(".c", "./testdir") == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']) else "Fail")
print("Pass" if (find_files(".h", "./testdir") == ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']) else "Fail")
print("Pass" if (find_files(".w", "./testdir") == []) else "Fail")
print("Pass" if (find_files(".c", "./test") == None) else "Fail")
print("Pass" if (find_files(".c", "") == None) else "Fail")




