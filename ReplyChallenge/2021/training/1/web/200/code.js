

document.getScript("https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js", function()
{
    document.getScript("https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/sha256.js", function()
    {
        function auth() {
            var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x73"); // ops...missing last byte!
            var u = document.getElementById("user").value;
            var p = document.getElementById("pass").value;
            var t = false;
        
            if(u == "\x68\x34\x63\x6b\x33\x72") {
                var enc = CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), { iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) });
                if(enc == "PKhuCrfh3RUw4vie3OMa8z4kcww1i7198ly0Q4rpuyA=") {
                    t = true;
                }
            } 
        
            if(t) {
                console.log("Congratulations, you won! You can now submit the password as the FLAG of the challenge :-)");
            } else {
                console.log("Wrong credentials! :(");
            }
        }
        
        auth();
    });
});


