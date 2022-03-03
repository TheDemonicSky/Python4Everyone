data = 'X-DSPAM-Confidence:0.8475'
pos = data.find(":")
length = len(data)
extracted = float(data[pos + 1 : length])
print(extracted)

#Learned how to extract data from a string
