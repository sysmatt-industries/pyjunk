#!/usr/bin/env python3


import os, sys, logging, time, pprint, warnings, argparse, re

PROJECT_PATTERN = '^\w+-\d+$' # ex: AAA-NNNNN 

warnings.filterwarnings('ignore')
ME = sys.argv[0]
loggingFormat='%(asctime)s %(filename)s: %(message)s'
logging.basicConfig(stream=sys.stderr, level=logging.WARNING, format=loggingFormat)
logger = logging.getLogger(ME)
start_time = time.time()

ENV_PROJECT_TREE = "{}_PROJECTS".format($ME)
PROJECT_TREE = os.environ.get(ENV_PROJECT_TREE)

def bomb(chunk):
	logger.error("%s",chunk)
	sys.exit(1)

def majorModeHandler(arg):
    """
    Given the MODEorPROJECT agument, we will determine if we are a per-project or major mode
    Per-project could be a project ID, Filesystem directory (or .) or search criteria.
    """
    # Convert to list if not
    if not isinstance(arg,(list,)): arg = [arg]

    if os.path.isdir(arg[0]):
        logger.debug("Argument [{}] is a directory".format(arg[0]))
    elif isProjectId(arg[0]):
        logger.debug("Argument [{}] is a Project ID".format(arg[0]))
    elif isSearch(arg[0]):
        logger.debug("Argument [{}] is a Search".format(arg[0]))
    else:
        logger.debug("Argument [{}] must be a major mode".format(arg[0]))
        handleMajorMode(arg)

def isProjectId(arg):
    if re.match(PROJECT_PATTERN, arg, re.ASCII): return True
    return False

def isSearch(arg):
    if re.match('^\/', arg, re.ASCII): return True
    return False

def handleMajorMode(arg):
    majParser = argparse.ArgumentParser()
    majParser.add_argument("--list",  help="List all projects, FILTER can be appended", action="store_true")
    majParser.add_argument("--new",   help="Create a new project, project name and options follow", action="store_true")
    majParser.add_argument("--init",  help="Initialize a new {} project tree".format(ME), action="store_true")
    majArgs = majParser.parse_args([ "--{}".format(arg[0])])
    if majArgs.init:
        initTree(arg[1:])
    elif majArgs.list:
        bomb("not implemented")
    elif majArgs.new:
        bomb("not implemented")
    else:
        searchMajorPlugins(arg)

def initTree(arg):
    bomb("not implemented [{}]".format(arg))

def searchMajorPlugins(arg):
    bomb("search not implemented")

if not PROJECT_TREE:
    bomb("PROJECT_TREE is not set, Check environment variable {}".format(ENV_PROJECT_TREE))

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  help="increase output verbosity", action="store_true")
parser.add_argument("-d", "--debug",    help="enable debugging output", action="store_true")
parser.add_argument("MODEorPROJECT",    help="provide a major MODE or PROJECT identifier", default="list", nargs='*')
args = parser.parse_args()


if args.verbose:
    logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


majorModeHandler(args.MODEorPROJECT)
bomb("MODEorPROJECT=[{}]".format(args.MODEorPROJECT))
