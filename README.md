# Scraping

 
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:jonathonf/python-3.6    
    sudo apt-get update -y
    sudo apt-get install python3.6 libpython3.6
    sudo apt-get install python-virtualenv python3.6-venv
    
    virtualenv --python=python3.6 venv
    source venv/bin/activate
      
instalar phantomjs:

    curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
    sudo apt install nodejs
	sudo npm i -g install phantomjs-prebuilt --unsafe-perm

corre mas rapido sin hacer el test unitario y sin Firefox, sera un lio ir tomando las fotos y guiandolo remotamente XD

para guardar en python `folder/nombre.png`

usar `driver.quit()` para evitar tener el navegador abierto en memoria

correr el server en segundo plano:
    
    nohup python -m http.server 7000 > my.log 2>&1 &
    ps -ef |grep python
    kill -9 <PI>

descargar geckodriver actualizado para usarlo en ubuntu, descargar y descomprimir:

    chmod +x geckodriver
    export PATH=$PATH:/path.../geckodriver y agregarlo como variable al driver
    o guardarlo en /usr/bin/

usar polyglot

    export PATH=$PATH:/home/okadath/Desktop/python/bot_local/geckodriver


instalar chromewebdriver:
sudo apt-get install chromium-chromedriver

en raspberry hay errores hay que instalar rust para selenoum y todo el dev de python



https://tekshinobi.com/django-celery-rabbitmq-redis-broker-results-backend/

las plantillas en flask siempre deben ir en /templates


sudo apt install python3-pip python3-dev libpq-dev  nginx curl libcairo2-dev libsdl-pango-dev python3-certbot-nginx

sudo -H pip3 install virtualenv
virtualenv venv
source venv/bin/activate


pipenv lock -r > requirements.txt
pip install -r requirements.txt
pip install  gunicorn


 
sudo cp gunicorn.service /etc/systemd/system/
sudo systemctl enable gunicorn.service
sudo systemctl start gunicorn.service
sudo systemctl daemon-reload
 