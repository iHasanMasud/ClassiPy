# About

ClassiPy is a simple and efficient Python tool used to classify files into different categories based on their extension. It allows users to quickly and accurately sort through and organize files according to their type. ClassiPy supports a wide range of popular file types. With ClassiPy, users can easily keep their files organized and easily locate the files they need.

## Installation

1.Clone the repository

    git clone https://github.com/iHasanMasud/ClassiPy.git

2.Switch to the application folder

    cd ClassiPy

3.Create a virtual env
    
        python -m venv .

4.Activate virtual env
    
        # Bash
        source Scripts/activate
        # Windows
        Scripts/activate 

5.Install requirements
    
        python -m pip install -r requirements.txt


6.To run the code, you can use the following command:

        python ClassiPy.py
It will ask you to enter the full path of the folder you want to classify. Enter the path and press enter.

## If you want to create an executable file, skip step 6

7.To create the executable file, you can use the following command:

        pyinstaller --onefile ClassiPy.py

8.Find the exe file located in the ClassiPy/dist folder

9.Double-click the exe file to run the application, it will prompt for the path of the folder you want to classify

10.Write the path of the folder you want to classify and press enter
    
        # Example
        C:\Users\yourUserName\Downloads