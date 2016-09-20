#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sat
#
# Created:     13/01/2015
# Copyright:   (c) Sat 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from xml.etree.ElementTree import fromstring

def readXML(xmlstr):
	tree = fromstring(xmlstr)
	display_content(tree)

def display_content(tree):
    if tree.tag == 'br':
        print "\n"
    elif tree.text == None:
        print tree.tag
    else:
        print "%s:%s"%(tree.tag, tree.text)
    for child_node in tree:
        display_content(child_node)


if __name__ == '__main__':
	xmlstr= '<Address><br></br><to>James</to><from>Jani</from><heading>Reminder</heading><body>Please check your mail.</body></Address>'
	readXML(xmlstr)