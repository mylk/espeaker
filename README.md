# Espeaker

Espeaker is a way for your colleagues to talk to you using your computer's speech synthesizer.

0. Run Espeaker,
0. Give them your ip and the port number that espeaker listens to,
0. Listen to your music as loud as you wish.
0. If anyone wants to talk to you, points his browser to your ip and port

You are gonna notice him this time! Have fun and continue listening to music!

&nbsp;

Mainly, Espeaker is an application to demonstrate the [Tinywebserver]((https://github.com/mylk/tinywebserver/) python3 module which is
my implementation of a simple web server that serves static content.

In case you want to give it a try, or just want to run this demo application, use the link above to install `tinywebserver`.

&nbsp;

## Installation

You can download the source code using Git:

    git clone https://github.com/mylk/espeaker.git

or you can [get the zip archive](https://github.com/mylk/espeaker/zipball/master "espeaker source code") of the project.
In case you preferred the zip archive, you need to extract it first.

Give Espeaker execute permissions:

    chmod +x espeaker.py

&nbsp;

## Configuration

You can tweak the `config.py` file to meet your needs, for the running port of the service and the web root directory.

&nbsp;

## Run

    ./espeaker.py

&nbsp;

## Dependencies

* espeak

    You need the espeak binary in order to have the speech synthesizer available to your computer.
    Windows users can get it from [espeak.sourceforge.net](http://espeak.sourceforge.net/download.html)
    Linux users can get it using the package manager of their distribution.

* Tinywebserver

    Espeaker depends on the [Tinywebserver]((https://github.com/mylk/tinywebserver/) module which will serve a web page
    that your speaker colleagues are going to use.
    Use the URL above to get it and to read the installation instructions.

* subprocess

    Espeaker also depends on the subprocess module to spawn the espeak command.
