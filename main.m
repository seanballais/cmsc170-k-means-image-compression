%% Iniialize parameter values.
arg_list = argv();
input_image_filename = arg_list(1){1};
output_image_filename = arg_list(2){1};
K = str2num(arg_list(3){1});
max_iters = str2num(arg_list(4){1});

%% Apply K-means to compress the image.
A = double(imread(input_image_filename));
A = A / 255; % Put the pixel values into the range [0 - 1].
img_size = size(A);

% Reshape the image into an Nx3 matrix where N = number of pixels.
% Each row will contain the Red, Green and Blue pixel values
% This gives us our dataset matrix X that we will use K-Means on.
X = reshape(A, img_size(1) * img_size(2), 3);

initial_centroids = kMeansInitCentroids(X, K);
[centroids, idx] = runkMeans(X, initial_centroids, max_iters);

% Recover compressed image.
X_recovered = centroids(idx, :);
X_recovered = reshape(X_recovered, img_size(1), img_size(2), 3);

imwrite(X_recovered, output_image_filename);
