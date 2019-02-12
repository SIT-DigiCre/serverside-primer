FROM debian:stretch

EXPOSE 22 80 8800

RUN useradd -m -U -s /bin/bash -G sudo digicre
RUN echo "passwd\npasswd" | passwd digicre

RUN apt update && apt install -y vim emacs sudo curl ssh
RUN apt install -y php python3 python3-pip nodejs golang

RUN pip3 install flask
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
	php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
	php composer-setup.php && \
	php -r "unlink('composer-setup.php');"

COPY . /home/digicre
RUN chown -R digicre:digicre /home/digicre
RUN chown -R digicre:digicre /var/www/html

ENTRYPOINT service ssh start && service apache2 start && su - digicre
