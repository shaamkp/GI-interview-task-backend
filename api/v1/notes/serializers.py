from rest_framework import serializers

from web.models import Notes


class CreateNotesSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()


class ListNotesSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Notes
        fields = (
            'id',
            'title',
            'body',
            'created_at',
        )

    def get_created_at(self, instance):
        if instance.created_at:
            return instance.created_at.date()
        else:
            return None
