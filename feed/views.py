import logging
from django.views import generic

logger = logging.getLogger('development')


class IndexView(generic.TemplateView):

    template_name = 'feed/index.html'
