%% Fingerprint
% Takes a set of windows (in the form of a 2D array) and calculates a 
% document fingerprint using the winnowing algorithm. It will return the 
% document fingerprint as a 2D array in which each column contains a 
% winnowed value and its corresponding position.
%
% Author: Anish Hota

% function with input windowarray and output f
function f = Fingerprint(windowarray)
% sets the size of windowarray to rows and cols
[rows, cols] = size(windowarray);
% finds the min and position of the values in each row using the RightMin
% function
for i = 1:rows
    for j = 1:cols
        [m(1,i), pos(1,i)] = RightMin(windowarray(i,:));
        % adjusting the position with each row to coolerate with the
        % original array before the Window function
        pos(1,i) = pos(1,i)+i-1;
    end
end
% puts the m and pos into a single 2byn array
f = [m;pos];
% deletes any duplicates in the array
f= f';
f = unique(f, 'rows','stable');
f = f';