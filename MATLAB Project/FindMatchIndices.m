%% Find Match Indices
% Compares two non-empty 1D arrays and returns a list of index positions from 
% array one of any values that also appear in array 2.
%
% Author: Anish Hota

% Function with input arrays a and b and output indices
function [indices] = FindMatchIndices(a, b)
% indices is [] if the if nothing matches
indices = [];
% For loop that sets the indices to the i position if a number in array a 
% appears in array b
for i = 1:length(a)
    compare = strfind(b, a(i));
    if compare > 0
        indices(i) = i;
        % removes zeroes from the array and transposes the array to 1 row
        indices = nonzeros(indices);
        indices = indices';
    end
end
