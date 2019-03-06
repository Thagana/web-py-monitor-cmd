import click
import requests
from .send_email import mail_send

@click.group()
def main():
	pass

@main.command()
@click.option('--email', prompt='Enter Your Email')
@click.option('--password', prompt='Enter Your Password',hide_input=True)
@click.option('--subject', prompt='Enter Subject')
@click.option('--body', prompt='Enter Body/Content')
@click.option('--reciever', prompt='Enter The reciever')


def send_mail(email, password, subject, body, reciever):
	""" Send and Email to the team """
	try:
		mail_send(email, password, subject, body, reciever)
		click.echo('Mail Sent successfully')
	except Exception as e:
		click.echo('Failed to send mail: ' + str(e))


@main.command()
@click.argument('url')
@click.argument('verbose', default=False)
def check_status(url, verbose):
	""" Get Server status """
	try:
		r = requests.get(url)
		if verbose == 'False' and r.status_code == 200:
			click.echo("Servers are not down Every a-okay! ")
		elif verbose == 'True' and r.status_code == 200:
			click.echo(r.headers)
		else:
			click.echo("Seems like servers are down... send email?")
	except Exception as e:
		click.echo('ERROR: '+ str(e) + '')

