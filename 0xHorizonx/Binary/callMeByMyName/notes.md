# INFO

Provided : nc 0xhorizon.eu 8888

After connection we can see:

`Hello ! What's your name ?`

After what the cmd need an input. Obviously it appears like a BufferOverflow.
Let's try to input a lot of data:

`Hello ! What's your name qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq`

Response:

`Hello qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq Good job here is your flag: horiz0nx{Segment@t10n_fau1t_1s_c00L_1n_PWN}`

Okey thanks Seg Fault!

(exploit in `script.py`)

# Gotcha !

horiz0nx{Segment@t10n_fau1t_1s_c00L_1n_PWN}