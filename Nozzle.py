# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:20:40 2020

@author: sunge
"""
import CoolProp as cp
import math

from sympy import Symbol
from sympy.solvers import solve



    def nozzle_area_ratio(self, a, a_star, gamma):
        m = Symbol('M')
        sol = solve((a / a_star) - (1 / m) * ((2 / (gamma + 1)) * (1 + (gamma - 1) / 2) * m ** 2) ** ((gamma + 1) / (2 * (gamma - 1))), m)
        print("Nozzle area ratio:",sol)
        return sol
    
    def mass_flow_rate(self, pressure, temperature,throat_area, mach_num = 1,
                       gamma = 1.4, R_prime = 8.314, M_prime = 30):
        m = Symbol('m')
        sol = solve(m - throat_area * (pressure/temperature) * (gamma/(R_prime/M_prime))**(0.5)
        * (mach_num/(1+((gamma-1)*mach_num**2)/2) ** ((gamma+1)/(2*(gamma-1)))))
        print("Mass flow rate:",sol)
        return sol
    
    def get_exit_pressure(p0,mach_num, gamma = 1.4):
        p = Symbol('p')
        sol = solve(p0/p - ((1+(gamma-1)* mach_num**2)/2) ** (gamma/(gamma-1)),m)
        print("Exit Pressure:",sol)
        return sol

    def get_thrust_from_nozzle(self, m_dot, r_cnst, temp_not, p_e, p_o, p_amb, a_e, gamma=1.4):
        thrust_from_nozzle = m_dot * math.sqrt(((2 * gamma) / (gamma - 1)) * r_cnst * temp_not * (1 - (p_e / p_o) ** ((gamma - 1) / gamma))) + (p_e - p_amb) * a_e
        return thrust_from_nozzle

