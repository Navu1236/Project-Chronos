# Project-Chronos
AI Archeologist for digital text reconstruction.

Navaneeth - se24ucse079
Shirsha   - se24ucam027
Dhruv Bohra - se24ucam068
Anusha  - se24ucam006
Laranya -se24ucse205



Project Description
Project Chronos is a web application that reconstructs and clarifies incomplete, cryptic, or slang digital text fragments using Google Gemini AI and provides contextual explanations with real-world sources via SerpAPI. Users input informal or fragmented text, and the application returns a clear, grammatically correct reconstruction along with web results explaining the slang or phrase, helping bridge generational and linguistic digital gaps.


Setup Instructions

1. Clone the Repository

git clone https://github.com/Sherbo-pie/Project-Chronos.git
cd project-chronos

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows

3. Install Required Libraries and Dependencies

pip install -r requirements.txt

4. Setup Your API Keys

Create a `.env` file in the project root directory and add:
```
GEMINI_API_KEY=your_google_gemini_api_key
SERPAPI_API_KEY=your_serpapi_key
```
For team use or modular code (if needed):
```
GEMINI_API_KEY_FRIEND=your_teammate_gemini_key
```

Usage Guide

 1. Running the Application Locally

Start the Flask server:

```sh
python main.py
```

The application will be available in your browser at:  
`http://127.0.0.1:5000`

#2. Using the Application

- Visit the web page.
- Enter your fragmented or cryptic text (e.g., `smh at the top 8 drama`) in the provided input box.
- Click **Reconstruct**.
- View the AI-reconstructed (clear) text and contextual web links returned on the page.

Command-line Example (if supported)

If your application supports command-line input (optional):

```sh
python main.py "smh at the top 8 drama"
```

***

Project Structure

```
project-chronos/
├── main.py          # Main Flask backend/app
├── utils.py         # Helper for contextual sources (Gemini + SerpAPI)
├── templates/
│   └── index.html   # Frontend UI
├── static/          # Static files (images, styles)
├── requirements.txt # Python dependencies
├── .env             # Your API keys (do not share this publicly)
└── README.md        # Documentation (this file)
```


Example

Input fragment:
`smh at the top 8 drama`

AI-Reconstructed Text:
“Shaking my head at all the drama in the top eight.”

Contextual Sources:
- [Web article explaining ‘smh’](https://example.com)  
- [Relevant forum post](https://example.com)  
- [Slang dictionary entry](https://example.com)


Acknowledgements

- [Google Gemini API](https://ai.google.dev/)
- [SerpAPI](https://serpapi.com/)
- Flask, Requests, Python





You can copy this directly into your README.md—a clear, professional documentation for running and understanding your project!

[1](https://github.com/othneildrew/Best-README-Template)
[2](https://realpython.com/readme-python-project/)
[3](https://github.com/lincc-frameworks/python-project-template)
[4](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
[5](https://www.pyopensci.org/python-package-guide/tutorials/add-readme.html)
[6](https://git.ifas.rwth-aachen.de/templates/ifas-python-template/-/blob/master/README.md)
[7](https://github.com/topics/readme-template)
[8](https://www.makeareadme.com)
[9](https://www.youtube.com/watch?v=12trn2NKw5I)
