# KeyReader

＃ Goal
* To help us record account and Key easily,and encode our data to protect it.

＃ Usage
* pip install model then run main.py with python.

# Function of the program

* Setting Your Own account in the register page.
* After register an account, it will create a accountname.json data.(though it has been encoded,but still protect it as well.)
* ADD,Delete,KeyWord Search Your Account and Key.
* Click button to copy your Account or Key to scrapbook.
* Using QRcode to copy your Account or Key to your phone.

# What you can do easily to make it more usefully.
* In encode(data) and decode(data) function,you can make your own rule to encode data.
  - data is a dictionary
* In setting you can setup your own program key.
  - default is ' programkey = datetime.now().strftime("%Y%m%d") '
* If you are using Mac, please change the AppPath absolute path in setting.


  



