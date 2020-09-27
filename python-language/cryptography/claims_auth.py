import jwt

data = {'payload': 'data', 'iss': 'rodrigoazevedo.com', 'aud': 'dojo-python'}
secret = 'secret-key'
token = jwt.encode(data, secret)

def decode(token, secret, issuer=None, audience=None):
    try:
        print(jwt.decode(
            token, secret, issuer=issuer, audience=audience))
    except (
        jwt.InvalidIssuerError, jwt.InvalidAudienceError
    ) as err:
        print(err)
        print(type(err))
        
decode(token, secret)
# not providing the issuer
decode(token, secret, audience='dojo-python')
# not providing the audience
decode(token, secret, issuer='rodrigoazevedo.com')
# both
decode(token, secret, issuer='wrong', audience='dojo-python')
decode(token, secret, issuer='rodrigoazevedo.com', audience='wrong')

decode(token, secret, issuer='rodrigoazevedo.com', audience='dojo-python')