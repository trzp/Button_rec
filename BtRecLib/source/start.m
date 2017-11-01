function buttons = start(path1,path2,downsample)
    while 1
        try
            close all;
            im = imread(path1);
            if downsample==1
                im = im(1:2:end,1:2:end,:);
            end
            gray = rgb2gray(im);
            egs = edge(gray,'canny',0.1);    %直接从灰度提取边缘
            egs = bwareaopen(egs,30,8);   %去除面积过小的区域
            [L,num] = bwlabel(egs);      %将所有边缘标记出来
            buttons = -1*ones(num,4);
            for i=1:num
                eg = L==i;
                %brec
                c_area = sum(sum(eg));        %该边缘的面积
                n_eg = imfill(eg,'holes');    %尝试补洞
                nc_area = sum(sum(n_eg))  ;   %新的面积
                if nc_area>c_area             %说明能够补洞，该边缘为封闭边缘
                    r = regionprops_tjs(eg); 
                    Centroid = r(1:2);
                    MajorAxisLength = r(3);
                    MinorAxisLength = r(4);
                    BoundingBox = r(5:8);
                    if MajorAxisLength/MinorAxisLength<1.3 %方形
                        buttons(i,:) = [Centroid,BoundingBox(3:4)];
                    end
                end
            end
            buttons = buttons(buttons(:,1)>0,:);
            if downsample==1
                buttons = buttons.*2;
            end
            
            for ii=1:20
                try
                    save(path2,'buttons');
                    break;
                catch
                    pause(0.005);
                end
            end
            
        catch 
        end
    end
end


