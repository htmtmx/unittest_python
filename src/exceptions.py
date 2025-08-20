class InsufficientFundsError(Exception):
    pass


class WithdrawalOutsideBusinessHoursError(Exception):
    pass


class WithdrawalOutsideBusinessDaysError(Exception):
    pass
