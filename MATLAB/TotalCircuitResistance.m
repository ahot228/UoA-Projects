function RTotal = TotalCircuitResistance(R1,R2,R3)
% TotalCircuitResistance calculates the total resistance of a component of
% an electrical circuit that consists of two resistors in parallel (R1 and
% R2) connected to a third resistor in series (R3).
% 
% Author: George Ohm

RTotal = R1 * R2 / (R1 + R2) + R3;

end

