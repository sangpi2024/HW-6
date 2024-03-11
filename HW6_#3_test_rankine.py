from rankine import Rankine

# Parameters for the first cycle
p_high = 8000 * 1e3  # convert kPa to Pa
p_low = 8 * 1e3  # convert kPa to Pa
x1 = 1  # Saturated vapor

# Create a Rankine cycle instance
rankine_cycle_1 = Rankine(p_high=p_high, p_low=p_low, x1=x1)

# Calculate

Now, let's implement the `calculate_efficiency` method in our `Rankine` class, which calculates the efficiency based on the cycle's parameters using thermodynamic equations and steam table data.

For the efficiency calculation, we would need to determine the enthalpy at various points in the cycle:
- **Point 1**: Steam entering the turbine
- **Point 2**: Steam leaving the turbine
- **Point 3**: Liquid leaving the condenser
- **Point 4**: Liquid entering the boiler

However, as this involves complex thermodynamic calculations and we are not using the actual steam-stem.py file that has been provided for the course, the code below will illustrate what the method would look like, but cannot provide accurate calculations without the correct data or the `CoolProp` library.

```python
def calculate_efficiency(self):
    """
    Calculates the efficiency of the Rankine cycle.
    """
    # We assume here that the steam tables or CoolProp library is used to find enthalpies (h) and entropies (s)
    # CoolProp can be used like: CP.PropsSI('H', 'P', pressure, 'Q', quality, 'Water')
    # where 'H' is for enthalpy, 'P' for pressure, 'Q' for quality (0-1 for liquid-vapor phase), 'Water' for the fluid

    # For point 1: High pressure, x = 1 (saturated vapor) or superheated
    if self.x1 is not None:
        h1 = CP.PropsSI('H', 'P', self.p_high, 'Q', self.x1, 'Water')  # Saturated vapor
        s1 = CP.PropsSI('S', 'P', self.p_high, 'Q', self.x1, 'Water')
    else:
        h1 = CP.PropsSI('H', 'P', self.p_high, 'T', self.T_superheat, 'Water')  # Superheated
        s1 = CP.PropsSI('S', 'P', self.p_high, 'T', self.T_superheat, 'Water')

    # For point 2: Low pressure, isentropic expansion
    s2 = s1  # Isentropic: entropy remains constant
    h2 = CP.PropsSI('H', 'P', self.p_low, 'S', s2, 'Water')

    # For point 3: Low pressure, saturated liquid
    h3 = CP.PropsSI('H', 'P', self.p_low, 'Q', 0, 'Water')  # Saturated liquid

    # For point 4: Isentropic compression, back to high pressure
    s4 = CP.PropsSI('S', 'P', self.p_low, 'Q', 0, 'Water')
    h4 = CP.PropsSI('H', 'P', self.p_high, 'S', s4, 'Water')

    # Work done by the turbine and work required by the pump
    w_turbine = h1 - h2
    w_pump = h4 - h3

    # Heat added in the boiler
    q_in = h1 - h4

    # Thermal efficiency
    efficiency = (w_turbine - w_pump) / q_in
    return efficiency
