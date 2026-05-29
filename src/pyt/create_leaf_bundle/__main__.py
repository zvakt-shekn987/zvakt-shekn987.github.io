import sys

from . import utils

def main():

    args = sys.argv[1:]
    post_name, timeformat1, timeformat2, *_ = (args + [None, None, None, None])[:3]
    utils.create_leaf(post_name, timeformat1, timeformat2)

if __name__ == "__main__":
    main()
