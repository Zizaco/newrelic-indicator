.PHONY: clean
prepare:
	apt-get update -qq
	apt-get install git libgtk2.0-dev libglib2.0-dev
	apt-get install python-appindicator

install:
	./register-startup.sh
	./newrelic-indicator.sh
