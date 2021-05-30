from rest_framework import serializers
from tvmserver.utils import assume_role


class CrecentialSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        command = instance["command"]
        account = instance["account"]
        credentials = assume_role(policy_document=command.document, account=account)
        return credentials
