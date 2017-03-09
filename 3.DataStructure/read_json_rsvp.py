import json 
import pprint 



meetupfile = open('MeetupRsvpStream-1-2017-02-24-00-00-28-1c4c16e9-7835-4b70-bead-1b6a3cc52c30',
'r').read()

splitText = meetupfile.split('\n')

pprint.pprint(json.loads(splitText[1]))

