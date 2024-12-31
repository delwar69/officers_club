from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # Install using `pip install xhtml2pdf`

def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            # Save data to the database
            member = form.save()
            
            # Generate PDF
            template = get_template('members/member_pdf.html')  # Path to the PDF template
            context = {'member': member}
            html = template.render(context)
            
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="member_{member.id}.pdf"'
            
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF')
            
            return response  # Return the PDF to the browser for download
            
    else:
        form = MemberForm()
    return render(request, 'members/register.html', {'form': form})
