from PIL import Image
import time
import psutil


# just like take in how many there are horizontally and veritcally then
filename = raw_input("/* Enter the sheet's name (pls incl. extension) */ ")
supposedSize = input("/* Enter what you think the height/width of a square tile is: */")
supposedRows = input("/* Enter the number of tile rows in the sheet: */")
supposedColumns = input("/* Enter the number of tile columns in the sheet: */")

originalSheet = Image.open(filename)
# well, i dunno. get the color of the first pixel and then find borders or something.
sheet = originalSheet.copy()

# so i guess i'll just like iterate over each row/column till I find something not 
# matching like the first pixel

width, height = sheet.size
top, bottom, left, right = 0,0,0,0 # bounds basically for the borders.
pixel1 = sheet.getpixel((0,0))

stop = False
if stop == False:
    for i in xrange(0, width):
        if stop == False:

            for j in xrange(0, height):
                pixel = sheet.getpixel((i, j))
                if(pixel != pixel1):
                    left = i
                    stop = True
                    break

stop = False
if stop == False:
    for i in xrange(0, width):
        if stop == False:

            for j in xrange(0, height):
                pixel = sheet.getpixel((width-(1+i), j))
                if(pixel != pixel1):
                    right = width-(i+1)
                    stop = True
                    break

stop = False
if stop == False:
    for i in xrange(0, height):
        if stop == False:

            for j in xrange(0, width):
                pixel = sheet.getpixel((j, i))
                if(pixel != pixel1):
                    top = i
                    stop = True
                    break

stop = False
if stop == False:
    for i in xrange(0, height):
        if stop == False:

            for j in xrange(0, width):
                pixel = sheet.getpixel((j, height-(i+1)))
                if(pixel != pixel1):
                    bottom = height-(i+1)
                    stop = True
                    break

print "/* top: ", top, " */"
print "/* left: ", left, " */"
print "/* bottom: ", bottom, " */"
print "/* right: ", right, " */"

leftoverSpace = height - supposedRows*supposedSize
leftoverV = 0
leftoverH = 0
if leftoverSpace % (supposedRows-1) == 0:
    leftoverV = leftoverSpace/(supposedRows-1)
else:
    leftoverV = leftoverSpace/(supposedRows+1)

leftoverSpace = width - supposedColumns*supposedSize
if leftoverSpace % (supposedColumns-1) == 0:
    leftoverH = leftoverSpace/(supposedColumns-1)
else:
    leftoverH = leftoverSpace/(supposedColumns+1)

print "/* supposed size: ", supposedSize, " */"
print "/* leftover lines: ", leftoverSpace, " */"
print "/* leftovers vertical: ", leftoverV, " */"
print "/* leftovers horizontal: ", leftoverH, " */"

for i in xrange(0, supposedRows):
    
    topEdge = top + i*(supposedSize+leftoverV)

    for j in xrange(0, supposedColumns):

        leftEdge = left + j*(supposedSize+leftoverH)

        firstThing = sheet.crop( (leftEdge, topEdge, leftEdge+(supposedSize), topEdge+(supposedSize)) )
        firstThing.show()
        time.sleep(1)
        for proc in psutil.process_iter():
            if proc.name == "display":
                proc.kill()

        lilName = raw_input()

        if lilName != "":
            print "."+lilName, "{"
            print "\tbackground: url('"+filename+"') "+str(leftEdge)+"px "+str(topEdge)+"px;"
            print "\twidth:"+ str(supposedSize) +";"
            print "\theight:"+ str(supposedSize) +";"
            print "}"

