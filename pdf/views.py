from django.shortcuts import render, HttpResponse
from .models import PDF

# Create your views here.
def Index(request):
    pdfs = PDF.objects.all()
    return render(request,'index.html', {'pdfs':pdfs})


def download_file(request, file_id):
    uploaded_file = PDF.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response