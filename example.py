
# Printing a table Mike...
def printTable( aList ):
	
	firstEntry = aList[ 0 ];

	headers = []
	line = ''
	for key in firstEntry.keys():
		line += key + '\t'
		headers.append( key )

	print line

	for entry in aList:
		line = ''
		for header in headers:
			line += entry[ header ] + '\t\t'
		print line
	
# Basic lists
print 'Basic lists \n'
print( 'myvar = [ 1, 2, 3 ]' )
myvar = [ 1, 2, 3, ]
print myvar

print ''

#print myvar

# You can add things to myvar!
print 'myvar.append( 4 )'
myvar.append( 4 )
print myvar

print ''

print 'You can also make lists of lists...'
myvar = [ [ 'one', 'two', 'three' ], [ 'four', 'five', 'six' ], [ 'seven', 'eight', 'nine' ] ]
print "myvar = [ [ 'one', 'two', 'three' ], [ 'four', 'five', 'six' ], [ 'seven', 'eight', 'nine' ] ]"
print myvar

print ''

print 'And now you can reference any part of those lists by index. All lists are index by 0.'
print 'myvar[ 0 ]'
print myvar[ 0 ]

print ''

print 'myvar[ 0 ][ 1 ]'
print myvar[ 0 ][ 1 ]

print ''

print "Here's an example of why to append. Lets create a list of the multiples of 3..."
multiple = 3
values = []
for i in range( 0, 10 ):
	values.append( i * multiple )
print values
	
print ''

print 'For more on lists: http://docs.python.org/2/tutorial/datastructures.html'

print ''

print 'Dictionary example'

people = []

people.append( {
	'name': 'Mike',
	'dickSize': '6',
	'funFactor': '10'
} )

people.append( {
	'name': 'Andrew',
	'dickSize': '4',
	'funFactor': '7'
} )

people.append( {
	'name': 'Matt',
	'dickSize': '15',
	'funFactor': '2'
} )

printTable( people )
