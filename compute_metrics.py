import os

from PIL import Image
import numpy as np
import sewar


def main():
    K = [ 2, 4, 8, 16, 32 ]
    num_images = 15

    with open('test_results/metric_results.csv', 'w') as metric_results_f:
        metric_results_header = [ 'Result ID', 'PSNR', 'Compression Ratio' ]
        metric_results_f.write('{}\n'.format(','.join(metric_results_header)))
        for i in range(1, num_images + 1):
            base_image_filename = 'test_images/{}.png'.format(i)
            base_image = np.asarray(
                Image.open(base_image_filename).convert('RGBA')
            )
            base_image_size = os.stat(base_image_filename).st_size
            for k in K:
                result_id = '{}-{}'.format(i, k)
                new_image_filename = 'test_results/{}.png'.format(result_id)
                new_image = np.asarray(
                    Image.open(new_image_filename).convert('RGBA')
                )
                new_image_size = os.stat(new_image_filename).st_size

                psnr = sewar.full_ref.psnr(base_image, new_image)
                compression_ratio = base_image_size / new_image_size
                result = '{},{},{}\n'.format(
                    result_id,
                    psnr,
                    compression_ratio
                )
                metric_results_f.write(result)


if __name__ == '__main__':
    main()