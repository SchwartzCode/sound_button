# Press a button to play a sound

## Setup Instructions
1. Flash SD card with a raspberry-pi compatible OS (main branch works for debian buster, bullseye branch works for debian bullseye)
    - Newest OS's supported by raspberry pi [are available here](https://www.raspberrypi.com/software/operating-systems/)
2. [Connect your pi to the internet](https://raspberrypihq.com/how-to-connect-your-raspberry-pi-to-wifi/)
3. Connect speaker and ensure it is connected with the command `aplay -l`
    - Note: you can also see all connected sound cards with the command `cat /proc/asound/cards`
4. Verify the speaker works with the command: `speaker-test -c2 -D plughw:n,0` where n is the sound card number
5. Set your speaker to the desired device by creting a file `/etc/asound.conf` and adding these lines (n is the desired sound card number again):
    - defaults.pcm.card n
    - defaults.ctl.card n
6. Verify your default audio output is now your speaker by running `speaker-test c2`
    - Note: if you want to adjust the volume of audio output, use the command `alsamixer` to view a dashboard that allows you to edit output volume
7. Install Git by running the command: `sudo apt-get install git`
8. Run this command to download the code: `git clone https://github.com/SchwartzCode/sound_button.git`
    - This branch works for debian buster. If you are running the debian bullseye OS, you will need to:
        - checkout the bullseye branch of this repo: `git checkout -b bullseye origin/bullseye`
        - install vlc: `sudo apt install vlc`
        
9. Add a folder called "sounds" inside the sound\_button folder you downloaded in step 7 that is filled with the audio clips you want to play
10. Connect a button to the GPIO pins (TODO: more info here)
11. Run the script to verify everything works
12. If you want the script to play automatically, add these two lines to the bottom of the .bashrc file in your raspberry pi's home directory (type `cd ~` to get to home directory)
    - `cd ~/sound_button`
    - `python sound_button_script.py`
    - You will also need to set up auto-login on the pi ([instructions here](https://raspberrypi.stackexchange.com/questions/40415/how-to-enable-auto-login))

## Debugging issues
- If you get a weird Input/Output error when trying to play sounds, you may need to turn the volume down on your audio player (can adjust this with by running `alsamixer` command)
- If you are having trouble installing things, try running the command: `sudo apt-get update` and then: `sudo apt-get upgrade`

## Useful Resources

- [Python GPIO Library for Raspberry Pi](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)

- [Raspberry Pi GPIO Pinout](https://iot4beginners.com/difference-between-bcm-and-board-pin-numbering-in-raspberry-pi/)

- [Changing default output on Rasepberry Pi](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config)
