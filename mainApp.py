from flask import Flask, render_template, request, url_for, redirect, render_template_string
from app import GermanText
from pydub import AudioSegment

app = Flask(__name__)
app.secret_key = 'John The Ripper'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def currentTemp():
    if request.method == 'POST':
        
        wavFile = request.files['file']
        audio_file = wavFile
        filename = wavFile.filename        
        if audio_file.content_type != 'audio/wav' and audio_file.content_type not in ('audio/mpeg', 'audio/mp3'):            
            return redirect(url_for('home'))
        if audio_file.content_type not in ('audio/mpeg', 'audio/mp3'):         
            convertedText = GermanText.germanTextFromSpeech(audio_file)            
        else:
            audio = AudioSegment.from_file(audio_file)
            wavFile = audio.export('output.wav', format='wav')
            convertedText = GermanText.germanTextFromSpeech(wavFile)
        if convertedText[0] != False:            
            return redirect(url_for('home'))
        return render_template('index.html', convertedText=convertedText[1])
    return "Error"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
