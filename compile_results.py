import math
import sys

from PIL import Image, ImageDraw, ImageFont


def main(num_images, margin, img_padding):
    K = [ 2, 4, 8, 16, 32 ]
    text_font = ImageFont.truetype('assets/fonts/Inter-Light.ttf', 16)

    for i in range(1, num_images + 1):
        base_image = Image.open('test_images/{}.png'.format(i))
        img_width, img_height = base_image.size

        compiled_img_width = (2 * margin) + (5 * img_padding) + (6 * img_width)
        compiled_img_height = ((2 * margin)
                               + img_height
                               + math.floor(img_height * 0.18))
        compiled_img_size = tuple([ compiled_img_width, compiled_img_height ])
        compiled_img_bg_colour = tuple([255] * 4)
        compiled_img = Image.new('RGBA',
                                 compiled_img_size,
                                 compiled_img_bg_colour)
        compiled_img_d = ImageDraw.Draw(compiled_img)

        base_img_text = 'Base Image'
        base_img_text_size = compiled_img_d.textsize(base_img_text,
                                                     font=text_font)
        base_img_text_width, base_img_text_height = base_img_text_size
        base_img_text_x = (margin
                           + (img_width// 2)
                           - (base_img_text_width // 2))
        base_img_text_y = (margin + img_height
                           + ((margin + math.floor(img_height * 0.18)) // 2)
                           - (base_img_text_height // 2))
        compiled_img_d.text((base_img_text_x, base_img_text_y ),
                            base_img_text,
                            fill='black',
                            font=text_font)

        compiled_img.paste(base_image, (margin, margin))

        result_idx = 0
        result_start_x = margin + img_width + img_padding
        for k in K:
            result_img = Image.open('test_results/{}-{}.png'.format(i, k))
            result_img_x = (result_start_x
                            + ((img_width + img_padding) * result_idx))
            compiled_img.paste(result_img, (result_img_x, margin))

            result_text = 'k = {}'.format(k)
            result_text_size = compiled_img_d.textsize(result_text,
                                                       font=text_font)
            result_text_width, result_text_height = result_text_size
            result_text_x = (result_img_x
                             + (img_width// 2)
                             - (result_text_width // 2))
            result_text_y = (margin
                             + img_height
                             + ((margin + math.floor(img_height * 0.18)) // 2)
                             - (result_text_height // 2))
            compiled_img_d.text((result_text_x, result_text_y),
                                result_text,
                                fill='black',
                                font=text_font)

            result_idx += 1

        compiled_img.save('test_results/compilations/{}.png'.format(i))



if __name__ == '__main__':
    argument_list = list(map(int, sys.argv[1:]))
    if len(argument_list) != 3:
        print('Usage: compile_results.py <number of images> <margin> '
              + '<image padding size>')
        sys.exit(-1)

    num_images = argument_list[0]
    margin = argument_list[1]
    img_padding = argument_list[2]
    main(num_images, margin, img_padding)
