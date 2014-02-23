import logging
from logging import config as log_config
import sys
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
import os
import stat


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
	def readdir(self, path, fh):
		return super(Hello, self).readdir(path, fh) + ['world', ]

	def getattr(self, path, fh=None):
		try:
			return super(Hello, self).getattr(path, fh)
		except:
			return {
				"st_atime": 0L,
				"st_ctime": 0L,
				"st_gid": 0,
				"st_mode": stat.S_IFREG | 0755,
				"st_mtime": 0L,
				"st_nlink": 1,
				"st_size": 0,
				"st_uid": 0,
			}

if __name__ == "__main__":
	#print >> sys.stderr, fuse.APIVersion()

	logging.getLogger().setLevel(logging.DEBUG)

	if len(sys.argv) < 2:
		print >> sys.stderr, "usage: %s <mountpoint>" % sys.argv[0]
		sys.exit(1)

	mountpoint = sys.argv[1]

	FUSE(Hello(), mountpoint, foreground=True)
