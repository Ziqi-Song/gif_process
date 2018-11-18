#-*- coding: UTF-8 -*-

import imageio

def create_gif(image_list, gif_name):

    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)

    return

def main():
    image_list = ['1-0.png', '1-1.png', '1-2.png',
                  '1-3.png', '1-4.png', '1-5.png',
                  '1-6.png', '1-7.png', '1-8.png',
                  '1-9.png', '1-10.png', '1-11.png',
                  '1-12.png', '1-13.png']
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)

if __name__ == "__main__":
    main()