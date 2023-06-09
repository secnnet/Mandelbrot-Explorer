import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from ipywidgets import interact, FloatSlider, IntSlider, Dropdown, IntProgress
from IPython.display import display
import time

def mandelbrot(c, max_iter):
    """
    Compute the escape time for a given point c in the complex plane.
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n - np.log(np.log2(abs(z)))
        z = z * z + c
    return max_iter


def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, progress, color):
    """
    Draw the Mandelbrot set within the specified range and resolution.
    """
    # Generate arrays of x and y values
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    result = np.zeros((height, width))

    for i in range(len(r2)):
        for j in range(len(r1)):
            # Compute the escape time for each point
            result[i, j] = mandelbrot(complex(r1[j], r2[i]), max_iter)
        progress.value += 1
        time.sleep(0.01)

    return r1, r2, result


def create_picture(xmin=-2.0, xmax=1.0, ymin=-1.5, ymax=1.5, width=1000, height=1000, max_iter=256, color1="black", color2="blue", color3="lightblue", color4="white", color5="red", color="green"):
    """
    Create and display the Mandelbrot set picture with interactive widgets.
    """
    # Create a colormap from the specified colors
    colors = [color1, color2, color3, color4, color5, color]
    cmap = LinearSegmentedColormap.from_list("mycmap", colors)

    # Create a progress bar widget
    progress = IntProgress(min=0, max=height, value=0, description="Rendering:")
    display(progress)

    # Draw the Mandelbrot set
    d = draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, progress, color)
    
    # Display the image
    img = plt.imshow(d[2], extent=(xmin, xmax, ymin, ymax), cmap=cmap, interpolation='bilinear')
    img.set_clim(0, max_iter)
    plt.title('Mandelbrot Set')
    plt.axis('off')
    plt.show()


# Define the available color options
color_options = ["black", "blue", "lightblue", "white", "red", "green", "yellow", "orange", "purple", "pink", "gray"]

# Create the interactive widget using the interact function
interact(create_picture,
         xmin=FloatSlider(min=-2.5, max=1.5, step=0.1, value=-2.0),
         xmax=FloatSlider(min=-2.5, max=1.5, step=0.1, value=1.0),
         ymin=FloatSlider(min=-2.5, max=1.5, step=0.1, value=-1.5),
         ymax=FloatSlider(min=-2.5, max=1.5, step=0.1, value=1.5),
         width=IntSlider(min=100, max=2000, step=100, value=1000),
         height=IntSlider(min=100, max=2000, step=100, value=1000),
         max_iter=IntSlider(min=50, max=1000, step=50, value=256),
         color1=Dropdown(options=color_options, value="black"),
         color2=Dropdown(options=color_options, value="blue"),
         color3=Dropdown(options=color_options, value="lightblue"),
         color4=Dropdown(options=color_options, value="white"),
         color5=Dropdown(options=color_options, value="red"),
         color=Dropdown(options=color_options, value="green"))
