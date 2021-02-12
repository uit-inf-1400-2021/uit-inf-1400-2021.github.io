
import math

square = [(1,1), (1,2), (2,2), (2,1)]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter                
    


import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

class Polygon:
    def __init__(self):
        self.vertices = []
    def add_point(self, point):
        self.vertices.append((point))
    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)



import os
import shutil
import zipfile

class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
       
    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)
    
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()
        
    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()
            
    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
            shutil.rmtree(self.temp_directory)


#from zip_processor import ZipProcessor
import sys
import os

class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        '''perform a search and replace on all files
        in the temporary directory'''
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()

#from zip_processor import ZipProcessor
import os
import sys
from pygame import image
from pygame.transform import scale

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in os.listdir(self.temp_directory):
            im = image.load(self._full_filename(filename))
            scaled = scale(im, (640,480))
            image.save(scaled, self._full_filename(filename))

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()


# composition

import os
import shutil
import zipfile

class ZipProcessor:
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
        self.processor = processor
        
    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)
    
    def process_zip(self):
        self.unzip_files()
        self.processor.process(self)
        self.zip_files()
        
    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()
            
    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)



from zip_processor import ZipProcessor
import sys
import os

class ZipReplace:
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string
        
    def process(self, zipprocessor):
        '''perform a search and replace on all files in the
        temporary directory'''
        for filename in os.listdir(zipprocessor.temp_directory):
            with open(zipprocessor._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with open(zipprocessor._full_filename(filename), "w") as file:
                file.write(contents)

if __name__ == "__main__":
    zipreplace = ZipReplace(*sys.argv[2:4])
    ZipProcessor(sys.argv[1], zipreplace).process_zip()
