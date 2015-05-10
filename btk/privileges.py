__author__ = 'jkonieczny'


def can_manage_title(user):
    if user.is_staff:
        return True


def can_loan_book(user):
    if user.is_staff:
        return True
