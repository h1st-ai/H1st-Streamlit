import h1st.core as h1
from app.ai.models.fuzzy_tip_calculator import FuzzyTipCalculator


class TipCalculatorWorkflow(h1.Graph):
    def __init__(self):
        super().__init__()

        self.start()
        self.add(FuzzyTipCalculator())
        self.end()

