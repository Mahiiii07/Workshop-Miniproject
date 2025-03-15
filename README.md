  For Task A and B  
How to install dependencies :

    pip install gradio torch torchvision pillow requests


How to run my app :

    Steps : 
	
    1) Go to folder where you saved this file.
    2) Activate the virtual environment : env1\scripts\activate
    3) Run the app : python Task_A_B.py


Purpose of each Component in my Project :

    1) PyTorch (torch) → Loads & runs the pre-trained ResNet18 model for image classification.
	
    2) Torchvision (torchvision.transforms, torchvision.models) → Provides image preprocessing tools and ResNet18 model.
	
    3) PIL (Pillow) → Handles image input and processing.
	
    4) Requests (requests) → Fetches the ImageNet labels from an online source.
	
    5) Gradio (gradio) → Creates an interactive web UI for the game.
	
    6) ResNet18 Model (resnet18(pretrained=True)) → A deep learning model trained on ImageNet for object recognition.

  For Task C 
  
How to install dependencies :

    1) pip install selenium pyautogui
    2) After downloading, place the driver in project folder or add its path in the script:
        driver = webdriver.Chrome(executable_path="path/to/chromedriver")

How to run my app :

    1) Go to folder where you saved this file.
    2) Activate the virtual environment : env1\scripts\activate
    3) Run the app : python Task_C.py

Purpose of each Component in my Project :

    1) Selenium WebDriver : 
    
        - webdriver.Chrome() → Opens Chrome browser.
        - driver.get('https://www.youtube.com/') → Navigates to YouTube.
        - find_element(By.NAME, 'search_query') → Locates the search bar.
        - send_keys() → Enters search text and presses Enter.
        - driver.quit() → Closes the browser.

    2) PyAutoGUI
        - moveTo(x, y) → Moves the mouse to a specific (x, y) coordinate on the screen.
        - click() → Clicks at the current mouse position.
        - Used for selecting a video, liking, and closing the tab.
