# OctoPrint setup for Prusa MK3S

Prusa recommends using a Raspberry Pi Zero W to run [OctoPrint](http://octoprint.org/) for your printer. While this is very clean and easy, it is underpowered and you can't get a camera. You also risk the print failing if you are checking its status too often via the UI or app. Here's my setup for attaching a Raspberry Pi 3B+, camera, and lights to a Prusa MK3S printer for a reliable OctoPrint server with a camera. The total cost is about $100.

## Hardware

* Raspberry Pi 3B+
* 16GB microSD Card
* Raspberry Pi Camera v2
* 1 meter ribbon cable for camera
* WS2812 LED light strip

## Prints

### Raspberry Pi Mount - Bottom

https://www.thingiverse.com/thing:2843889

Resolution: 0.15

Infill: 20% (optional)

### Raspberry Pi Mount - Lid

http://www.thingiverse.com/thing:559858

Resolution: 0.1

Infill: 20%

### Camera Mount - Arm, Camera, Lid, Post

https://www.prusaprinters.org/prints/7064-customizable-raspberry-pi-camera-bed-mount-prusa-m/

Customizable via included OpenSCAD, but the gcode files committed here should work great with an MK3S. This mount does require using a couple of the spare M4 screws included with your Prusa.

Material: PLA should be safe, but PETG is better given its proximity to heat bed

Resolution: 0.2

Infill: 20%

### Ribbon clips

http://www.thingiverse.com/thing:3189351

**Print 4 of these!**

Resolution: 0.2

Infill: 10%

## Octoprint

1. Flash Raspberry Pi SD card with [OctoPi](https://github.com/guysoft/OctoPi) image
2. Set wifi password in `octopi-wpa-supplicant.txt`
3. Boot up raspberry pi and `ssh pi@octopi.local`
4. `passwd` to change root password
5. Edit `/etc/hostname` to give this octopi a unique name
6. Visit `http://octopi.local` in browser
6. Configure [Prusa MK3S printer profile](https://github.com/prusa3d/OctoPi/blob/devel/src/modules/octopi/filesystem/home/pi/.octoprint/printerProfiles/_default.profile)
7. Install octoslack and octopod plugins
8. Restart Raspberry Pi
9. Configure plugins as needed
10. Happy printing!

## Lighting

This repo also includes a script that can control a WS2812 LED light strip attached to the raspberry pi. It will dynamically change lights based on the status of the printer. I use [these ones](https://www.amazon.com/gp/product/B00JYPJAL2/) but Adafruit's NeoPixels will work well too.

1. Connect lights to raspberry pi

Trim led strip to 15 pixels so that they fit on the top frame of the MK3S. Solder 3 wires (65cm length each) to connect led strip to 5V, GND, and GPIO pin 18. I also use a [Texas Instruments SN74AHCT125N buffer](https://www.digikey.com/product-detail/en/texas-instruments/SN74AHCT125N/296-4655-5-ND/375798) to ensure correct logic voltage, but this is optional. My Raspberry Pi 3B+ was able to drive the LED strip with 3.3v logic.

Mount the led strip to the bottom of the frame with double sided tape and use 4 zip ties to hold in place, since the heat from the lights + extruder will weaken the tape very quickly.

2. Clone this repo

```bash
git clone https://github.com/neilgupta/prusa-octoprint-setup.git
cd prusa-octoprint-setup
```

3. Install dependencies

```bash
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install -r requirements.txt
```

4. Install [MQTT plugin](https://github.com/OctoPrint/OctoPrint-MQTT) in Octoprint, configure it to talk to `hiome.local`. This assumes you have [Hiome](https://hiome.com)... if not, get on that first! Set the topic format to `_hiome/1/sensor/CLIENT_NAME/` where `CLIENT_NAME` is "prusa_" + octopi's hostname (ie "prusa_octopi")

5. Install led systemd service

```bash
sudo cp octoprint-led.service /etc/systemd/system/octoprint-led.service
sudo systemctl enable octoprint-led.service
sudo systemctl start octoprint-led.service
```

To run the script as a one-off, it's `sudo python3 led.py`

6. Start a print from octoprint!

<div align="center">
  <a href="https://raw.githubusercontent.com/neilgupta/prusa-octoprint-setup/master/prusa.jpeg">
    <img width="756px" height="1008px" src="https://raw.githubusercontent.com/neilgupta/prusa-octoprint-setup/master/prusa.jpeg" alt="My Prusa MK3S" />
  </a>
</div>
