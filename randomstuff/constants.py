def _warn(client, warning):
	if client.suppress_warnings == True:
		return
	else:
		print("[WARNING] "+"\n"+warning)

BASE_URL = 'https://api.pgamerx.com'
IMAGE_TYPES = ['aww', 'duck', 
	'dog', 'cat', 
	'memes', 'dankmemes', 
	'holup', 'art', 
	'harrypottermemes','facepalm']
JOKE_TYPES = ['any', 'dev', 'spooky', 'pun']
PLANS = ['', 'pro', 'ultra', 'biz', 'mega']
VERSIONS = ['2', '3', '4']
SERVERS = ['primary', 'backup', 'unstable']