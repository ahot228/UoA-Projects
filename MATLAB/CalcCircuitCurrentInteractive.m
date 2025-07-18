% Calulates the total resitance and total current in the circuit with given
% user input values
% Author: Anish Hota

% Clears workspace
clear

% Allows user to input values for R1, R2, R3 and V
R1 = input('R1 resistor value: ');
R2 = input('R2 resistor value: ');
R3 = input('R3 resistor value: ');
V = input('Voltage value: ');

%  Reference to total resitance function
RTotal = TotalCircuitResistance(R1, R2, R3);

% Equation for current using ohms law
I = V / RTotal;

% Displaying values for total resistance and current
disp('Total Resitance (in ohms): ')
disp(RTotal)
disp('Current (in amps): ')
disp(I)
