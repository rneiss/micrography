import string
import re
from PIL import Image, ImageColor, ImageDraw, ImageFont
import requests
import json

#Set some variables. Feel free to play with these to your heart's content
imgBgColor = (120,120,120)  #rgb
sourceImage = "Pieter_Lastman_-_Jonah_and_the_Whale_-_Google_Art_Project.jpg"
destinationFile="output.png"
sefariaRef="Jonah 1-4" # valid text references can be found here: https://github.com/blockspeiser/Sefaria-Project/wiki/Text-References


#set some more variables. These probably shouldn't be mucked with too much.
fontSize = 10
fontDrawSize = 18
font = ImageFont.truetype("MiriamMonoCLM-Book.ttf", fontDrawSize)
imgMargin = 10
sampleDensity=1


def main():

    #image input
    sample = Image.open(sourceImage)
    width, height = sample.size
    
    #set pixel density to = 8.5"/11" @ ~300 dpi (i.e. width [330] * fontsize [10] / pixel density of 1), and resize other side to fit,
    if (width > height):
    	basewidth = 330
    	wpercent = (basewidth/float(sample.size[0]))
    	hsize = int((float(sample.size[1])*float(wpercent)))
    	sample = sample.resize((basewidth,hsize), Image.ANTIALIAS)
    	width, height = sample.size
    
    else:
    	baseheight = 300
    	hpercent = (baseheight/float(sample.size[1]))
    	wsize = int((float(sample.size[0])*float(hpercent)))
    	sample = sample.resize((wsize,baseheight), Image.ANTIALIAS)
    
    	width, height = sample.size


    #text input    
    url = 'http://www.sefaria.org/api/texts/'+sefariaRef
    params = dict(
    	commentary=0,
    	context=0
    )
    resp = requests.get(url=url, params=params)
        
    data = json.loads(resp.text)
     
    #remove whitespace, punctuation, nikkudot, taamim
    text=json.dumps(data['he']).decode('unicode-escape')    
    text = text.replace(u"\u05BE"," ")
    exclude = set(string.punctuation+u"\uFEFF"+"\n")
    text = ''.join(char for char in text if char not in exclude)
    strip_cantillation_vowel_regex = re.compile(ur"[^\u05d0-\u05f4\s]", re.UNICODE)
    text = strip_cantillation_vowel_regex.sub('', text)
    
    #output init
    outputImageSize = (width*fontSize//sampleDensity+imgMargin,height*fontSize//sampleDensity+imgMargin)
    outputImage = Image.new("RGB", outputImageSize, color=imgBgColor)
    draw = ImageDraw.Draw(outputImage)

	#cycle through each pixel, get the color, place the next letter in the text
    index = 0
    for y in range(0,height,sampleDensity):
        for x in range (width-1,0,-sampleDensity):  #this goes from width to 0 rather than vice versa to properly place hebrew
            color = sample.getpixel((x,y))

            if color != imgBgColor:
				try:
					draw.text((x*fontSize//sampleDensity, 
							   y*fontSize//sampleDensity), 
							   text[index], font=font, fill=color)

					index += 1
				except (IndexError):
					index = 0

    #save image
    outputImage.save(destinationFile)

if __name__ == '__main__':	
	main()