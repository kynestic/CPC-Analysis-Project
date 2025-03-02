<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">CPC Analysis Project</h3>

  <p align="center">
    <br />
    <a href="https://curvy-scene-7cf.notion.site/Project-Report-NVIDIA-Stock-Prediction-12638586a6b380f89c51df52f44d56c4"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/kynestic/NVIDIA-Stock-prediction/issues">Report Bug</a>
    ·
    <a href="https://github.com/kynestic/NVIDIA-Stock-prediction/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was created with the main goal of researching and learning how to use some popular models such as BERT, T5 and CLIP to process events then combine with buy/sell/volume data to predict NVIDIA's stock price in the future.

<!-- GETTING STARTED -->
## Getting Started
Before setting up the project, you need to install the following:

1. Visual Studio Code (VSC)  
  Visual Studio Code is a lightweight, powerful code editor that supports extensions for various programming languages.

2. Python 3.x  
  Python is the programming language required to run the project. Ensure you have version 3.x installed.

3. venv (Virtual Environment)  
  A virtual environment is recommended to isolate project dependencies. This can be created using the built-in `venv` module in Python.

### Major Dependencies
- **huggingface-hub** (0.25.2)
- **numpy** (2.1.1)
- **pandas** (2.2.3).
- **scikit-learn** (1.5.2)
- **scipy** (1.14.1)
- **torch** (2.4.1)
- **transformers** (4.45.2)
- **selenium** (4.25.0)
- **ipykernel** (6.29.5)  

### Installation
1. Clone the repo
  ```sh
  git clone https://github.com/kynestic/NVIDIA-Stock-prediction
  ```
2. Setup (and activate) your environment
  ```sh
  python -m venv /path/to/new/virtual/environment
  /path/to/new/virtual/environment/Scripts/activate
  ```
3. To install the necessary libraries and frameworks, enter the following command into the terminal:
  ```sh
  cd path/to/project
  pip install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
## Usage
  Due to the lack of CPC data in real life, we only create synthesis data with the support of LLM: chatGPT, Gemini,...
  Follow the path data\synthesis, we can see the file data_synthesis.py. This is where we create synthesis data for prediction task.

<!-- ROADMAP -->
## Roadmap


<!-- CONTRIBUTING -->
## Contributing


<!-- LICENSE -->
## License


<!-- Authors -->
## Authors
Nguyen Manh Duc - ducnguyenmanh7791@gmail.com  
Nguyen Thi Yen - haiyen190903@gmail.com  

Project document: [Link](https://curvy-scene-7cf.notion.site/Project-Report-CPC-trend-prediction-12638586a6b380f89c51df52f44d56c4?pvs=4)
<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements


## Thank you

<!-- If this is useful: [![Buy me a coffee](https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg)](https://www.buymeacoffee.com/catiaspsilva) -->
