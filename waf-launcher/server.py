from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor

resource = File('/home/albatros/Projects/waf-launcher/waf-launcher/bin/Debug')
factory = Site(resource)
reactor.listenTCP(9998, factory)
reactor.run()
