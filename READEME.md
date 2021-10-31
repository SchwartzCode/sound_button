# Sound Button

## Setup Instructions
1. Flash SD card with a raspberry-pi compatible OS (raspbian-lite is what I used)
2. Connect speaker and ensure it is connected with the command `aplay -l`
    - Note: you can also see all connected sound cards with the command `cat /proc/asound/cards`
3. Verify the speaker works with the command: `speaker-test -c2 -D plughw:n,0` where n is the sound card number
4. Set your speaker to the desired device by creting a file `/etc/asound.conf` and adding these lines (n is the desired sound card number again):
    - defaults.pcm.card n
    - defaults.ctl.card n
5. Verify your default audio output is now your speaker by running `speaker-test c2`
    - Note: if you want to adjust the volume of audio output, use the command `alsamixer` to view a dashboard that allows you to edit output volume
6. Connect your pi to the internet (TODO: add reference for this)
7. Clone this repository (TODO: add link)
8. Add a folder called "sounds" inside the sound_button folder you downloaded in step 7 that is filled with the audio clips you want to play
9. Connect a button to the GPIO pins (TODO: more info here)
10. Run the script to verify everything works
11. If you want the script to play automatically, add these two lines to the bottom of the .bashrc file in your raspberry pi's home directory (type `cd ~` to get to home directory)
    - `cd ~/sound_button` TODO: replace - with underscore
    - `python sound_button_script.py`
