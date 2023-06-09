# Mandelbrot Set Explorer

This program allows you to explore the Mandelbrot set and generate interactive visualizations using Jupyter Notebook. The Mandelbrot set is a famous fractal that exhibits intricate and infinitely complex patterns.

![3](https://github.com/secnnet/Mandelbrot-Explorer/assets/17622687/680241fa-91bc-4e01-b149-bc76eeabfd6b)

## Installation

To run this program, you need to have the following dependencies installed:

- NumPy
- Matplotlib
- ipywidgets
- IPython

You can install these dependencies using pip:
`pip install numpy matplotlib ipywidgets IPython`

## Usage

1. Open Jupyter Notebook or JupyterLab.
2. Create a new notebook or open an existing one.
3. Copy and paste the provided code into a code cell.
4. Run the code cell to generate the interactive widget.
5. Adjust the sliders and dropdowns to explore different regions and color options of the Mandelbrot set.
6. The rendered image will be displayed below the interactive widget.

## Customization

The provided code offers several options for customization:

- Adjust the `xmin`, `xmax`, `ymin`, and `ymax` sliders to change the range of the complex plane to explore.
- Modify the `width` and `height` sliders to adjust the resolution of the generated image.
- Use the `max_iter` slider to control the maximum number of iterations for computing the escape time of each point in the fractal.
- Select different colors for the fractal using the `color1` to `color5` dropdowns.
- The resulting image will be displayed with the specified colormap.

Feel free to experiment with different parameter values to create unique visualizations of the Mandelbrot set.

## License

This repository is licensed under the [MIT License](LICENSE).
