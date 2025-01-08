This is a very simple GUI test used to toggle the LED on/off.

The way this works is not exactly straightforward: the Qt GUI is only able to send serial outputs to the Arduino, which then parses the serial input to determine what the current state of the LED should be.

You will see that there are two folders: one that contains the regular PlatformIO Arduino code, and one that contains the Qt GUI code. You must run the Arduino code first, then run the Qt GUI code, as (again) the Qt GUI is just sending messages to the Arduino through serial.

The QtSerialPort library is necessary, so in addition to downloading the regular developer package, you should also download the QtSerialPort library for this to work.

To understand the different parts of the Qt GUI, you can watch this video: https://www.youtube.com/watch?v=cXojtB8vS2E. I pretty much followed it through to get to where I am now.

For the integration of the Arduino code and the Qt GUI, this video is of great help: https://www.youtube.com/watch?v=IqEO95Gfp6k. I used the code from the video to set up the serial port, and then wrote my own LED on/off functions.
