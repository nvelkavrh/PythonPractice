# -*- coding: utf-8 -*-
''' 
Fun with httplib; read HTTP headers for interesting info
'''

import httplib
conn = httplib.HTTPConnection('docs.python.org')
conn.request('HEAD', '/2/library/httplib.html')
resp = conn.getresponse()

# Does the document exist? What's the HTTP response code?
status = resp.status
print status

# Display intersting info through the page's HTTP headers:
for h in resp.getheaders():
	print h



