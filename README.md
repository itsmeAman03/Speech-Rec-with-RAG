## Speech-Rec-with-RAG

This project provides a command-line tool to transcribe audio files, identify their language, and perform summarization or translation on the transcribed text.

# Features

- **Transcription:** Uses the Whisper library to convert audio files to text.
- **Language Detection:** Identifies the language spoken in the audio file.
- **Summarization:** Generates a concise summary of the transcribed text (custom implementation).
- **Translation:** Translates the transcribed text to another language (custom implementation).

# Requirements\*\*

- Python 3.x
- Libraries:
  1. `whisper` ([https://openai.com/blog/whisper/](https://openai.com/blog/whisper/))
  2. `transformers`
     3, `dotenv`
  3. `requests`

# Installation

1. Clone or download the repository.
2. Create virtual environment.

   ```bash
   python -m venv env
   ```

3. Activate your virtual environment.
   ** For linux/MacOsS**

```bash
source env/bin/activate
```

**For windows:**

```bash
env/bin/activate

```

4. Install the required libraries:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project directory (if needed for translation). Add your environment variables for any secret keys used by `Translateionn`.
   Enter your RapidAPI in `.env` file

# Usage

1. Open a terminal and navigate to the project directory.
2. Copy your Audio files in Artifacts folder
3. Run the script:

   ```bash
   python main.py
   ```

**User Input**

The script will prompt you for the following information:

1. **Audio File Selection:** The script will list audio files found in a predefined directory. Choose the file you want to process by entering the corresponding index number.
2. **Option Selection:**
   - **1. Summarization:** Generates a summary of the transcribed text.
   - **2. Translation:** Translates the transcribed text to a target language you specify.

**Note:** The script uses custom implementations for summarization and translation (`summarization` and `Translateionn`). Make sure you have these modules defined in your project.

**Output**

The script will display the following based on your selection:

- **Transcription:** The transcribed text from the audio file.
- **Summary:** A summarized version of the transcribed text (if option 1 is chosen).
- **Translation:** The translated text in your target language (if option 2 is chosen).
