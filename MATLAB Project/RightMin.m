%% Right Min function
% Finds the value and position of the rightmost minimum in an array of values
%
% Author: Anish Hota

% function with the input array and output m and pos
function [m, pos] = RightMin(array)
% shows m the minimum value of the array
m = min(array);
% then gets the last values in the array that equals m as the position(pos)
pos = find(array==m, 1, 'last');