from PIL import Image, ImageDraw, ImageFont
import textwrap


def generate_meme(image_path, top_text, bottom_text='', font_path='font\\impact.ttf', font_size=9):
	# load image
	im = Image.open("moeiz.jpeg")
	draw = ImageDraw.Draw(im)
	image_width, image_height = im.size
	
	# load font
	font = ImageFont.truetype(font="font\\impact.ttf", size=int(image_height*font_size)//100)

	# convert text to uppercase
	top_text = top_text.upper()
	bottom_text = bottom_text.upper()

	# text wrapping
	char_width, char_height = font.getsize('A')
	chars_per_line = image_width // char_width
	top_lines = textwrap.wrap(top_text, width=chars_per_line)
	bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

	# draw top lines
	y = 10
	for line in top_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill='white', font=font)
	    y += line_height

	# draw bottom lines
	y = image_height - char_height * len(bottom_lines) - 15
	for line in bottom_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill='white', font=font)
	    y += line_height

	# save meme
	im.save('meme-' + im.filename.split('/')[-1])


if __name__ == '__main__':
	top_text = "Testing"
	bottom_text = "Bikin meme pake python moment"
	generate_meme('./idontalways.jpg', top_text=top_text, bottom_text=bottom_text)