0x14. Javascript - Web scraping

General
Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module

General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
All your files must be executable
The length of your files will be tested using wc
You are not allowed to use var


Install Node 10
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

Install semi-standard
$ sudo npm install semistandard --global

Install request module and use it
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

Tasks:
0. Readme
Write a script that reads and prints the content of a file.

1. Write me
Write a script that writes a string to a file.

2. Status code
Write a script that display the status code of a GET request.

3. Star wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

4. Star wars Wedge Antilles
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

5. Loripsum
Write a script that gets the contents of a webpage and stores it in a file.

6. How many completed?
Write a script that computes the number of tasks completed by user id.

7. Who was playing in this movie? #advanced
Write a script that prints all characters of a Star Wars movie:

8. Right order #advanced
Write a script that prints all characters of a Star Wars movie:

9. Twitter Auth #advanced
Write a Javascript script that takes in 3 strings and sends a search request to the Twitter API
