# nicerc_physics_pi
## Rewrite of the NICERC Physics Curriculum to use the Raspberry Pi device

This is a rewrite of the existing Student Materials for the [NICERC Physics Curriculum](https://nicerc.org/) to make use of the Raspberry Pi devices. Hopefully this will be useful for anyone wishing to use the NICERC Computer Science Curriculum (which uses the Raspberry Pi platform) along with the Physics Curriculum. All materials are being written in [Jupyter Notebooks](http://jupyter.org/).

### Materials needed

* [Raspberry Pi](https://www.raspberrypi.org/)
* [Pimoroni Explorer Pro HAT](https://shop.pimoroni.com/products/explorer-hat)
* [STS-PI Robot Chassis](https://shop.pimoroni.com/products/sts-pi)
* [MPU6050 Gyro/Accelerometer](https://www.amazon.com/MPU-6050-MPU6050-Accelerometer-Gyroscope-Converter/dp/B008BOPN40/ref=sr_1_2?ie=UTF8&qid=1530192890&sr=8-2&keywords=MPU6050)

### Style

My Jupyter notebooks use the [Spinzero theme](https://github.com/neilpanchal/spinzero-jupyter-theme) by Neil Panchal. This theme emulates a <a href="https://www.codecogs.com/eqnedit.php?latex=LaTeX" target="_blank"><img src="https://latex.codecogs.com/gif.latex?LaTeX" title="LaTeX" /></a> document style, and I personally find it pleasing. Other styles may result in different formatting, etc.

#### Installing Theme

If you want to use my theme, you can either clone it from Neil Panchal's github and follow the install directions there, or you can use the copy I've included under the theme directory. I have made a few small modifications to the `custom.css` file to improve mostly table handling. I would suggest installing the original theme then if desired installing my CSS file. Another option is to install the [Jupyter Themes](https://github.com/dunovank/jupyter-themes) and use those.

#### Markdown Jupyter Kernel

Notebooks with no python code use the [Markdown Jupyter Kernel](https://github.com/vatlab/markdown-kernel) to avoid sarting a new python kernel for notebooks with no code. Installation is simple and the commands are provided on the GitHub page.
 
### Setup

You need to install and conf