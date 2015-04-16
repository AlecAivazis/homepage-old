# django imports
from django.contrib.sitemaps import Sitemap
from .models import Post

# define the blog sitemap
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5


    def items(self):
        """ the various blog posts """
        return Post.objects.visible()

    def lastmod(self, obj):
        """ the last time the post was modified """
        return obj.post_date
