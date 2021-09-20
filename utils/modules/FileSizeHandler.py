import os


class SizeCalculator:
  def convert_size(self, size, unit):
    """ Take size in bits convert it in whatever unit """
    units = {
      'B' : lambda size: size / 1024**0,
      'KB': lambda size: size / 1024**1,
      'MB': lambda size: size / 1024**2,
      'GB': lambda size: size / 1024**3,
      'TB': lambda size: size / 1024**4,
    }

    unit_size = units[unit](size)
    return unit_size

  def get_file_size(self, file_path):
    return os.path.getsize(file_path)

  def get_folder_size(self, location, unit='MB'):
    size = self.get_folder_size_raw(location)
    return self.convert_size(size, unit)

  def get_folder_size_raw(self, location):
    size = 0
    for path, dirs, files in os.walk(location):
      for f in files:
        file_path = os.path.join(path, f)
        size += self.get_file_size(file_path)
    return size

  def get_request_size(self, request, unit):
    size = len(request.data)
    return self.convert_size(size, unit)

  def get_response_size(self, response, unit):
    if response.status_code > 250:
      return 0

    size = len(response.content)
    return self.convert_size(size, unit)


