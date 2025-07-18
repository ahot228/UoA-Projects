% pseudocode is something resembling coding steps in a non-specific language

% clear the workspace
clear

% get coordinates of two points from user
x1 = input('Enter x coordinate of point 1: ');
y1 = input('Enter y coordinate of point 1: ');
x2 = input('Enter x coordinate of point 2: ');
y2 = input('Enter y coordinate of point 2: ');

% call function to calculate distance
dist = func_distance(x1, y1, x2, y2);

% display distance to user
disp('Distance: ')
disp(dist)