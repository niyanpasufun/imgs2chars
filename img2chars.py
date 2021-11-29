import os
import cv2

# char_string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
char_string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;: "
char_string = char_string.split(',')
char_string.reverse()
char_string = ''.join(char_string)


def rgb2char(r, g, b):
    length = len(char_string)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # section width of every char
    unit = (256.0 + 1) / length

    # map gray to index of 'char_string'
    idx = int(gray / unit)
    return char_string[idx]


def img_scale(scale, img_path):
    img = cv2.imread(img_path)
    img_shape = img.shape

    height, width, mode = img_shape

    target = cv2.resize(img, (int(width / scale*1.9), int(height / scale / 1.2)))

    return target


def img2chars(img, to_path):
    txt = ''
    height, width, mode = img.shape
    # get a tuple with pixel value, and map every pixel to one of chars
    for i in range(height):
        line = ''
        for j in range(width):
            line += rgb2char(img[i][j][0], img[i][j][1], img[i][j][2])
        txt = txt + line + '\n'

    # save it as a txt file
    with open(to_path, 'w', encoding='utf-8') as f:
        f.write(txt)


if __name__ == '__main__':
    src_dir = './bad_apple_imgs'
    dest_dir = './bad_apple_chars'
    frames_files = os.listdir(src_dir)
    frames_files.sort(key=lambda x: int(x.replace('.png', '')))
    for file in frames_files:
        frame_num = file.replace(".png", '')
        img = img_scale(5, f'{src_dir}/{file}')
        img2chars(img, f'{dest_dir}/{frame_num}.txt')
        print(f'{file} success.')
