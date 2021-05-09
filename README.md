# shopify-code-challenge
This repo is for shopify fall 2021 backend internship position
### How to run
Install python3 and flask```pip3 install flask```(or ```pip install flask```). 
Clone the repo, and run it by using ```sudo python app.py```(or ```python app.py```). 
Open ```http://127.0.0.1:8080/``` in browser.
### What I did 
Finish Add image(s) to the repository idea.<br />
##### Features
Click ```Choose Files``` button to upload one/bulk of images with .jpg/.png/.gif extensions. 
Image larger than 1MB(1024*1024) will be refused. 
Then click ```submit``` to upload images and show in page.
##### Tests
From ```tests``` folder, select one or many ```xxxSuccess```files(like jpgSuccess.jpg) at the same time to upload. (success) <br />
From ```tests``` folder, select one or many ```xxxFail```files(like jpgFail.jpg) at the same time to upload. (fail as expected, and return 413 error)
(because file is large than 1MB)<br />
From ```tests``` folder, select ```jpeg1.jpeg```file at the same time to upload. (fail as expected, return 400 error)
(because file does not have required extension)<br />






 