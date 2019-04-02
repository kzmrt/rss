import logging
from django.views import generic

logger = logging.getLogger('development')


class IndexView(generic.ListView):

    paginate_by = 5
    template_name = 'feed/index.html'
    # model = Post