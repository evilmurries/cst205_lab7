# Team 10 - Tech Life Balance Best Engineers
# Lab 7 Module 3


# This warmup function draws a snowman on the supplied desert image
def draw_snowman():
  pic = get_pic()
  height = getHeight(pic)
  width = getWidth(pic)
  
  # Make the snowman body
  addOvalFilled(pic, 100, height - 150, 100, 100, white)
  addOvalFilled(pic, 115, height - 210, 75, 75, white)
  addOvalFilled(pic, 125, height - 265, 60, 60, white)
  
  
  explore(pic)
  return pic

# This function returns opens a file browser and returns the file
def get_pic():
 return makePicture(pickAFile())

# This function receives a source and target image, then
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

# This function assembles a collage out of user selected image files
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
  return target