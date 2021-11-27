import cv2
import os


def logging_(msg, path='./failed.log'):
    with open(path, 'a') as f:
        f.write(msg)


def save_img():
    video_path = './bad_apple.mp4'
    vc = cv2.VideoCapture(video_path)
    c = 0
    rval = vc.isOpened()

    while rval:
        c = c + 1
        rval, frame = vc.read()
        pic_path = './bad_apple_imgs'
        if rval:
            cv2.imwrite(f'{pic_path}/{c}.png', frame)
            print(f'frame {c} success.')
            cv2.waitKey(1)
        else:
            logging_(f'frame {c} failed\n')
            break
    vc.release()
    print('------ save_success ------')


save_img()
