%% Strip String Function
% Strip out whitespace and other unprintable characters, plus convert all
% uppercase characters to lowercase.
%
% Author: Anish Hota

% function with output stripped and an input stringarray
function stripped = StripString (stringarray)
i=1;
% for any ascii values below 33 or higher than 126 dete from array
% otherwise continue
while i <= length(stringarray)
    if double(stringarray(i)) >= 33 && double(stringarray(i)) <= 126
        stringarray(i) = stringarray(i);
        i = i+1;
    % if there are only spaces return a 0x0 char array
    else
        stringarray(i) = '';
    end
end

% lowercase the stringarray and output stripped
stripped = lower(stringarray);
% if the array contains only special characters then return a 0x0 char
% array
if strcmp(stripped,blanks(0))==true
    stripped = '';
end