import logging
from django.views import generic
from feed.models import Rss

logger = logging.getLogger('development')


class IndexView(generic.ListView):

    paginate_by = 5
    template_name = 'feed/index.html'
    model = Rss