# %%
api_key="AIzaSyD0DAXRJjrK7EQwZK37lE7Zxm8oNgiKSTk"



# %%
import google.generativeai as genai

# %%
import os
google_api_key=os.getenv('AIzaSyD0DAXRJjrK7EQwZK37lE7Zxm8oNgiKSTk')
genai.configure(api_key=google_api_key)

# %%
model=genai.GenerativeModel('gemini-1.5-pro-latest')

# %%
def to_markdown(text):
    text=text.replace(".","  *,")
    return Markdown(textwrap.indent(text, '> ',predicate=lambda _:True))


# %%
model

# %%
from IPython.display import Markdown
from IPython.display import display
import textwrap

# %%
genai.GenerativeModel(
    model_name='models/gemini-1.5-pro-latest',
    generation_config={},
    safety_settings={},
    tools=None,
    system_instruction="You are a doctor and You are provided with any wound you must reply by saying what main 3 steps to be taken at that time , what all medicines or cream or bandage to be used. Provide me this details point wise, keep it under 60 words, a subheading for medication to be taken must be there",
)

# %%
response=model.generate_content("bruise")

# %%
to_markdown(response.text)

# %%
def response(text):
    r=model.generate_content(text)
    return(to_markdown(response.text))
    

# %%
def generate_and_format_markdown(input_text):
    
    response = model.generate_content(input_text)
    return to_markdown(response.text)

# markdown_content = generate_and_format_markdown("Input your text here")
# display(markdown_content)

# %%
import glob
img='runs/detect/predict*/image0.jpg'
image=model.generate_content(["Write a very short discription about the Detection of wound,structure of wound,shape of wound,the amount of blood and redness visible in the wound,how serious the wound can be seeing through the image give this in point wise and only one word answer for example detected: Laceration , this detected must be the first point alwasy,Blood visible: High, seriousness: Moderate and can be treated by medicine it self, structure: Oval shaped, The Heading must be WOUND ANALYSIS OF IMAGE nothing else to be there in heading, every thing must be in point wise.", img],stream=True)
image.resolve()

# %%
to_markdown(image.text)

# %%
import glob
def analyze_wound(image_path):
    
    prompt = [
        "Write a very short description about the structure of wound, shape of wound, the amount of blood and redness visible in the wound, how serious the wound can be seeing through the image. Give this in point wise and only one word answer for example ssWhich type of wound, Blood visible: High/low/moderate, seriousness: Moderate/low/high, structure: Oval shaped. The Heading must be WOUND ANALYSIS OF IMAGE, nothing else to be there in heading, everything must be in point wise.",
        image_path
    ]
    image = model.generate_content(prompt, stream=True)
    image.resolve()
    return to_markdown(image.text)

# %%


# %%



