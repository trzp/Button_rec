function result = regionprops_tjs(bw)
    [r,c] = find(bw>0);
    list = [c,r];
    Centroid = mean(list,1);
    
    xbar = Centroid(1);
    ybar = Centroid(2);
    x = list(:,1) - xbar;
    y = -(list(:,2) - ybar); 
    N = length(x);

    % Calculate normalized second central moments for the region. 1/12 is
    % the normalized second central moment of a pixel with unit length.
    uxx = sum(x.^2)/N + 1/12;
    uyy = sum(y.^2)/N + 1/12;
    uxy = sum(x.*y)/N;

    % Calculate major axis length, minor axis length, and eccentricity.
    common = sqrt((uxx - uyy)^2 + 4*uxy^2);
    MajorAxisLength = 2*sqrt(2)*sqrt(uxx + uyy + common);
    MinorAxisLength = 2*sqrt(2)*sqrt(uxx + uyy - common);

    min_corner = min(list,[],1) - 0.5;
    max_corner = max(list,[],1) + 0.5;
    BoundingBox = [min_corner (max_corner - min_corner)];
    result = [Centroid,MajorAxisLength,MinorAxisLength,BoundingBox];