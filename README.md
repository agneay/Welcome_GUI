# Welcome_GUI [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
## A simple hackable start up welcome application


![](https://img.shields.io/badge/maintained-yes-green?style=for-the-badge)
![](https://img.shields.io/github/forks/agneay/Welcome_GUI?style=for-the-badge)
![](https://img.shields.io/github/issues/agneay/Welcome_GUI?style=for-the-badge)
![](https://img.shields.io/github/stars/agneay/Welcome_GUI?style=for-the-badge)
![](https://img.shields.io/github/license/agneay/Welcome_GUI?style=for-the-badge)

I bellieve in complete hackable software and creativity freedom and thats exactly why I created Welcome_GUI. With easy to install and setup process

> NOTE: Currently this application is only available for linux

## Getting Started
Clone the repo
```
git clone https://github.com/agneay/Welcome_GUI
cd Welcome_GUI
```

create a folder named Welcome_GUI by the following command
```
mkdir ~/.config/Welcome_GUI
```

copy `main.py` and `config.json` files to `Welcome_GUI` folder

## Dependencies
- Python3.12.3
- Pip
- Pip packages [AppOpener,pillow,tkinter,json]

  To install the pip packages run the following commands
  ```
  pip install pillow AppOpener tkinter json
  ```
  or alternatively run
  ```
  pip install -r requirements.txt
  ```

## A simple basic configuration example:
![](https://github.com/agneay/Welcome_GUI/blob/main/assets/example.png)

## Default config file : config.json
```json
{
    "_comment":"BASIC CONFIGURATIONS",
    "_comment":"DO NOT DELETE ANY OPTION",
    "Background":"Black",
    "Title":"Welcome to my OS",
    "Geometry":"990x600",
    "Icon":"./assets/icon.ico",
    "Heading":"Welcome to Agneay's OS",
    "Logo":"./assets/icon.ico",
    "Body":"This is a simple startup screen created by AGNEAY B NAIR",


    "_comment":"ADVANCED CONFIGURATIONS FOR HEADING",
    "Heading_fg":"white",
    "Heading_bg":"Black",
    "Heading_size":"40",
    "Heading_font":"Arial",
    "Heading_padx":"50",
    "Heading_pady":"50",

    "_comment":"ADVANCED CONFIGURATIONS FOR BODY",
    "Body_fg":"white",
    "Body_bg":"Black",
    "Body_size":"20",
    "Body_font":"Arial",
    "Body_padx":"50",
    "Body_pady":"50",

    "_comment":"BUTTONS FOR QUICKLAUNCH APPLICATIONS",
    "btn_1_text":"whatsApp",
    "btn_2_text":"telegram desktop",
    "btn_3_text":"notepad",
    "btn_4_text":"atom",


    "_comment":"ADVANCED CONFIGURATIONS FOR BUTTONS",
    "Btn_1_fg":"White",
    "Btn_2_fg":"White",
    "Btn_3_fg":"White",
    "Btn_4_fg":"White",
    
    "Btn_1_bg":"Black",
    "Btn_2_bg":"Black",
    "Btn_3_bg":"Black",
    "Btn_4_bg":"Black"
}
```

Feel free to edit this config file


Add the following line to your startup script in linux
```
python ~/.config/Welcome_GUI/main.py
```


## Installation via install.sh
>NOTE: `install.sh` is currently under development phase, the use of  `install.sh` is not recommended

To install via `install.sh` use the following commands
```
chmod +x install.sh
./install.sh
```
 

