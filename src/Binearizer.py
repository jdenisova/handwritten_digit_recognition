class Binearizer:
  """
  Бинеаризует изображение.
  """
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(ImageBinearizer, cls).__new__(cls)
    return cls.instance

  def _to_gray_image(self, image: np.array) -> np.ndarray:
    """
    Преобразует цветное изображение в серое (один канал - яркость).
    
    Вход: цветное изображение.
    Выход: серое изображение.
    """
 
    img = img_as_float(image)
 
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
 
    return 0.2126*r + 0.7152*g + 0.0722*b
 
  def binarize_p(self, image: np.ndarray, p: float) -> np.ndarray:
    """
    Пороговая бинеаризация изображения.
    """
    gray_image = self._to_gray_image(image)

    n, m = gray_image.shape
    
    for i in range(n):
      for j in range(m):
        gray_image[i, j] = 1 if gray_image[i, j] > p else 0
    return gray_image
