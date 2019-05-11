import subprocess
import sys
import time

def check_running_processes(running_processes):
    new_running_processes = list()
    for p in running_processes:
        if p.poll() is None:
            new_running_processes.append(p)

    return new_running_processes


def main(output_dir, start_image_index, num_images,
         num_allowed_processes, interpreter_exec_cmd):
    K = [ 2, 4, 8, 16, 32 ]  # Arbitrary choices.
    max_iters = 15           # Uhm, arbitary choice also. Haha.

    end_image_index = start_image_index + num_images
    running_processes = list()
    for img_num in range(start_image_index, end_image_index):
        input_filename = 'test_images/{}.png'.format(img_num)
        for k in K:
            # Don't fork additional subprocesses until the number of running
            # processes is less than the number of allowed running processes.
            running_processes = check_running_processes(running_processes)
            while len(running_processes) >= num_allowed_processes:
                time.sleep(5)
                running_processes = check_running_processes(running_processes)
            
            output_filename = '{}/{}-{}.png'.format(output_dir, img_num, k)
            command = [
                *interpreter_exec_cmd, '-W', 'main.m',
                input_filename, output_filename, str(k), str(max_iters)
            ]
            process = subprocess.Popen(command)
            process.wait()
            running_processes.append(process)


if __name__ == '__main__':
    argument_list = sys.argv[1:]
    if len(argument_list) < 4:
        print('Usage: start_tests.py <output directory> <start image index> '
              + '<number of images> <number of allowed processes> '
              + '<interpreter_exec_cmd')

    output_dir = argument_list[0]
    start_image_index = int(argument_list[1])
    num_images = int(argument_list[2])
    num_allowed_processes = int(argument_list[3])
    interpreter_exec_cmd = argument_list[4:]
    main(output_dir, start_image_index, num_images,
         num_allowed_processes, interpreter_exec_cmd)
