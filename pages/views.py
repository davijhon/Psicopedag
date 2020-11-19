import os
import json
import requests
from django.http import HttpResponse, Http404
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic import TemplateView, ListView, View

from .models import ( 
    Header, 
    Contacto,
	Toolbox,
	SectionContent,
)
from .forms import ContactoForm

GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY
GOOGLE_RECAPTCHA_SECRET_KEY = settings.GOOGLE_RECAPTCHA_SECRET_KEY

def sending_email(nombre, correo, asunto, mensaje):
	# This function send a email to a customer
	# with the info about the plan changed or buyed

	subject = asunto
	html_message = render_to_string('email/contact_email.html', {'subject': subject, 
																  'name': nombre,
															      'email': correo,
															      'message': mensaje, })
	plain_message = strip_tags(html_message)
	from_email = settings.DEFAULT_FROM_EMAIL
	to = settings.DEFAULT_FROM_EMAIL

	send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def download_free_pdf(request, slug):
	# This function download the document in media static file.
	pdf = Toolbox.objects.get(slug=slug)
	pdf_path = pdf.file.path
	file_path = os.path.join(settings.MEDIA_ROOT, pdf_path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/pdf")
			response['Content-Length'] = os.path.getsize(file_path)
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404


def error_400(request):
        data = {}
        return render(request,'pages/error_pages/400.html', data)

def error_403(request):
        data = {}
        return render(request,'pages/error_pages/403.html', data)

def error_404(request):
        data = {}
        return render(request,'pages/error_pages/404.html', data)

def error_500(request):
        data = {}
        return render(request,'pages/error_pages/500.html', data)


class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = ContactoForm()
		file1 = Toolbox.objects.order_by('created')[0]
		file2 = Toolbox.objects.order_by('created')[1]
		# headers = list(Header.objects.filter(status=True).order_by('position')[:3])
		conoceme = SectionContent.objects.get(seccion__nombre='Conoceme')
		apoyo = SectionContent.objects.get(seccion__nombre='Apoyo')
		evaluacion = SectionContent.objects.get(seccion__nombre='Evaluacion')
		terapias = SectionContent.objects.get(seccion__nombre='Terapias')
		motivacionales = SectionContent.objects.get(seccion__nombre='Motivacionales')
		pedagogico_didactico = SectionContent.objects.get(seccion__nombre='Pedagógico-didácticos')
		especializados = SectionContent.objects.get(seccion__nombre='Especializados')
		modalidad_presencial = SectionContent.objects.get(seccion__nombre='Modalidad Presencial')
		e_learning = SectionContent.objects.get(seccion__nombre='E-learning')


		ctx = {
			# 'carousel_image1': headers[0],
			# 'carousel_image2': headers[1],
			# 'carousel_image3': headers[2],
			'conoceme': conoceme,
			'apoyo': apoyo,
			'evaluacion': evaluacion,
			'terapias': terapias,
			'motivacionales': motivacionales,
			'pedagogico_didactico': pedagogico_didactico,
			'especializados': especializados,
			'modalidad_presencial': modalidad_presencial,
			'e_learning': e_learning,
			'file1': file1,
			'file2': file2,
			'google_recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY,
			'form': form
		}
		return render(request, 'pages/index.html', ctx)
	
	def post(self, request, *args, **kwargs):
		form = ContactoForm(self.request.POST or None)

		try:
			if form.is_valid():
				nombre = form.cleaned_data.get('nombre')
				correo = form.cleaned_data.get('correo')
				asunto = form.cleaned_data.get('asunto')
				mensaje = form.cleaned_data.get('mensaje')

				''' Begin reCAPTCHA validation '''
				recaptcha_token = request.POST.get('g-recaptcha-response')
				url = 'https://www.google.com/recaptcha/api/siteverify'
				values = {
					'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
					'response': recaptcha_token
				}
				cap_server_response = requests.post(url=url, data=values)
				cap_json = json.loads(cap_server_response.text)
				if cap_json['success'] == False:
					messages.error(request, 'Invalid reCAPTCHA. Please try again.')
					return redirect("pages:index")
				''' End reCAPTCHA validation '''

				contact = Contacto(
					nombre=nombre,
					correo=correo,
					asunto=asunto,
					mensaje=mensaje,
				)
				contact.save()
				sending_email(nombre, correo, asunto, mensaje)
			messages.success(self.request, "Tu mensaje fue enviado exitosamente!")
			return redirect("pages:index")
		except ObjectDoesNotExist:
			messages.error(self.request, "Lo sentimos. Algo ha ocurrido al momento de enviar el mensaje. Intenta nuevamente")
			return redirect("pages:index")

