from deveops.utils import sshkey, aes
from django.core.exceptions import ValidationError


def private_key_validator(key):
    if not sshkey.private_key_validator(key):
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': key},
        )


def public_key_validator(key):
    if not sshkey.public_key_validator(key):
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': key},
        )
