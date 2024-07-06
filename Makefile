build:
	sudo docker build -t upswing-app .;

run:
	sudo docker run --net host -d -p 10005:8000 --name test-app  upswing-app
remove:
	sudo docker rm -f test-app;

rebuild:
	sudo docker build -t upswing-app .;
	sudo docker rm -f test-app;
	sudo docker run --net host -d -p 10005:8000 --name test-app  upswing-app
