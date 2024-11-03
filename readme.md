# Zed PyServer

1.[description](#description) 
2.[dependencies](#dependencies) 
3.[how to use](#use)

## description

This is a small script written in python aimed at those who use the zed code editor on Linux OS. 
This will allow you to serve files in the web development process and see the changes in your preferred browser in real time. This file includes the languages ​​commonly used in web development (html, css, js, jsx, ts, tsx). You can add more extensions files in watch_directories def.

## dependencies
Linux systems already have python3 installed by default.  
You just need to use the venv module to create a virtual environment, activate it, and then install livereload.

## use 
open a terminal in the root directory of your project.

you can copy the content of server.py file or `git clone `

1.[create and activate the virtual environment]

```
python3 -m venv venv
#activate virtual environment
source venv/bin/activate
# you should see (venv) in your CL 
```
2.[install livereload]
```
pip install livereload
#now you can run the server 
python3 server.py
```
3.[try it]

open your browser in localhost:3000. 
You can modify port in server.py : 
```
server.serve(root='.', host='0.0.0.0', port=3000)
```
and add more extensions files in watch_directories function.
example: `server.watch(os.path.join(subdir, dir_name, '*.svg'))`

4.[deactivate virtual environment]
```
#terminal
deactivate
```

don`t forget add server.py and venv in your .gitignore file