import matplotlib.pyplot as plt

import ffmpeg
from PIL import Image

# configurations:
config = (
    ('Nikon 40x0.95',   'AMS-AGY v1 (Snouty!)', '30deg', 'High NA'),
    ('Nikon 40x0.95',   'AMS-AGY v1 (Snouty!)', '45deg', 'Low NA'),
    ('Nikon 40x0.95',   'AMS-AGY v2 (Snouty!)', '30deg', 'High NA big field!'),
    ('Nikon 40x0.95',   'AMS-AGY v2 (Snouty!)', '45deg', 'Low NA big field!'),
    ('Nikon 40x0.95',   'AMS-AGY v2 (Snouty!)', '55deg', 'Any immersion!'),
    ('Olympus 40x0.95', 'AMS-AGY v1 (Snouty!)', '30deg', 'High NA'),
    ('Olympus 40x0.95', 'AMS-AGY v1 (Snouty!)', '45deg', 'Low NA'),
    ('Olympus 40x0.95', 'AMS-AGY v2 (Snouty!)', '30deg', 'High NA big field!'),
    ('Olympus 40x0.95', 'AMS-AGY v2 (Snouty!)', '45deg', 'Low NA big field!'),
    ('Olympus 40x0.95', 'AMS-AGY v2 (Snouty!)', '55deg', 'Any immersion!'))

# get size:
image = Image.open('images\img0.png')
print('-> image.size =', image.size)
x_px, y_px = image.size
time_points = 10

# make folder for images:
folder = 'images_plt'
directory = ffmpeg._make_directory(folder)

# make images with scale bar and text using matplotlib:
fig = plt.figure()

# set size, margins, space, max intensity and dpi:
x_inch = 6
y_inch = x_inch * y_px / x_px
xmargin, ymargin, space = 0.15, 0.64, 0.05
plt.figure(figsize=(x_inch, y_inch), dpi=300)

# loop over images adding scale bar and text:
for i in range(time_points):
    image = Image.open('images\img%i.png'%i)
    print('-> image = %i'%i)
    plt.clf()
    plt.imshow(image)
    plt.axis('off')
    plt.figtext(xmargin, ymargin + 4 * space,
                'O1 = %s'%config[i][3],
                color='yellow', family='monospace')
    plt.figtext(xmargin, ymargin + 3 * space,
                'O2 = %s'%config[i][0],
                color='blue', family='monospace')
    plt.figtext(xmargin, ymargin + 2 * space,
                'O3 = %s'%config[i][1],
                color='black', family='monospace')
    plt.figtext(xmargin, ymargin + 1 * space,
                r'$\theta$  = %s'%config[i][2],
                color='cyan', family='monospace')
    plt.savefig(folder + '/img%06i.png'%i, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# make gif:
ffmpeg.images_to_gif(folder=folder,
                     start=0,
                     stop=time_points,
                     fps=0.75,
                     scale=1,
                     output='output.gif')
