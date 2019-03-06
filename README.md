## A simple site (cmd) monitor written in python (click)

### Functionality
* checks if the website is up and running by checking the status code of the request
* [\OPTIONAL]\ Send Email to the team for analysis

#### Checking for status code
```bash
$ python run.py check-status https://whateverwebsiteyouwant.com True
{'Date': 'Wed, 06 Mar 2019 22:53:14 GMT', 'Server': 'Apache', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Pragma': 'no-cache', 'Set-Cookie': 'PHPSESSID=3dfec8c5aa376c1b69cb36e5b006ce75; path=/', 'Connection': 'close', 'Transfer-Encoding': 'chunked', 'Content-Type': 'text/html; charset=UTF-8'}
```
```bash
$ python run.py check-status https://whateverwebsiteyouwant.com False
Servers are not down Every a-okay!
```
#### Sending an email
```bash
$ python run.py send-mail
Enter Your Email:
Enter Your Password:
Enter Subject:
Enter Body/Content:
Enter The reciever:
Mail Sent successfully
```

