text= "X-DSPAM-Confidence:    0.8475"
a=text.find(":")
tex=text[a:]
print(float(tex))