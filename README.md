Simple Django Application that performs api requests and stores in db

Requirements :- 

sqlite3
django
python3
(refer requirements.txt for more)

Steps to recreate the steps I did to install:-

Navigate to folder containing my_blog,
>>python3 -m venv venv
>>source venv/bin/activate

Navigate into my_blog,
>>pip install --upgrade pip
>>pip install -r requirements.txt
>>python manage.py makemigrations
>>python manage.py migrate
>>python manage.py runserver 
to check if it's working
quit the server now

>>chmod +x start.sh
>>sudo apt-get install build-essential curl file git
>>sudo apt install linuxbrew-wrapper
(
if it didnn't work, do this :- 
>>sudo apt-get install build-essential curl git m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev
)
>>brew update && brew upgrade --all && brew cleanup && brew prune
>>brew install docker-machine
>>sudo apt-get install build-essential


Add Linuxbrew to your ~/.bash_profile by running
    echo 'export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"' >>~/.bash_profile
    echo 'export MANPATH="/home/linuxbrew/.linuxbrew/share/man:$MANPATH"' >>~/.bash_profile
    echo 'export INFOPATH="/home/linuxbrew/.linuxbrew/share/info:$INFOPATH"' >>~/.bash_profile
- Add Linuxbrew to your PATH
    PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
- We recommend that you install GCC by running:
    brew install gcc
- Run `brew help` to get started
- Further documentation: 
    http://docs.brew.sh


>>sudo apt-get install virtualbox
>>docker-machine create development --driver virtualbox --virtualbox-disk-size "5000" --virtualbox-cpu-count 2 --virtualbox-memory "4096"
>>docker-machine env development
 	op:- 	export DOCKER_TLS_VERIFY="1"
		export DOCKER_HOST="tcp://192.168.99.100:2376"
		export DOCKER_CERT_PATH="/home/rego/.docker/machine/machines/development"
		export DOCKER_MACHINE_NAME="development"
		# Run this command to configure your shell: 
		# eval $(docker-machine env development)

>>eval $(docker-machine env development)

To see if everything works :-
>> sudo docker images
       op:-	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE

You can now dockerize your Python application and get it running using the docker-machine
Now create Dockerfile,
>>sudo docker build -t rego/dockerizing_my_blog .

>>sudo docker run -it -p 8000:8000 rego/dockerizing_my_blog:latest



Navigate to :-

localhost:8000  -> users page
localhost:8000/comments  -> comments page

Output :- 
(venv) rego@rglappy:~/Desktop/rego/Personal/Django/Project/Blog/my_blog$ sudo docker run -it -p 8000:8000 rego/dockerizing_my_blog:latest
Starting Gunicorn.
[2019-10-21 03:44:24 +0000] [1] [INFO] Starting gunicorn 19.9.0
[2019-10-21 03:44:24 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2019-10-21 03:44:24 +0000] [1] [INFO] Using worker: sync
[2019-10-21 03:44:24 +0000] [11] [INFO] Booting worker with pid: 11
[2019-10-21 03:44:24 +0000] [12] [INFO] Booting worker with pid: 12
[2019-10-21 03:44:24 +0000] [14] [INFO] Booting worker with pid: 14
Data is already in the DB cannot add duplicate username and email they are UNIQUE!
Data is already in the DB cannot add duplicate username and email they are UNIQUE!

