function idx = findClosestCentroids(X, centroids)
  K = size(centroids, 1);

  % You need to return the following variables correctly.
  idx = zeros(size(X,1), 1);
  num_i = size(X, 1);

  for i = 1:num_i
    x = X(i, :);
    shortest_distance = Inf;
    for k = 1:K
      centroid = centroids(k, :);
      distance = sqrt(sum(bsxfun(@minus, x, centroid) .^ 2));
      if distance < shortest_distance
        shortest_distance = distance;
        idx(i) = k;
      endif
    endfor
  endfor
end

