from plfs_lout.parse_lout import parse
from plfs_lout.save import save
import sys
import pathlib

def main():
    louts = parse(sys.argv[1])
    lout = match_name(louts,sys.argv[2])
    if lout is None:
        print("Could not find matching layout",file=sys.stderr)
        sys.exit(1)
    save(lout[1],sys.argv[2],sys.argv[3])

def match_name(louts,fname):
    p = pathlib.Path(fname)
    name = p.stem.lower()
    for l in louts:
        if l[0]==name:
            return l
    return None

if __name__=="__main__":
    main()
