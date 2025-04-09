# vvibesmusehub

## AI Music Generator App

This is a Python-based AI music generator app for macOS, specifically optimized for Apple M1 hardware. The app uses Hugging Face to search and download the models required for music generation. Users can customize the directory where the models will be downloaded.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/vvibesmusehub.git
   cd vvibesmusehub
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the app:
   ```sh
   python app.py
   ```

2. Follow the on-screen instructions to generate music.

## Customizing the Directory for Model Downloads

To customize the directory where the models will be downloaded, you can modify the `config.py` file. Set the `MODEL_DIR` variable to your desired directory path.

Example:
```python
MODEL_DIR = "/path/to/your/custom/directory"
```
