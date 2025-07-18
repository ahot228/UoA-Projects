%% K-Gram
% Take a string and divide it into a sequence of k-grams, where each 
% element is k characters long. 
%
% Author: Anish Hota

% function with input k and string and output cellarray
function cellarray = Kgram(k, string)
% set i=1
i = 1;
% if k is larger than the string then just display the string
if k > length(string)
    cellarray = {string};
end
% while loop that creates the k grams by putting the k terms into cell
% arrays
while i+(k-1) <= length(string)
    cellarray{i} = (string(i:i+(k-1)));
    i=i+1;
end