from pydantic import BaseModel


class InputData(BaseModel):
    limit_bal: int
    sex: int
    education: int
    marriage: int
    age: int
    pay_0: int
    pay_2: int
    pay_3: int
    pay_4: int
    pay_5: int
    pay_6: int
    bill_amt1: int
    bill_amt2: int
    bill_amt3: int
    bill_amt4: int
    bill_amt5: int
    bill_amt6: int
    pay_amt1: int
    pay_amt2: int
    pay_amt3: int
    pay_amt4: int
    pay_amt5: int
    pay_amt6: int


class OutputData(BaseModel):
    next_month_default: bool