## **Yalini Brhanavan - GMIT - H.Dip Data Analytics**

<img src="https://image.ibb.co/gw4Gen/Index_GMIT.png" alt="Index GMIT" border="0" />

* DATA REPRESENTATION AND QUERYING: Project 2020
* Sep 2020

---
## Project Outline
1. A basic Flask server that has a
2. REST API, (to perform CRUD operations)
3. One or more database table and
4. Accompanying web interface, using AJAX calls, to perform these CRUD operations.


**How to run the file:**
* Python version 3.8 was downloaded via Anaconda Navigator 3 to Windows 10 OS (https://www.anaconda.com/).
* Check FLASK APP and install it  
* I used a config.py, there is a template of this file in this git repository called 'dbconfigtemplate.py' please rename it and change the credentials. I have *config.py in gitignore. 
* I have also included sql script (initdb.sql) for the database and the table with sample data. you can use this to create the database (yalinidatarepresentation) and the tables (car and person).

<br/>
<img src="describecar.png" alt="Describe car" width="75%" height="75%" ><br/> 
<br/>
<br/>
<img src="describeperson.png" alt="describe person" width="75%" height="75%" ><br/> 
<br/>

* "server.py" that implement the REST API. After you run this file you can login to the local host in the following url http://127.0.0.1:5000/ . If you click the botton login it will take you to the data tables. I haven't set it up with the login credentials for the purpose of this project. 
* Staticpages folder contains the "login_css.html" and  "index.html" .  "index.html" will use AJAX to link to the server and provide a nice user interface.
* login_css.html is just another page and it does't do any function. I just wanted to show how another page could be connected to the home page and wanted to style and model a login page. 
* CarDao.py and PersonDao.py 

Webpage design:
Home page with Car Table and person Table. The webpage is inter linked with the login page.
<br/>
<img src="CarTable.png" alt="CarTable" width="75%" height="75%" ><br/> 
<br/> 
<img src="PersonTable.png" alt="PersonTable" width="75%" height="75%" ><br/> 

Login Page
<br/> 
<img src="loginpage.png" alt="loginpage" width="75%" height="75%" ><br/> 

----
**REFERENCES:** <br/> <br/>
* class notes
* https://stackoverflow.com/ 
* https://www.w3schools.com/
