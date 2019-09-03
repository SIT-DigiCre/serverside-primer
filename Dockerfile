FROM debian:stretch

EXPOSE 22 80 8800

RUN useradd -m -U -s /bin/bash -G sudo digicre
RUN echo "passwd\npasswd" | passwd digicre

RUN apt update && apt install -y vim emacs sudo curl ssh

# for Node.js v12.x
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -

RUN apt install -y php python3 python3-pip nodejs golang

# Python setup
RUN pip3 install flask

# PHP setup
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
	php composer-setup.php && \
	php -r "unlink('composer-setup.php');"

COPY . /home/digicre
RUN chown -R digicre:digicre /home/digicre
RUN chown -R digicre:digicre /var/www/html

# Node.js setup
RUN sudo -u digicre /bin/bash -c "cd ~/nodejs && npm install"

ENTRYPOINT service ssh start && service apache2 start && su - digicre
