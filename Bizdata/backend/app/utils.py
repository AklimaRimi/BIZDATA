from cv2 import rotate
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import pandas as pd
import numpy as np

def get_image():
    buffer = BytesIO()
    plt.savefig(buffer,format = 'png',dpi = 60)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph= base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    
    buffer.close()
    return graph
    
    

def get_plot(*args, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize = (20,10))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    
    

    sns.set_palette(sns.color_palette('pastel'))
    plt.title(f'Barplot' )
    data.plot(kind='bar')
    plt.legend(loc='lower left')
    plt.xticks(rotation = 10)

        

    graph = get_image()
    return graph
        
        
    
    