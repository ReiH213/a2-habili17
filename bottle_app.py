#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file

def static_file_callback(filename):
 return static_file(filename, root='./')

def htmlify(text):
    page = """
        <!doctype html>
         <html lang="en
         <head>
         <meta charset="utf-8" />
  
 <title> My Garage</title>
 
<style>
   
body {
     background-image: url("./static/wallpaper.jpg")
}
.header {
      background-color: transparent;
      text-align: center;
      padding: 15px;
}
.navbar {
    overflow: hidden;
    background-color: black;
}
.navbar a {
    float: left;
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: transparent;
}
li {
    float: left;
    color:silver;
}
li a {
    display: block;
    color: silver;
    text-align: center;
    padding: 15px 15px;
    text-decoration: none;
    font-size:25px;
}
li a:hover {
    background-color: #111;
}
  a {
     color: chocolate;
}  
  h1 { 
    color: chocolate;
    text-align: center ;
}
p {
 color:silver;
 font-size:19px;
}
</style>
</head>
<body >
 <div class="header">
  <h1>  My </h1>
 </div>
 
  <div class="navbar">
        <ul class="main-nav">
            <li><a href="./."> HOME </a></li>
            <li><a href=""> GALLERY </a></li>
            <li><a href=""> ABOUT </a></li>
            <li><a href="contact.html"> CONTACT </a></li>
        
        </ul>
         </div>
          <p>Comment</p>
<form action="/" method="get">
                   <input type="text" name="comment" style="width:200px; height:100px" />
                </form>
                <p>Password</p>
    <form action="/" method="get">
                   <input type="text" name="password" />
                   <input type="submit" value="submit" />
                </form>
%s
        </body>
        </html>
    """ % (text)
    return page







route('/', 'GET',homepage)
route('/static/<filename>', 'GET', static_file_callback)


#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
