clear all
close all
clc

myfiles = dir("arrays\");
filenames={myfiles(:).name}';
filefolders={myfiles(:).folder}';
csvfiles=filenames(endsWith(filenames,'.csv'));
csvfolders=filefolders(endsWith(filenames,'.csv'));
files=fullfile(csvfolders,csvfiles);
values = zeros(21,10);

for i = 1:21
        f = files{i};
        ff = load(f)';
        values(i,:) = ff;
end



beta = linspace(0.1, 1, 20);
Q = linspace(10, 100, 30);


imagesc([beta(2), beta(end)], [Q(2), Q(end-2)], values)
colorbar
xlabel('\beta')
ylabel('\beta / \gamma')
title('R_\infty as a function of \beta and \beta / \gamma')
set(gca,'YDir','normal')