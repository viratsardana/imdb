import logging
import optparse
import urllib2
import simplejson
import gettext
from gettext import gettext as _
gettext.textdomain('imdb')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from imdb import imdbconfig

class ImdbLens(SingleScopeLens):

    class Meta:
        name = 'imdb'
        description = 'Imdb Lens'
        search_hint = 'Search Imdb'
        icon = 'imdb.svg'
        search_on_blank=True

    # TODO: Add your categories
    imdb_category = ListViewCategory("MOVIES", "dialog-symbolic-information")
    def imdb_query(self,search):
     try:
        search = search.replace(" ", "+")
        url = ("http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=%s" % (search))
        results = simplejson.loads(urllib2.urlopen(url).read())
        print "Searching Imdb"
        return results
     except (IOError, KeyError, urllib2.URLError, urllib2.HTTPError, simplejson.JSONDecodeError):
        print "Error : Unable to search imdb"
        return []
        
    def search(self, search, results):   
          d={}
          d=self.imdb_query(search)
          s="title_popular"
          l="title_exact"
          for i in range (0,5):
           		results.append("http://www.imdb.com/title/%s/?ref_=nv_sr_1" % (d[s][i]["id"]),
                    "http://upload.wikimedia.org/wikipedia/commons/3/35/IMDb_logo.svg",
                    self.imdb_category,
                    "text/html",
                    d[s][i]["title"],
                    "IMDB Movie",
                    "http://www.imdb.com/title/%s/?ref_=nv_sr_1" % (d[s][i]["id"]))
          pass 

