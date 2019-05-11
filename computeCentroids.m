function centroids = computeCentroids(X, idx, K)
    [m n] = size(X);
    centroids = zeros(K, n);
    for k = 1:K
      examples = X(find(idx == k), :);
      num_examples = size(examples, 1);
      centroids(k, :) = sum(examples) ./ num_examples;
    endfor
end

