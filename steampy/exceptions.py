class SevenDaysHoldException(Exception):
    pass


class TooManyRequests(Exception):
    pass


class ApiException(Exception):
    def __init__(self, error_code):
        self.error_code = error_code
        self.error_message = {
            3: "Lost connection",
            8: "Incorrect parameter",
            15: "Access denied. Are you allowed to use market?",
            20: "Service unavailable. The requested service is currently unavailable.",
            25: "Limit exceeded. Too much of a good thing.",
            29: "Duplicate request. The action has already occurred in the past, ignored this time.",
            40: "Blocked. Action blocked due to the rate limit.",
            42: "No Match. Nothing matching the request.",
            84: "RateLimitExceeded. Temporary rate limit exceeded, try again later."
        }

    def __str__(self):
        return self.error_message.get(self.error_code, f"success: {self.error_code}")


class LoginRequired(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class CaptchaRequired(Exception):
    pass


class ConfirmationExpected(Exception):
    pass


class ProxyConnectionError(Exception):
    pass
