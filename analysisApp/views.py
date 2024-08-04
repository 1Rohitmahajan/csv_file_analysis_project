from django.shortcuts import render,HttpResponse
from .forms import UploadFileForm
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# Create your views here.
def index(request):
    upload_success = request.GET.get('upload_success', False)
    return render(request, 'index.html', {'upload_success': upload_success})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def handle_uploaded_file(f):
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    file_path = f'tmp/{f.name}'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def get_plot(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data.select_dtypes(include=['float64', 'int64']), kde=True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            if file_path is None:
                return render(request, 'upload.html', {'form': form, 'error': 'Error saving file.'})
            
            try:
                data = pd.read_csv(file_path)
                plot = get_plot(data)
                context = {
                    'form': form,
                    'data_head': data.head().to_html(classes='table table-striped'),
                    'description': data.describe().to_html(classes='table table-striped'),
                    'missing_values': data.isnull().sum().to_frame().to_html(classes='table table-striped'),
                    'plot': plot,
                }
            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': f'Error processing file: {e}'})
            finally:
                # Clean up the temporary file
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            return render(request, 'result.html', context)
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})

from django.template.loader import render_to_string
import os



def data_analysis_results(request):
    if request.method == 'POST':
        data_head = request.POST.get('data_head')
        description = request.POST.get('description')
        missing_values = request.POST.get('missing_values')
        plot = request.POST.get('plot')
        file_name = request.POST.get('file_name')

        # Generate the HTML content
        html_content = render_to_string('data_analysis_results.html', {
            'data_head': data_head,
            'description': description,
            'missing_values': missing_values,
            'plot': plot,
        })

        # Create the HTTP response for download
        response = HttpResponse(html_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}.html"'
        return response

    return render(request, 'file_name_form.html')
def display_data_analysis(request):
    # Sample data for demonstration
    data_head = '<table><tr><th>Col1</th><th>Col2</th></tr><tr><td>Data1</td><td>Data2</td></tr></table>'
    description = '<table><tr><th>Stat</th><th>Value</th></tr><tr><td>Mean</td><td>10</td></tr></table>'
    missing_values = '<table><tr><th>Col</th><th>Missing</th></tr><tr><td>Col1</td><td>0</td></tr></table>'
    plot = 'iVBORw0KGgoAAAANSUhEUgAAAAUA'  # This is a placeholder for an actual base64 encoded plot image

    context = {
        'data_head': data_head,
        'description': description,
        'missing_values': missing_values,
        'plot': plot,
    }

    return render(request, 'data_analysis_results.html', context)