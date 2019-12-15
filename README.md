# OctoPrint setup for Prusa MK3S

Prusa recommends using a Raspberry Pi Zero W to run [OctoPrint](http://octoprint.org/) for your printer. While this is very clean and easy, it is underpowered and you can't get a camera. You also risk the print failing if you are checking its status too often via the UI or app. Here's my setup for attaching a Raspberry Pi 3B+ and camera to a Prusa MK3S printer for a reliable OctoPrint server with a camera. The total cost is about $80.

## Hardware

* Raspberry Pi 3B+
* 16GB microSD Card
* Raspberry Pi Camera v2
* 1 meter ribbon cable for camera

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

## Setup

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
