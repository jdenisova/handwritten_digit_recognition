from skimage.io import imread
import numpy as np

class Loader:
  """
  Загрузка изображения и преобразование в массив np.ndarray
  """
  
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Loader, cls).__new__(cls)
    return cls.instance

  def __init__(self):
    self._prefix = ""

  @property
  def prefix(self):
    return self._prefix

  @prefix.setter
  def prefix(self, value: str):
    self._prefix = value
 
  def load(self, file_name: str) -> np.ndarray:
    return imread(self.prefix + file_name)
