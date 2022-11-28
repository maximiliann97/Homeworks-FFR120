clear all
close all
clc

% average_1 = [54.2 278.2 661.2 769.2 869.4 894 918.8 957.6 960.8];
% Gamma = [0.01, 0.02];
% Beta = linspace(0.1, 0.9, 9);
% 
% beta_gamma_1 = Beta/Gamma(1);
% beta_gamma_2 = Beta/Gamma(2);
% average_1 = reshape(average_1, [3, 3]);
% average_2 = reshape(average_2, [3 3]);
% 
% imagesc([Beta(1), Beta(end)], [beta_gamma_1(1), beta_gamma_1(end)], average_1')
% colorbar
% xlabel('\beta')
% ylabel('\beta / \gamma')
% title('R_\infty as a function of \beta and \beta / \gamma')
% set(gca,'YDir','normal')


average_1 = [10  16  91 169 339 447 712 691 877 872 878 899 911 965 962 963 949 961 955 960];
average_2 = [10  21  20  46  65  66  97  59 172 287 387 353 466 447 473 589 423 580 488 534];

Gamma = [0.01, 0.02];
Beta = linspace(0, 1, 20);

beta_gamma_1 = Beta/Gamma(1);
beta_gamma_2 = Beta/Gamma(2);
average_1 = reshape(average_1, [4, 5]);

imagesc([Beta(1), Beta(end)], [beta_gamma_1(1), beta_gamma_1(end)], average_1')
colorbar
xlabel('\beta')
ylabel('\beta / \gamma')
title('R_\infty as a function of \beta and \beta / \gamma')
set(gca,'YDir','normal')