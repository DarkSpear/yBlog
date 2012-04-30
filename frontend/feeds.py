from frontend.models import Record
from django.contrib.syndication.views import Feed

class LatestEntriesFeed(Feed):
    title = "yBlog title"
    link = "/details/"
    description = "yBlog description"

    def items(self):
        return Record.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.cut

    def item_link(self, item):
        return '?id=' + str(item.id)
