import os
import dotenv

dotenv.load_dotenv()
from google.cloud import texttospeech

# Set the text input to be synthesized
output_destination = "output_files"

# Error check for Output Folder
if not os.path.exists(f"{output_destination}"):
    os.mkdir(f"{output_destination}")

class TextToSpeech:
    def __init__(self):
        API_KEY = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
    
    def synthesize_text(self, target_text):
        synthesis_input = texttospeech.SynthesisInput(text=target_text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        
        with open(f"{output_destination}/text_output.mp3", "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
            
    def synthesize_text_index(self, target_text, index):
        synthesis_input = texttospeech.SynthesisInput(text=target_text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        
        with open(f"{output_destination}/output{index}.mp3", "wb") as out:
            # The response's audio_content is binary.
            # Write the response to the output file.
            out.write(response.audio_content)
            print(f'[synthesize_text_index] Content written to file "output{index}.mp3"')
    
    def synthesize_narrations(self, response): 
        # Response variable is going to be from Konstantin's Module
        slides = response["slides"]
        for i in range(len(slides)):
            self.synthesize_text_index(slides[i]["narration"], i)
        print(f"[COMPLETE] Created Narrations for {len(slides)} slide objects.")
        
        

# Test Code
tts = TextToSpeech()

test_response = {
  "slides": [
    {
      "narration": "In this first slide, we will learn how to work with Phoenix Channels by establishing a connection from the client to the channel running on the server. To accomplish this, we need to create a new socket object and pass it a path to the socket.",
      "image_description": "Client establishing connection to server"
    },
    {
      "narration": "Once we have the socket object, we can establish a connection to the path we defined when we created it. Next, we need to define a new channel object before we're ready to start pushing messages down the server.",
      "image_description": "Socket connecting to server"
    },
    {
      "narration": "To create a new channel object, we invoke the socket.channel function with the topic-subtopic and some parameters. These parameters will be passed to the join/3 function in the GameChannel.",
      "image_description": "Creating new channel object"
    },
    {
      "narration": "We can make this process neater and more flexible by wrapping the socket.channel call in a new function called new_channel. This function will take a subtopic and the screen name of the player who wants to join.",
      "image_description": "Wrapping socket.channel call in new_channel function"
    },
    {
      "narration": "Now, we can invoke the new_channel function with a player's name to generate a new channel object, which will already have the specified parameters baked into it.",
      "image_description": "Invoking new_channel function with player's name"
    },
    {
      "narration": "Before clients can do anything more meaningful in a channel, they need to join it on a topic-subtopic combination. To let users do that, we need to implement a join/3 function in the IslandsInterface.GameChannel module.",
      "image_description": "Implementing join/3 function"
    },
    {
      "narration": "Now that we have a simple clause of the join/3 function, let's go to the IEx session we have running and compile our new GameChannel. Then, we need to get a client to use join/3. For that, we'll need some JavaScript, which we'll write in the next section.",
      "image_description": "Compiling GameChannel and writing JavaScript"
    },
    {
      "narration": "We have now established a client connection to the server and implemented a join/3 function. The next steps involve modeling the game state, rendering the player and opponent boards, and mapping DOM events to functions that update the game state.",
      "image_description": "Modeling game state and rendering boards"
    }
  ]
}

tts.synthesize_narrations(test_response)