import logging
from django.views import generic
import feedparser

logger = logging.getLogger('development')


class IndexView(generic.TemplateView):

    template_name = 'feed/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = 'https://headlines.yahoo.co.jp/rss/all-c_sci.xml'
        feed = feedparser.parse(url)

        context = {
            'feed_title': feed['feed']['title'],
            'entries': feed['entries'],
        }

        return context
