import numpy as np
import h1st.core as h1

class FuzzyTipCalculator(h1.FuzzyLogicModel):
    def add_variables(self):
        """
        Add fuzzy variables with membership functions
        """
        self.add_variable(
            range_=np.arange(0, 10, 0.1),
            name='food_quality',
            membership_funcs=[('poor', 'triangle', [0, 0, 4]), # triangle (p1, p2, p3)
                              ('fair', 'gaussian', [3.5, 1]), # gaussian (mean, vairance)
                              ('good', 'gaussian', [6.5, 1]),                              
                              ('excellent', 'triangle', [6, 10, 10])
                             ],
            type_='antecedent'
        )
        self.add_variable(
            range_=np.arange(0, 10, 0.1),
            name='service_quality',
            membership_funcs=[('poor', 'triangle', [0, 0, 3]),
                              ('good', 'trapezoid', [2, 4, 6, 8]),# (p1, p2, p3, p4)
                              ('excellent', 'triangle', [7, 10, 10]),
                             ],
            type_='antecedent'
        )
        self.add_variable(
            range_=np.arange(0, 25, 0.1),
            name='tip_percent',
            membership_funcs=[('low', 'triangle', [0, 0, 10]),
                              ('medium', 'triangle', [5, 12.5, 20]),
                              ('high', 'triangle', [15, 25, 25])],
            type_='consequent'
        )

    def add_rules(self):
        """
        Add fuzzy rules here. Place antecedent type variables in 'if' statement
        and place consequent type varibles in 'then' statement.
        """
        vars = self.variables
        self.add_rule(
            'rule1',
            if_=vars['food_quality']['poor'] & vars['service_quality']['poor'], 
            then_=vars['tip_percent']['low'])
        self.add_rule(
            'rule2',
            if_=vars['food_quality']['poor'] & vars['service_quality']['good'],
            then_=vars['tip_percent']['medium'])
        self.add_rule(
            'rule3',
            if_=(vars['food_quality']['fair']|vars['food_quality']['good']) & vars['service_quality']['poor'],
            then_=vars['tip_percent']['medium'])
        self.add_rule(
            'rule4',
            if_=vars['food_quality']['poor'] & vars['service_quality']['excellent'],
            then_=vars['tip_percent']['medium'])        
        self.add_rule(
            'rule5',
            if_=vars['food_quality']['good'] & vars['service_quality']['good'],
            then_=vars['tip_percent']['medium'])
        self.add_rule(
            'rule6',
            if_=vars['food_quality']['excellent'] & vars['service_quality']['good'],
            then_=vars['tip_percent']['high'])        
        self.add_rule(
            'rule7',
            if_=vars['service_quality']['excellent'],
            then_=vars['tip_percent']['high'])        