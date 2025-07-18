%% Similarity Score
% Calculates a similarity score by taking a list of matched positions for a 
% string and determining what proportion of characters in a string matched
%
% Author: Anish Hota

% function with input positions, k and tstring and output score
function score = SimilarityScore(positions, k, tstring)
%sets the variable similar to an array of 'tstring' zeros
similar = zeros(1, tstring);
% for every position in positions it creates a 1 in similar k times so the
% end result for similar will be 1s and 0s
for i = 1:length(positions)
    similar(positions(i):positions(i)+(k-1)) = 1;
end
% removes the zeroes from similar then finds the proportion of the length
% of similar to the tstring length
similar = nonzeros(similar);
score = length(similar)./tstring;
