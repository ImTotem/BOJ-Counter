# TODO Find not committed Number of Solved Problems

import os

def search(root: str) -> set:
    ret = set()
    for (path, _, files) in os.walk(root):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py' and __file__.split("/")[-1] != filename:
                ret.add(int(path.split("/")[-1].split(".")[0]))
    
    return ret

if __name__ == "__main__":
    committed: set = search(input("path input > "))
    solved: set = set(map(int, open(os.getcwd()+"/solved.txt", "r").readline().split()))

    print("solved:", len(solved))
    print("committed:", len(committed))
    print()

    not_committed = sorted(solved - committed)
    print("not committed:", len(not_committed))
    print()
    
    with open("not committed.md", 'w') as f:
        for i in range(len(not_committed)):
            f.write(f"{i}. - [ ] https://www.acmicpc.net/problem/{not_committed[i]}\n")