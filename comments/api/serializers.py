from rest_framework.serializers import (ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField)
from comments.models import Comments

class CommentsSerializer(ModelSerializer):
	class Meta:
		model = Comments
		fields = [
			'id',
			'content_type',
			'object_id',
			'content'
					]
