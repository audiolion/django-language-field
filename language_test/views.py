from django.shortcuts import render
from django.views import View
from .forms import TestForm


class TestView(View):
    def get(self, request):
        form = TestForm()
        return render(request, 'language_test/test.html', {'form': form})