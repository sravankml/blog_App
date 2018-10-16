from rest_framework.generics import (ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from comments.models import Comments
from bored.api.permisions import IsOwnerOrReadOnly
from bored.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .serializers import CommentsSerializer

# class ContentsCreateAPIView(CreateAPIView):
# 	queryset = Contents.objects.all()
# 	serializer_class = ContentsCreateUpdateSerializer
# 	permisson_classes = [IsOwnerOrReadOnly,IsAuthenticated]

# 	def perform_create(self,serializer):
# 		serializer.save(user_name=self.request.user)
class ContentsListAPIView(ListAPIView):
	queryset = Comments.objects.all()
	serializer_class = CommentsSerializer
	filter_backends= [SearchFilter, OrderingFilter]
	search_fields = ['user_name']
	pagination_class = PostLimitOffsetPagination 
class ContentsDetailsAPIView(RetrieveAPIView):
	queryset = Comments.objects.all()
	serializer_class = CommentsSerializer
	# lookup_field = 'pk'
# class ContentsDeleteAPIView(DestroyAPIView):
# 	queryset = Contents.objects.all()
# 	serializer_class = ContentsDetailSerializer
# 	lookup_field = 'pk'
# class ContentsUpdateAPIView(RetrieveUpdateAPIView):
# 	queryset = Contents.objects.all()
# 	serializer_class = ContentsCreateUpdateSerializer
# 	lookup_field = 'pk'
# 	permission_classes = [IsOwnerOrReadOnly]
# 	def perform_update(self,serializer):
# 		serializer.save(user=self.request.user)

