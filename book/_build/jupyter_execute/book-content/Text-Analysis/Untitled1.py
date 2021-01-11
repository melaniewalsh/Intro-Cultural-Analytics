import regex as re

sample = """This is how the world ends
This is how the world ends 
Not with a bang
But with the president announcing on live TV he intends to steal the election"""

output = (re.search('(?<=not with a bang)[\s\S]*', sample, re.IGNORECASE)).group()
output = output.replace('\n', '').lower()
sample_output= f'💥💥💥\nThis is the way the world ends\nThis is the way the world ends\nNot with a bang {output}\n💥💥💥\n\n'
print(sample_output)

re.search('(?<=not with a bang)*', sample, re.IGNORECASE)[0]

len("""💥💥💥
This is the way the world ends
This is the way the world ends
Not with a bang but with the president announcing on live tv he intends to steal the election
💥💥💥""")

sample = "And that's the way the world ends, not with a bang, but with a non-productive cough."

sample = ' '.join(sample.lower().split()) 

sample = ' not with a bang'

"not with a bang but" in sample

re.sub(r'[\'"”.,]','',sample)

re.sub(r'^https?:\/\/.*[\r\n]*', '', sample, flags=re.MULTILINE)

re.sub(r'^ ', '', sample)

