from fpq_core.views import FormView
from .forms import CreationForm


class CreationView(FormView):
    template_name = 'fpq_author/create.html'
    form_class = CreationForm

    def _guest(self) -> bool:
        return True
