import os
import shutil
import subprocess
from pathlib import Path

def _make_directory(foldername):
    directory = os.path.join(Path.cwd(), foldername)
    print('Making directory: "%s"...'%directory, end='')
    if os.path.exists(directory):
        input('\n***Delete folder: "%s"?*** (enter to continue)'%directory)
        shutil.rmtree(directory)
        os.makedirs(directory)
    else:
        os.makedirs(directory)
    print('done.')
    return directory

def _call_ffmpeg(cmd_list):
    # Additional details here:
    # https://github.com/thevangelist/FFMPEG-gif-script-for-bash
    # http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html
    for cmd in cmd_list:
        try:
            with open(Path.cwd() / 'conversion_messages.txt', 'wt') as f:
                f.write('So far, everthing is fine...\n')
                f.flush()
                subprocess.check_call(cmd, stderr=f, stdout=f)
                f.flush()
            (Path.cwd() / 'conversion_messages.txt').unlink()
        except: # This is unlikely to be platform independent :D
            print('ffmpeg command failed. Is ffmpeg installed?')
            raise
    if os.path.exists(Path.cwd() / 'palette.png'): # delete palette file
        os.remove(Path.cwd() / 'palette.png')
    return None

def video_to_gif(video, fps, scale, output='output.gif'):
    # Set fps and scale:
    s = 2 / scale
    filters = ('fps=' + str(fps) +
               ', scale=trunc(iw/%s)*2:trunc(ih/%s)*2:flags=lanczos'%(s, s))
    # Scan video for color subset and make 'palette.png'
    print('Converting video to gif...', end='')
    cmd1 = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-i', Path.cwd() / video,               # input video file
        '-vf', filters + ',palettegen',         # generate palette with filter
        Path.cwd() / 'palette.png'              # output palette
        ]
    cmd2 = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-i', Path.cwd() / video,               # input video file
        '-i', Path.cwd() / 'palette.png',       # input palette file
        '-lavfi', filters + ' [x]; [x][1:v] paletteuse',
        '-y', Path.cwd() / output               # output gif
        ]
    _call_ffmpeg(cmd_list=[cmd1, cmd2])
    print('done.')
    return None

def video_to_images(video, fps, px, folder='images'):
    d = _make_directory(folder)
    print('Extracting images...', end='')
    cmd = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-i', Path.cwd() / video,               # input video file
        '-f', 'image2',                         # force file format to 'image2'
        '-r', str(fps),                         # output fps
        '-s', px,                               # WxH output size in pixels
        os.path.join(d, 'img%06d.png')          # output images
        ]
    _call_ffmpeg(cmd_list=[cmd])
    print('done.')
    return None

def images_to_avi(folder, start, stop, fps, px, output='output.avi'):
    d = os.path.join(Path.cwd(), folder)
    print('Converting images to "%s"...'%output, end='')
    cmd = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-f', 'image2',                         # force file format to 'image2'
        '-framerate', str(fps),                 # set framerate
        '-start_number', str(start),            # start frame
        '-i', os.path.join(d, 'img%06d.png'),   # input images
        '-vframes', str(stop - start),          # number of frames
        '-s', px,                               # WxH output size in pixels
        os.path.join(Path.cwd(), output)        # output video
        ]
    _call_ffmpeg(cmd_list=[cmd])
    print('done.')
    return None

def images_to_mp4(folder, start, stop, fps, scale, output='output.mp4'):
    d = os.path.join(Path.cwd(), folder)
    # Set scale:
    s = 2 / scale
    scale_string = 'scale=trunc(iw/%s)*2:trunc(ih/%s)*2'%(s, s)
    print('Converting images to "%s"...'%output, end='')
    cmd = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-f', 'image2',                         # force file format to 'image2'
        '-r', str(fps),                         # set framerate
        '-start_number', str(start),            # start frame
        '-i', os.path.join(d, 'img%06d.png'),   # input images
        '-vframes', str(stop - start),          # number of frames
        '-movflags', 'faststart',               # internet optimisation...(?)
        '-pix_fmt', 'yuv420p',                  # cross browser compatibility
        '-vcodec', 'libx264',                   # codec choice
        '-vf', scale_string,                    # even pixel number (important)
        '-preset', 'veryslow',                  # take time and compress to max
        '-crf', '25',                           # image quality vs file size
        os.path.join(Path.cwd(), output)        # output video
        ]
    _call_ffmpeg(cmd_list=[cmd])
    print('done.')
    return None

def images_to_gif(folder, start, stop, fps, scale, output='output.gif'):
    d = os.path.join(Path.cwd(), folder)
    # Set scale:
    s = 2 / scale
    filters = 'scale=trunc(iw/%s)*2:trunc(ih/%s)*2:flags=lanczos'%(s, s)
    # Scan images for color subset and make 'palette.png'
    print('Converting images to "%s"...'%output, end='')
    cmd1 = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-f', 'image2',                         # force file format to 'image2'
        '-start_number', str(start),            # start frame
        '-i', os.path.join(d, 'img%06d.png'),   # input images
        '-vframes', str(stop - start),          # number of frames
        '-vf', filters + ',palettegen',         # generate palette with filter
        Path.cwd() / 'palette.png'              # output palette
        ]
    cmd2 = [
        'ffmpeg',                               # callable ffmpeg on path
        '-y',                                   # auto overwrite files
        '-f', 'image2',                         # force file format to 'image2'
        '-framerate', str(fps),                 # set framerate
        '-start_number', str(start),            # start frame
        '-i', os.path.join(d, 'img%06d.png'),   # input images
        '-i', Path.cwd() / 'palette.png',       # input palette file
        '-vframes', str(stop - start),          # number of frames
        '-lavfi', filters + ' [x]; [x][1:v] paletteuse',
        '-y', Path.cwd() / output               # output gif
        ]
    _call_ffmpeg(cmd_list=[cmd1, cmd2])
    print('done.')
    return None

if __name__ == '__main__':
    print('ffmpeg examples using "input.mp4":')

    print('\n-> convert .mp4 to .gif:')
    video_to_gif(video='input.mp4', fps=10, scale=0.25)

    print('\n-> get images from .mp4:')
    video_to_images(video='input.mp4', fps=10, px='640x480')

    print('\n-> make videos from images:')
    images_to_avi(folder='images', start=0, stop=221, fps=10, px='640x480')
    images_to_mp4(folder='images', start=0, stop=221, fps=40, scale=0.75)
    images_to_gif(folder='images', start=10, stop=50, fps=20, scale=0.5)

    print('\n-> get images from .avi and .gif:')
    video_to_images(video='output.avi', fps=5, px='640x480', folder='img_avi')
    video_to_images(video='output.gif', fps=10, px='640x480', folder='img_gif')
