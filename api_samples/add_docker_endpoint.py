"""
This function will interpolate the api_token taken as an input and then authenticate
to the CAS API. Note that linters will fail on the interpolation syntax used.
:return: Returns an instance of the session class.
:rtype: Session
"""

from caspyr import Session
return Session.login(${input.api_token})
