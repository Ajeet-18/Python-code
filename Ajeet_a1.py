'''module for currency exchange
this module provides several string parsing functions to impliment a
simple currency exchange routine using an online currency service.
the primary function in this module is exchange.
Author: Ajeet kumar
Date: Nov,26,2022
'''

def before_space(s):
    '''Returns a copy of s up to,but not including, the first space

    Example:
    >>> before_space('5.432 INR')
    '5.432'
    >>> before_space('5.695 USD')
    '5.695'

    parameter s: the string to slice
    precondition: s is a string with at least one space'''

    end_last=s.find(' ')
    before=s[:end_last]
    return before


def after_space(s):
    '''returns a copy of s after the first space 

    example:
    >>> after_space('5.432 INR')
    'INR'
    >>> after_space('5.695 USD')
    'USD'

    parameter s: the string to slice
    precondition: s is a string with at least one space''' 

    end_last=s.find(' ')
    after=s[:end_last]
    return after


def first_inside_quotes(s):
    '''Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that delimit it.
    we typically use single quotes (') to delimit a string if we want to use 
    a double quotes character (") inside of it.

    example:
    >>> first_inside_quotes('A "B C" D')
    'B C'
    >>> first_inside_quotes('A "B C" D "E F" G ')
    'B C'

    because it only picks the first such substring

    parameter s: a string to search
    precondition: s is a string containing at least two double quotes'''
    quote1=s.index('"')
    quote2=s.index('"',quote1+2)
    char=s[quote1+2:quote2]
    return char
if __name__=='__main__':
    import doctest
    doctest.testmod()
    

def get_lhs(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the string 
    inside double quotes (") immediately following the keyword
    "lhs".for example, if the JSON is
    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
    This function returns the empty string if the JSON response
    contains an error message.
    parameter json: a json string to parse
    precondition: json is the response to a currency query

    Example:
    >>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" :"19995.85429186 Euros", "err" : "" }')
    '1 Bitcoin'
    '''

    start=json.index(':')
    end=json.index('"',start+3)
    lhs=json[start+3:end]
    return lhs


def get_rhs(json):
    '''Returns the rhs value in the response to a currency query

    given a JSON response to a currency query, this returns the string 
    inside double quotes (")immediately following the 
    keyword 
    "rhs". For example, if the JSON is '{ "lhs" : "1 bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    then this function returns the empty string if the JSON respone contains an error massage.
    parameter json: a json string to parse
    precondition: json is the response to a currency quer

    Example:
    >>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : ""}')
    '19995.85429186 Euros'
    '''
    return json[json.find(',')+11:json.find(',',json.find(',')+9)-1]



def has_error(json):
    '''Returns True if the query has an error; otherwise False.

    Given a JSON response to a currency query, this returns True  if there  
    is an error massage.
    For example,
    if the JSON is '{"lhs" : "", "rhs" :"", "err" : "currency amount is invalid." }'
    then the query is not valid, so this function returns True (it does NOT returns the message 'currency amount is invalid.')
    parameter json: a json string to parse
    precondition:json is the response to a currency query

    Example:
    >>> has_error('{ "lhs":"2 Namibian Dollars", "rhs":"2 lesotho maloti",}')
    False
    >>> has_error('{ "lhs" : "", "rhs" : "", "err" : "currency amount is invalid." }')
    True
    '''
    start=json.index('"')
    end=json.index('"',start+27)
    err=json[start+27:end]
    return len(err)>1



def query_website(old,new,amt):

    '''Returns a JSON string that is a respones to a currency query.

    A currency query converts amt money in currency old to the currency new.
    The resonse should be a string of the form 
    '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
    where the values old-amount and new-amount contain the value and 
    name for the old-amount and new-amount will be empty, while "err" will have an error message.
    parameter old: the currency on hand
    precondition: old is a string with no spaces or non-letters
    parameter new: the currency to convert to 
    precondition: new is a string with no space or non letters
    parameter amt: amount of currency to convert
    precondition: amt is a float
    '''
    import requests
    json=requests.get(f'http://cs1110.cs.cornell.edu/2022fa/a1?old={old}&new={new}&amt={amt}').text
    return json
def is_currency(code):
    '''
    Returns: True if code is a valid (3 latter code for a) currency it returns False otherwise True
    parameter code: the currency code to verify
    precondition: code is a string with no spaaces or non-letters.'''
    amt=1.0
    return not(has_error(query_website(code,code,amt)))==False


def exchange(old,new,amt):
    '''Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency old to the currency new.
    The value returned represents the amount is currency new.
    The value returned has type float.
    parameter old: the currency on hand
    precondition: old is a string for a valid currency coad
    parameter new: the currency to convert to
    precondition: new is a string for a valid currency coad
    parameter amt: amountof currency to convert
    precondition: amt is float'''

    return before_space(get_rhs(query_website(old,new,amt)))
