%% Find Match Positions
% Compare two fingerprints and determines which positions in fingerprint 1 
% have a value that is also found in string 2 and which positions in 
% fingerprint 2 have a value that is also found in string 1.
%
% Author: Anish Hota

% function with inputs f1 and f2 and outputs p1 and p2
function [p1,p2] = FindMatchPositions(f1,f2)
% determines the rows an cols as the sizes of f1 and f2
[rows1, cols1] = size(f1);
[rows2, cols2] = size(f2);
% uses the FindMatchIndicies function to compare the two hash values in f1
% and f2 and then show p1 as the subsequent position values.
for i = 1:rows1
    for j= 1: cols1
        match1 = FindMatchIndices(f1(1,:),f2(1,:));
        p1 = f1(2,match1);
        % if there are no matches p1 = []
        if isempty(match1)
            p1 = [];
        end
    end
end
% For loop replicates the above for loop but compares it the other way
% around
for k = 1:rows2
    for l = 1:cols2
        match2 = FindMatchIndices(f2(1,:),f1(1,:));
        p2 = f2(2,match2);
        if isempty(match1)
            p2 = [];
        end
    end
end