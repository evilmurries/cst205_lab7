def get_pic():
 return makePicture(pickAFile())

def pyCopy(source, target, targetX, targetY):

  sourceWidth = getWidth( source )
  sourceHeight = getHeight( source )
  targetWidth = getWidth( target )
  targetHeight = getHeight( target )
  
  for x in range( 0, sourceWidth ):
    for y in range( 0, sourceHeight ):
      pixel = getPixel( source, x, y )
      color = getColor( pixel )
      
      if x + targetX < targetWidth - 1 and y + targetY < targetHeight - 1:      
        setColor( getPixel( target, x + targetX, y + targetY ), color )
        
  return target
def makecollage():
  target = makeEmptyPicture( 950, 1300, white)
  picture1 = get_pic()
  picture2 = get_pic()
  picture3 = get_pic()
  picture4 = get_pic()
  picture5 = get_pic()
  
  target=pyCopy(picture1,target, 200, 350)
  target=pyCopy(picture2,target, 500, 200)
  target=pyCopy(picture3,target, 175, 900)
  target=pyCopy(picture4,target, 175, 200)
  target=pyCopy(picture5,target, 500, 900)

  show(target)
