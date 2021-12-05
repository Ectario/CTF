# INFO

Provided: `nc 0xhorizon.eu 6789`

        54x-3y+63z-27a-17b-64c = 3960
        29x-100y+20z+47a+33b+2c = -1954
        16x-48y-46z+25a+64b-10c = -3571
        45x-58y-64z+15a+91b+54c = -3094
        98x-65y-23z+80a+21b+48c = 1903
        61x+11y-8z-92a-12b-69c = -2847

        Example: {"a":12, "b":23, "c":76, "x":56, "y":90, "z":90}
        Return in json format solutions: 
        Error in format

After many manual trials we can see that all the time we get 6 equations and 6 variables 'a' 'b' 'c' 'x' 'y' 'z'

So we need to create a script which is a linear-system solver for 6 equations with 6 variable:
- auto-connect to the server
- parse the input
- do the calculus
- send the result after rounding

Let's code! (`script.py`).

# Gotcha!

horiz0nx{S0_Str0ng_M4ths}
