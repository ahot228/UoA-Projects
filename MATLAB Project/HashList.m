%% Hash List
% Calculates the hash31 value for every string stored in a cell array to 
% generate a sequence of hashed values (which will be integers).
%
% Author: Anish Hota

% function with input cellarray and output numarray
function numarray = HashList(cellarray)
%converts the cell array into a string array
stringarray = string(cellarray);
% uses the Hash31 function to convert the values in the cell array
for i = 1:length(stringarray)
    numarray(i) = Hash31(char(stringarray(i)));
end