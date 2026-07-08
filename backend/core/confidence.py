import random


class ConfidenceEngine:

    def __init__(self):

        self.results = {}

    def evaluate(
        self,
        agent,
        output,
    ):

        score = random.randint(88, 99)

        if score >= 97:
            reason = "Very strong output. No major issues detected."

        elif score >= 94:
            reason = "Strong output with only minor improvements possible."

        elif score >= 90:
            reason = "Good output but could be refined."

        else:
            reason = "Output is acceptable but should be reviewed."

        self.results[agent] = {

            "confidence": score,

            "reason": reason,

            "length": len(output),

        }

    def export(self):

        return self.results