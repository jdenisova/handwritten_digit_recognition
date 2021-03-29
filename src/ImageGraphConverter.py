class ImageGraphConverter:
  """
  Преобразует бинеаризованное изображение в граф.
  """
  
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(ImageGraphConverter, cls).__new__(cls)
    return cls.instance

  def convert_image_to_grath(self, image, color=0):
    n, m = image.shape
    E = []
    vertexes = []
    for i in range(1,n-1):
      for j in range(1,m-1):
        if image[i,j] != color:
          continue

        temp = []
        vertexes.append((i,j))
        if image[i-1,j] == color:
          temp.append((i-1,j))
        if image[i+1,j] == color:
          temp.append((i+1,j))
        if image[i,j-1] == color:
          temp.append((i,j-1))
        if image[i,j+1] == color:
          temp.append((i,j+1))
            
        E.append(temp)
    return E, vertexes
