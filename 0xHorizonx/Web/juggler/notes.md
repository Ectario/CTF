# INFO

We arrive on a site. This site offers us to see if there is a backdoor and gives us the following code:

        <?php
            if(isset($_POST["password"])){
                if(md5($_POST["password"]) == "0e791913724986920161109490945425"){
                    echo "<p>Well played here is your flag: $FLAG</p>";
                }
                else{
                    echo "<p>Sorry authentication failed...</p>";
                }
            }
        ?>

Quickly we understand that we want the condition "if (md5 ($ _ POST [" password "]) ==" 0e791913724986920161109490945425 ")" to be valid.

We see that the condition is likely to be broken by a `type juggling` flaw

Let's try it. (see First Idea)

It wasn't the right way.

After having had advice and some research on the internet. The new idea would be to use the specifity looking at that the hash is '0e' followed only by numbers and only by numbers. 

Let's try it. (see Second Idea)

That was the good one!

# First Idea (Type Juggling)

## Concept

In php with a simple comparison, we have "0e5678" == 0, the string is interpreted as an integer and calculated. In our case, 0 ^ 5678 = 0 so the comparison is true.

We can abuse this feature to get around the condition, for that we need to find a string such that its hash md5 is of the form ^ 0e [0-9] * $.

## Problem

After trying a bruteforce to find in rockyou a string with the good hash, we got one [in `output.txt`]. **Problem : to perform the Type Juggling we needed to have an implicit cast (which is not present here).**

# Second Idea

## Concept

From the following link: https://github.com/spaze/hashes

We deduce it is a collision. Let's automate to find what is the collision for our hash by retrieving the list from the github. (Look at `script.py`)

## Result

__it was the good idea__

We get the password 18300492070hello which collide the hash and it works.

# Gotcha!

horiz0nx{PHP_m4g1c_hash3s}
