#!/usr/bin/env python3


import os, sys, logging, time, pprint, warnings, argparse

warnings.filterwarnings('ignore')
ME = sys.argv[0]
loggingFormat='%(asctime)s %(filename)s: %(message)s'
logging.basicConfig(stream=sys.stderr, level=logging.WARNING, format=loggingFormat)
logger = logging.getLogger(ME)
start_time = time.time()

def bomb(chunk):
	logger.error("%s",chunk)
	sys.exit(1)


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  help="increase output verbosity", action="store_true")
parser.add_argument("-d", "--debug",    help="enable debugging output", action="store_true")
parser.add_argument("MODEorPROJECT",    help="provide a major MODE or PROJECT identifier", default="list", nargs='*')
args = parser.parse_args()


if args.verbose:
    logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)

bomb("MODEorPROJECT=[{}]".format(args.MODEorPROJECT))
