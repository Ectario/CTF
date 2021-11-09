# INFO

We get a GIF file.

I tried to binwalk, strings or exiftool to search through hexadecimal, segment .text or meta-data. Nothing worked. 
So I ungif the gif -> getting each images. Online tools are our friends.

After that, let's scan it...
WOW got it ! Each one is a letter.

Let's code an automation.

# Automate

The script need to:

- Get each frame in good order
- decode the qr code
- append the letter in the result string

# Gotcha !

horiz0nx{qr_c0de_e@$y_t0_dec0de_w1th_scr1pt}
