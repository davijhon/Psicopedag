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
	Suscriptor
)
from .forms import ContactoForm


def sending_email(nombre, correo, asunto, mensaje):
	# This function send a email to a customer
	# with the info about the plan changed or buyed

	subject = asunto
	html_message = render_to_string('email/contact_email.html', {'subject': subject, 
																	'name': nombre,
																	'email': correo,
																	'message': mensaje, })
	plain_message = strip_tags(html_message)
	from_email = correo
	to = settings.DEFAULT_FROM_EMAIL

	send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def error_400(request, exception):
        data = {}
        return render(request,'pages/error_pages/400.html', data)

def error_403(request,  exception):
        data = {}
        return render(request,'pages/error_pages/403.html', data)

def error_404(request,  exception):
        data = {}
        return render(request,'pages/error_pages/404.html', data)

def error_500(request,  exception):
        data = {}
        return render(request,'pages/error_pages/500.html', data)


class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = ContactoForm()
		# contact = Web.objects.filter(estado=True).latest('fecha_creacion')
		headers = list(Header.objects.filter(status=True).order_by('position')[:3])

		ctx = {
			'carousel_image1': headers[0],
			'carousel_image2': headers[1],
			'carousel_image3': headers[2],
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

				contact = Contacto(
					nombre=nombre,
					correo=correo,
					asunto=asunto,
					mensaje=mensaje,
				)
				contact.save()
				sending_email(nombre, correo, asunto, mensaje)
			messages.success(self.request, "Tu mensaje fue enviado exitosamente!")
			return redirect("/")
		except ObjectDoesNotExist:
			messages.error(self.request, "Lo sentimos. Algo ha ocurrido al momento de enviar el mensaje. Intenta nuevamente")
			return redirect("pages:index")

