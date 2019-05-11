import subprocess
import sys

def main(output_dir, start_image_index, num_images, interpreter_exec_cmd):
    K = [ 2, 4, 8, 16, 32 ]  # Arbitrary choices.
    max_iters = 15           # Uhm, arbitary choice also. Haha.

    end_image_index = start_image_index + num_images
    for img_num in range(start_image_index, end_image_index):
        input_filename = 'test_images/{}.png'.format(img_num)
        for k in K:
            output_filename = '{}/{}-{}.png'.format(output_dir, img_num, k)
            command = [
                *interpreter_exec_cmd, '-W', 'main.m',
                input_filename, output_filename, str(k), str(max_iters)
            ]
            subprocess.run(command)


if __name__ == '__main__':
    argument_list = sys.argv[1:]
    if len(argument_list) < 4:
        print('Usage: start_tests.py <input image filename> <output directory>'
              + ' <start image index> <num_images>')

    output_dir = argument_list[0]
    start_image_index = int(argument_list[1])
    num_images = int(argument_list[2])
    interpreter_exec_cmd = argument_list[3:]
    main(output_dir, start_image_index, num_images, interpreter_exec_cmd)
