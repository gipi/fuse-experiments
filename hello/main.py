import logging
from logging import config as log_config
import sys
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn


log_config.dictConfig({
	'version': 1,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'console':{
			'level':'DEBUG',
			'class':'logging.StreamHandler',
			'formatter': 'simple'
		},
	},
	'loggers': {
		"fuse.log-mixin": {
			"handlers": ["console",],
			"level": "DEBUG",
			"propagate": True,
		},
	}
})

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
