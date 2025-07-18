%% Window
%Takes a sequence of integer values and creates a 2D array of windows for a 
% specified window size w.
%
% Author: Anish Hota

% function with input w and array and output windowarray
function windowarray = Window(w, array)
% if the width w is larger than array then return the array
if w > length(array)
    windowarray = array;
end
% nested for loop that creates a window with an indent of newline and size
% length(array)-w+1 and w
for i = 1:(length(array)-w+1)
    for j = 1:w
        newline = i+j-1;
        windowarray(i,j) = array(newline);
    end
end