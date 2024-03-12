import openai, playsound, time
openai.api_key = "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"

def typingPrint(text):
  for character in text:
    print(character, end='', flush=True)
    time.sleep(0.05)  # Adjust the speed of typing here
  print()  # Move to a new line after the text is typed out

def EVAAI(Bool, userInput):
  while (Bool):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": userInput}
      ]
    )

    message = completion.choices[0].message.content

    new_message = ""
    while len(message) > 0:
      # Find the index of the last space character before the 90th character
      index = message.rfind(" ", 0, 90)
      if index == -1:  # No space found in the first 90 characters
        index = 90
      # Add the line up to the last space character to the new message
      new_message += message[:index] + "\n"
      # Remove the line from the original message
      message = message[index:].lstrip()


    from gtts import gTTS



    text = new_message

    language = 'en'

    speech = gTTS(text=text, lang=language, slow=False)

    speech.save("text.mp3")
    # wait for the sound to finish playing?
    blocking = False

    playsound.playsound("text.mp3", block=blocking)

    typingPrint(new_message)

    Bool = False


