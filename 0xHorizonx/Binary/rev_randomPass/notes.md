# INFO

After decompiling with ghidra, in the main func, we can see :

  while( true ) {
    sVar3 = strlen(key);
    if (sVar3 <= (ulong)(long)i) break;
    flag[i] = key[i] ^ encrypted[i];     
    i = i + 1;
  }

So we get the line `flag[i] = key[i] ^ encrypted[i];` => the result of the XORing for each frame is saved in a register (RDX). Then, we only have to do `next` with gdb-peda to see in the register each char of the flag string.

That's it.

# Gotcha !

horiz0nx{REver$e_1s_c00L}


