from rest_framework.serializers import (ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField)
from bored.models import Contents
from comments.api.serializers import CommentsSerializer
from comments.models import Comments

class ContentsCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Contents
		fields = [

			'title',
			'timestamp'
					]
class ContentsSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name = 'bored-api:detail',
		lookup_field = 'pk'
		)
	class Meta:
		model = Contents
		fields = [
			'url',
			'user_name',
			'title',
			
			]


class ContentsDetailSerializer(ModelSerializer):
	Discriptions = SerializerMethodField()
	comments = SerializerMethodField()
	class Meta:
		model = Contents
		fields = [
			'pk',
			'user_name',
			'title',
			'Discriptions',
			'timestamp',
			'comments'
			

		]
	def get_Discriptions(self,obj):
		return obj.Discriptions
	def get_comments(self,obj):
		content_type = obj.get_content_type
		object_id = obj.id
		c_qs = Comments.objects.filter_by_instance(obj)
		comments = CommentsSerializer(c_qs,many=True).data
		return comments
	