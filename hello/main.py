import logging
import sys
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn

class Hello(LoggingMixIn, Operations):
	pass

if __name__ == "__main__":
	#print >> sys.stderr, fuse.APIVersion()

	logging.getLogger().setLevel(logging.DEBUG)

	if len(sys.argv) < 2:
		print >> sys.stderr, "usage: %s <mountpoint>" % sys.argv[0]
		sys.exit(1)

	mountpoint = sys.argv[1]

	FUSE(Hello(), mountpoint, foreground=True)
