# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from deveops.utils.sshkey import ssh_keygen
from authority.models import Key


class KeySerializer(serializers.ModelSerializer):
    pub_key = serializers.CharField(max_length=4096, required=False, source='public_key')

    class Meta:
        model = Key
        fields = (
            'id', 'uuid', 'pub_key', 'name', 'group_name', 'fetch_time'
        )
        read_only_fields = (
            'id', 'uuid', 'pub_key', 'group_name', 'fetch_time'
        )

    def create(self, validated_data):
        pri, pub = ssh_keygen()
        validated_data['private_key'] = pri
        validated_data['public_key'] = pub
        return super(KeySerializer, self).create(validated_data)