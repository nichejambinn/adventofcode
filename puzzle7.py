import sys

TOTAL_DISK_SPACE = 70000000
UPDATE_SIZE = 30000000

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0
        self.files = []
        self.dirs = []

    def __str__(self):
        s = "\t" * self.depth + self.name + "\n"
        for file in self.files:
            s += "\t" * self.depth + "- " + str(file) + "\n"
        for dir in self.dirs:
            s += "\t" * self.depth + str(dir)
        return s

    def mkdir(self, dir_name):
        dir = Dir(dir_name, self)
        self.dirs.append(dir)

    def cd(self, dir_name):
        if dir_name == '..':
            return self.parent

        return next(filter(lambda dir: dir.name==dir_name, self.dirs))

    def touch(self, file):
        self.files.append(file)

    def getSize(self):
        size = sum([file.size for file in self.files])
        size += sum([dir.getSize() for dir in self.dirs])
        return size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size})"


def read_filesystem(filename):
    root = Dir('/', None)
    cwd = root

    # read input
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            cmd = line.split()
            # execute command

            if cmd[1] == 'cd':
                # change current working directory
                if cmd[2] == '/':
                    cwd = root
                else:
                    cwd = cwd.cd(cmd[2])

            elif cmd[1] == 'ls':
                # list items
                line = file.readline().strip()

                while line and line[0] != '$':
                    item = line.split()

                    if item[0] == 'dir':
                        # make directory
                        cwd.mkdir(item[1])

                    else:
                        # create file
                        newfile = File(item[1], int(item[0]))
                        cwd.touch(newfile)
                   
                    line = file.readline().strip()

                continue

            line = file.readline().strip()

    return root


def total_dir_size_below_limit(cwd, limit=100000):
    total = 0

    cwd_size = cwd.getSize()
    if cwd_size <= limit:
        total += cwd_size

    for dir in cwd.dirs:
        total += total_dir_size_below_limit(dir)

    return total


def smallest_dir_to_delete(cwd, space_needed):
    min_dir = sys.maxsize
    cwd_size = cwd.getSize()

    if cwd_size >= space_needed:
        min_dir = min(cwd_size, min_dir)

    for dir in cwd.dirs:
        min_dir = min(min_dir, smallest_dir_to_delete(dir, space_needed))

    return min_dir



if __name__=='__main__':
    root = read_filesystem('puzzle7')
    
    print(total_dir_size_below_limit(root)) # part 1

    unused_space = TOTAL_DISK_SPACE - root.getSize()
    space_needed = UPDATE_SIZE - unused_space
    print(smallest_dir_to_delete(root, space_needed)) # part 2

