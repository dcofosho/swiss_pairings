<h1>Daniel Cohen: Swiss Pairing</h1>

<p> This is code for maintaining player/match information 
and generating "swiss pairs" in a tournament</p>

<hr>

<h2>Requirements</h2>
<ul><a href="https://www.python.org/downloads/release/python-2712/">
Click here to install Python 2.7 (if you have not already done so)</a></ul>
<ul><a href="https://www.vagrantup.com/">
Click here to install Vagrant and create an Atlas account (if you have not already done so)</a></ul>

<h2>Instructions</h2>
<ul>Place the project folder in the same directory as your vagrantfile</ul>
<ul>Run vagrant login, vagrant up, and vagrant ssh from your terminal/shell</ul>
<ul>Run psql -f tournament.sql to create the necessary databases on your VM 
(only necessary first time, or if you delete you databases)</ul>
<ul>Run python tournament.py</ul>
