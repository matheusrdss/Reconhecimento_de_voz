# Primeiro, importamos a biblioteca "Speech Recognition", para baixar cole no prompt de comando "pip install SpeechRecognition"
import speech_recognition as sr
import pyaudio

# Aqui vamos inicializar o "sr" para que ele reconheça as falas nas próximas linhas
# Simplificando, o "r" é o que vamos usar como reconhecedor de fala
r = sr.Recognizer()

# Aqui falamos para ele usar o microfone (source = microfone padrão do dispositivo)
with sr.Microphone() as source:
    # Depois mostra que esta realmente ouvindo e funcionando
    print("Ouvindo: ")
    # e aqui ele transforma o que ouviu do microfone utilizado para a captura em uma variavel que vamos chamar de "audio"
    # de maneira simples, ele pega a ferramenta "listen" que esta no "r" para ouvir o que recebe do microfone
    audio = r.listen(source)

# Aqui vamos alterar o audio para portugues BR com uma ferramenta do google e guardar na variavel "ouviu"
ouviu = r.recognize_google(audio, language='pt-BR')

# Nessa linha o print tem uma formatação para adicionar o que ouviu em seguida do "Eu ouvi"
print(f'Eu ouvi: {ouviu}')

#AVISO-----------------
# SE O CÓDIGO DER ALGUM ERRO, VERIFIQUE SE O PYAUDIO ESTA INSTALADO, SE NÃO ESTIVER, EXECUTE NO PROMPT DE COMANDO:
# pip install pyaudio