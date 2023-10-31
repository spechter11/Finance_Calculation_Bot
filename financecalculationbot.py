import math

#Finance Midterm Formulas in Python

class FinanceCalculations:
    def __init__(self):
        pass

    def present_value_single_cashflow(self, future_value, nominal_rate, time, compounding_frequency=1):
        """
        Calculate the present value of a single cash flow with variable compounding.
        
        Parameters:
        - future_value (float): The future value of the cash flow
        - nominal_rate (float): The annual interest rate (as a decimal)
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The present value
        """
        if future_value < 0 or nominal_rate < 0 or time < 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be non-negative and compounding_frequency should be greater than 0"
        
        return future_value / (1 + nominal_rate / compounding_frequency) ** (time * compounding_frequency)

    # Future Value Single Cash Flow
    def future_value_single_cashflow(self, present_value, nominal_rate, time, compounding_frequency=1):
        """
        Calculate the future value of a single cash flow with variable compounding.
        
        Parameters:
        - present_value (float): The present value of the cash flow
        - nominal_rate (float): The annual interest rate (as a decimal)
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The future value
        """
        if present_value < 0 or nominal_rate < 0 or time < 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be non-negative and compounding_frequency should be greater than 0"
        
        return present_value * (1 + nominal_rate / compounding_frequency) ** (time * compounding_frequency)

    # Interest Rate Single Cash Flow
    def interest_rate_single_cashflow(self, present_value, future_value, time, compounding_frequency=1):
        """
        Calculate the annual interest rate for a single cash flow with variable compounding.
        
        Parameters:
        - present_value (float): The present value of the cash flow
        - future_value (float): The future value of the cash flow
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The annual interest rate (as a decimal)
        """
        if present_value <= 0 or future_value <= 0 or time <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return ((future_value / present_value) ** (1 / (time * compounding_frequency)) - 1) * compounding_frequency


    # Number of Years Single Cash Flow
    def number_of_years_single_cashflow(self, present_value, future_value, nominal_rate, compounding_frequency=1):
        """
        Calculate the number of years for a single cash flow to reach a future value with variable compounding.
        
        Parameters:
        - present_value (float): The present value of the cash flow
        - future_value (float): The future value of the cash flow
        - nominal_rate (float): The annual interest rate (as a decimal)
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The number of years needed
        """
        if present_value <= 0 or future_value <= 0 or nominal_rate <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return (1 / compounding_frequency) * (math.log(future_value / present_value) / math.log(1 + nominal_rate / compounding_frequency))


    # Effective Annual Rate
    def effective_annual_rate(self, nominal_rate, compounding_frequency):
        """
        Calculate the effective annual rate given a nominal rate and compounding frequency.
        
        Parameters:
        - nominal_rate (float): The nominal annual interest rate (as a decimal)
        - compounding_frequency (int): Number of compounding periods per year
        
        Returns:
        float: The effective annual rate (as a decimal)
        """
        if nominal_rate < 0 or compounding_frequency <= 0:
            return "Invalid Input: Nominal rate must be non-negative and compounding_frequency should be greater than 0"
        
        return ((1 + nominal_rate / compounding_frequency) ** compounding_frequency) - 1


    # Present Value of a Perpetuity
    def present_value_perpetuity(self, annual_payment, nominal_rate):
        """
        Calculate the present value of a perpetuity.
        
        Parameters:
        - annual_payment (float): The payment received each year
        - nominal_rate (float): The annual interest rate (as a decimal)
        
        Returns:
        float: The present value of the perpetuity
        """
        if annual_payment < 0 or nominal_rate <= 0:
            return "Invalid Input: Annual payment must be non-negative and rate should be greater than 0"
        
        return annual_payment / nominal_rate

    # PV Perpetuity (Starting Today)
    def pv_perpetuity_starting_today(self, annual_payment, nominal_rate):
        """
        Calculate the present value of a perpetuity starting today.
        
        Parameters:
        - annual_payment (float): The payment received each year
        - nominal_rate (float): The annual interest rate (as a decimal)
        
        Returns:
        float: The present value of the perpetuity starting today
        """
        if annual_payment < 0 or nominal_rate <= 0:
            return "Invalid Input: Annual payment must be non-negative and rate should be greater than 0"
        
        return annual_payment/nominal_rate + annual_payment

    # Present Value of an Annuity
    def present_value_annuity(self, annual_payment, nominal_rate, time, compounding_frequency=1):
        """
        Calculate the present value of an annuity with variable compounding.
        
        Parameters:
        - annual_payment (float): The payment received each year
        - nominal_rate (float): The annual interest rate (as a decimal)
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The present value of the annuity
        """
        if annual_payment < 0 or nominal_rate <= 0 or time <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return annual_payment * ((1 - (1 / (1 + nominal_rate / compounding_frequency)) ** (time * compounding_frequency)) / (nominal_rate / compounding_frequency))

    # Cash Payment of an Annuity (Given PV)
    def cash_payment_annuity_pv(self, present_value, nominal_rate, time, compounding_frequency=1):
        """
        Calculate the cash payment of an annuity given its present value and variable compounding.
        
        Parameters:
        - present_value (float): The present value of the annuity
        - nominal_rate (float): The annual interest rate (as a decimal)
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The cash payment of the annuity
        """
        if present_value <= 0 or nominal_rate <= 0 or time <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return (present_value / (1 - (1 / (1 + nominal_rate / compounding_frequency) ** (compounding_frequency * time))) / 
                (nominal_rate / compounding_frequency))

    # Cash Payment of an Annuity (Given FV)
    def cash_payment_annuity_fv(self, future_value, nominal_rate, time, compounding_frequency=1):
        """
        Calculate the cash payment of an annuity given its future value and variable compounding.
        
        Parameters:
        - future_value (float): The future value of the annuity
        - nominal_rate (float): The annual interest rate (as a decimal)
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The cash payment of the annuity
        """
        if future_value <= 0 or nominal_rate <= 0 or time <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return (future_value / (((1 + nominal_rate / compounding_frequency) ** (time * compounding_frequency) - 1) / (nominal_rate / compounding_frequency)))

    # Number of Years Annuity (Given PV)
    def number_of_years_annuity_pv(self, present_value, annual_payment, nominal_rate, compounding_frequency=1):
        """
        Calculate the number of years for an annuity given its present value and variable compounding.
        
        Parameters:
        - present_value (float): The present value of the annuity
        - annual_payment (float): The payment received each year
        - nominal_rate (float): The annual interest rate (as a decimal)
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The number of years for the annuity
        """
        if present_value <= 0 or annual_payment <= 0 or nominal_rate <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return ((-math.log(1 - (present_value*(nominal_rate / compounding_frequency))/ annual_payment) / 
                math.log(1 + nominal_rate / compounding_frequency))) * 1/compounding_frequency

    # Number of Years Annuity (Given FV)
    def number_of_years_annuity_fv(self, future_value, annual_payment, nominal_rate, compounding_frequency=1):
        """
        Calculate the number of years for an annuity given its future value and variable compounding.
        
        Parameters:
        - future_value (float): The future value of the annuity
        - annual_payment (float): The payment received each year
        - nominal_rate (float): The annual interest rate (as a decimal)
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The number of years for the annuity
        """
        if future_value <= 0 or annual_payment <= 0 or nominal_rate <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return ((math.log(1 + (future_value * (nominal_rate / compounding_frequency)) / annual_payment) / 
                math.log(1 + nominal_rate / compounding_frequency))) * 1 / compounding_frequency

    # Future Value of an Annuity
    def future_value_annuity(self, annual_payment, nominal_rate, time, compounding_frequency=1):
        """
        Calculate the future value of an annuity with variable compounding.
        
        Parameters:
        - annual_payment (float): The payment received each year
        - nominal_rate (float): The annual interest rate (as a decimal)
        - time (float): The time period in years
        - compounding_frequency (int): Number of compounding periods per year. Default is 1 (annually).
        
        Returns:
        float: The future value of the annuity
        """
        if annual_payment <= 0 or nominal_rate <= 0 or time <= 0 or compounding_frequency <= 0:
            return "Invalid Input: All inputs must be positive and compounding_frequency should be greater than 0"
        
        return annual_payment * (((1 + nominal_rate / compounding_frequency) ** (time * compounding_frequency) - 1) / (nominal_rate / compounding_frequency))


    # Fisher Effect
    def fisher_effect(self, nominal_rate, inflation_rate):
        """
        Calculate the real interest rate using the Fisher Effect.
        
        Parameters:
        - nominal_rate (float): The nominal interest rate (as a decimal)
        - inflation_rate (float): The inflation rate (as a decimal)
        
        Returns:
        float: The real interest rate (as a decimal)
        """
        if nominal_rate < 0 or inflation_rate < 0:
            return "Invalid Input: Both nominal and inflation rates must be non-negative"
        
        return ((1 + nominal_rate) / (1 + inflation_rate)) - 1

    # Dividend Discount Model
    def dividend_discount_model(self, dividend, nominal_rate, growth):
        """
        Calculate the intrinsic value of a stock using the Dividend Discount Model.
        
        Parameters:
        - dividend (float): The dividend payment per share
        - nominal_rate (float): The required rate of return (as a decimal)
        - growth (float): The dividend growth rate (as a decimal)
        
        Returns:
        float: The intrinsic value of the stock
        """
        if dividend < 0 or nominal_rate <= growth:
            return "Invalid Input: Dividend must be non-negative and required rate of return should be greater than growth rate"
        
        return dividend / (nominal_rate - growth)

    # Multi Stage DDM
    def multi_stage_ddm_with_terminal_value(self, dividends, nominal_rate, terminal_value):
        """
        Calculate the intrinsic value of a stock using a Multi-Stage Dividend Discount Model with a terminal value.
        
        Parameters:
        - dividends (list): The dividend payments per share for each year
        - nominal_rate (float): The annual discount rate (as a decimal)
        - terminal_value (float): The estimated stock price at the end of the last year
        
        Returns:
        float: The intrinsic value of the stock
        """
        # Validate inputs
        if nominal_rate <= 0:
            return "Invalid Input: Discount rate must be greater than 0"
        
        if terminal_value <= 0:
            return "Invalid Input: Terminal value must be greater than 0"

        if not all(x >= 0 for x in dividends):
            return "Invalid Input: Dividends must be non-negative"

        intrinsic_value = 0

        for i, dividend in enumerate(dividends):
            intrinsic_value += dividend / ((1 + nominal_rate) ** (i + 1))
        
        intrinsic_value += terminal_value / ((1 + nominal_rate) ** len(dividends))
        
        return intrinsic_value


    # DDM No Growth
    def ddm_no_growth(self, dividend, nominal_rate):
        """
        Calculate the intrinsic value of a stock using the Dividend Discount Model with no growth.
        
        Parameters:
        - dividend (float): The dividend payment per share
        - nominal_rate (float): The required rate of return (as a decimal)
        
        Returns:
        float: The intrinsic value of the stock
        """
        if dividend < 0 or nominal_rate <= 0:
            return "Invalid Input: Both dividend and required rate of return must be non-negative and nominal rate should be greater than 0"
        
        return dividend / nominal_rate

    # DDM Constant Growth
    def ddm_constant_growth(self, dividend, nominal_rate, growth, time):
        """
        Calculate the intrinsic value of a stock using the Dividend Discount Model with constant growth over time.
        
        Parameters:
        - dividend (float): The dividend payment per share
        - nominal_rate (float): The required rate of return (as a decimal)
        - growth (float): The dividend growth rate (as a decimal)
        - time (float): The time period in years
        
        Returns:
        float: The intrinsic value of the stock
        """
        if dividend < 0 or nominal_rate <= growth or time <= 0:
            return "Invalid Input: Dividend and time must be non-negative, and required rate of return should be greater than growth rate"
        
        return (dividend * (1 + growth)**time) / (nominal_rate - growth)

    # Holding Period Return
    def holding_period_return(self, initial_price, final_price, dividend, times_recieved_div):
        """
        Calculate the holding period return for a stock.
        
        Parameters:
        - initial_price (float): The initial price of the stock
        - final_price (float): The final price of the stock
        - dividend (float): The dividend received during the holding period
        
        Returns:
        float: The holding period return (as a decimal)
        """
        if initial_price <= 0 or final_price < 0 or dividend < 0:
            return "Invalid Input: Initial price must be positive, and final price and dividend must be non-negative"
        
        return (final_price - initial_price + dividend*times_recieved_div) / initial_price


class FinanceImplementations:
    def __init__(self, finance_calculations):
        self.finance_calculations = finance_calculations
    
    def main_present_value_single_cashflow(self):
        # Hardcoded values
        future_value = 1000.0
        nominal_rate = 0.05
        time = 2.0
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.present_value_single_cashflow(future_value, nominal_rate, time, compounding_frequency)
        print(f"Present Value: {result}")

    def main_future_value_single_cashflow(self):
        # Hardcoded values
        present_value = 900.0
        nominal_rate = 0.05
        time = 2.0
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.future_value_single_cashflow(present_value, nominal_rate, time, compounding_frequency)
        print(f"Future Value: {result}")

    def main_interest_rate_single_cashflow(self):
        # Hardcoded values
        present_value = 900.0
        future_value = 1000.0
        time = 2.0
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.interest_rate_single_cashflow(present_value, future_value, time, compounding_frequency)
        print(f"Interest Rate: {result}")

    def main_number_of_years_single_cashflow(self):
        # Hardcoded values
        present_value = 900.0
        future_value = 1000.0
        nominal_rate = 0.05
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.number_of_years_single_cashflow(present_value, future_value, nominal_rate, compounding_frequency)
        print(f"Number of Years: {result}")

    def main_effective_annual_rate(self):
        # Hardcoded values
        nominal_rate = 0.05
        compounding_frequency = 4
        
        # Call the function and print the result
        result = self.finance_calculations.effective_annual_rate(nominal_rate, compounding_frequency)
        print(f"Effective Annual Rate: {result}")

    def main_present_value_perpetuity(self):
        # Hardcoded values
        annual_payment = 50.0
        nominal_rate = 0.05
        
        # Call the function and print the result
        result = self.finance_calculations.present_value_perpetuity(annual_payment, nominal_rate)
        print(f"Present Value of Perpetuity: {result}")

    def main_pv_perpetuity_starting_today(self):
        # Hardcoded values
        annual_payment = 50.0
        nominal_rate = 0.05
        
        # Call the function and print the result
        result = self.finance_calculations.pv_perpetuity_starting_today(annual_payment, nominal_rate)
        print(f"Present Value of Perpetuity Starting Today: {result}")

    def main_present_value_annuity(self):
        # Hardcoded values
        annual_payment = 50.0
        nominal_rate = 0.05
        time = 10
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.present_value_annuity(annual_payment, nominal_rate, time, compounding_frequency)
        print(f"Present Value of Annuity: {result}")

    def main_cash_payment_annuity_pv(self):
        # Hardcoded values
        present_value = 400.0
        nominal_rate = 0.05
        time = 10
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.cash_payment_annuity_pv(present_value, nominal_rate, time, compounding_frequency)
        print(f"Cash Payment of Annuity Given PV: {result}")

    def main_cash_payment_annuity_fv(self):
        # Hardcoded values
        future_value = 500.0
        nominal_rate = 0.05
        time = 10
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.cash_payment_annuity_fv(future_value, nominal_rate, time, compounding_frequency)
        print(f"Cash Payment of Annuity Given FV: {result}")


    def main_number_of_years_annuity_pv(self):
        # Hardcoded values
        present_value = 400.0
        annual_payment = 50.0
        nominal_rate = 0.05
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.number_of_years_annuity_pv(annual_payment, present_value, nominal_rate, compounding_frequency)
        print(f"Number of Years for Annuity Given PV: {result}")

    def main_number_of_years_annuity_fv(self):
        # Hardcoded values
        future_value = 500.0
        annual_payment = 50.0
        nominal_rate = 0.05
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.number_of_years_annuity_fv(annual_payment, future_value, nominal_rate, compounding_frequency)
        print(f"Number of Years for Annuity Given FV: {result}")

    def main_future_value_annuity(self):
        # Hardcoded values
        annual_payment = 50.0
        nominal_rate = 0.05
        time = 10
        compounding_frequency = 1
        
        # Call the function and print the result
        result = self.finance_calculations.future_value_annuity(annual_payment, nominal_rate, time, compounding_frequency)
        print(f"Future Value of Annuity: {result}")

    def main_fisher_effect(self):
        # Hardcoded values
        nominal_rate = 0.07
        inflation_rate = 0.02
        
        # Call the function and print the result
        result = self.finance_calculations.fisher_effect(nominal_rate, inflation_rate)
        print(f"Real Interest Rate (Fisher Effect): {result}")

    def main_dividend_discount_model(self):
        # Hardcoded values
        dividend = 1.0
        nominal_rate = 0.08
        growth_rate = 0.02
        
        # Call the function and print the result
        result = self.finance_calculations.dividend_discount_model(dividend, nominal_rate, growth_rate)
        print(f"Intrinsic Value (Dividend Discount Model): {result}")

    def main_multi_stage_ddm_with_terminal_value(self):
    # Hardcoded values
        dividends = [1.0, 1.05, 1.1]  # Dividends for each stage
        nominal_rate = 0.08  # Discount rate
        terminal_value = 50.0  # Terminal value at the end of the multi-stage period
    
    # Call the function and print the result
        result = self.finance_calculations.multi_stage_ddm_with_terminal_value(dividends, nominal_rate, terminal_value)
        print(f"Intrinsic Value (Multi-Stage DDM with Terminal Value): {result}")


    def main_ddm_no_growth(self):
        # Hardcoded values
        dividend = 1.0
        nominal_rate = 0.08
        
        # Call the function and print the result
        result = self.finance_calculations.ddm_no_growth(dividend, nominal_rate)
        print(f"Intrinsic Value (DDM No Growth): {result}")

    def main_ddm_constant_growth(self):
        # Hardcoded values
        dividend = 1.0
        nominal_rate = 0.08
        growth = 0.02
        time = 5
        
        # Call the function and print the result
        result = self.finance_calculations.ddm_constant_growth(dividend, nominal_rate, growth, time)
        print(f"Intrinsic Value (DDM Constant Growth): {result}")

    def main_holding_period_return(self):
        # Hardcoded values
        initial_price = 50.0
        final_price = 60.0
        dividend = 2.0
        times_received_div = 1
        
        # Call the function and print the result
        result = self.finance_calculations.holding_period_return(initial_price, final_price, dividend, times_received_div)
        print(f"Holding Period Return: {result}")

if __name__ == "__main__":
    finance_calculations = FinanceCalculations()
    finance_implementations = FinanceImplementations(finance_calculations)
    
    finance_implementations.main_present_value_single_cashflow()
    finance_implementations.main_number_of_years_single_cashflow()
    finance_implementations.main_effective_annual_rate()
    finance_implementations.main_present_value_perpetuity()
    finance_implementations.main_future_value_single_cashflow()
    finance_implementations.main_pv_perpetuity_starting_today()
    finance_implementations.main_present_value_annuity()
    finance_implementations.main_cash_payment_annuity_pv()
    finance_implementations.main_cash_payment_annuity_fv()
    finance_implementations.main_number_of_years_annuity_pv()
    finance_implementations.main_number_of_years_annuity_fv()
    finance_implementations.main_future_value_annuity()
    finance_implementations.main_fisher_effect()
    finance_implementations.main_dividend_discount_model()
    finance_implementations.main_multi_stage_ddm_with_terminal_value()
    finance_implementations.main_ddm_no_growth()
    finance_implementations.main_ddm_constant_growth()
    finance_implementations.main_holding_period_return()
