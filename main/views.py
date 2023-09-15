from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Joke
from .serializers import JokeSerializer
import random

# Create your views here.
#JokeView API view
class JokeView(APIView):
    def get(self, request):
        category = self.request.query_params.get('category')
        
        if category:
            # Filter jokes by category through endpoint
            queryset = Joke.objects.filter(category=category).values()
            if queryset.exists:
                # Random joke generator
                joke = random.choice(list(queryset))
                serializer = JokeSerializer(joke)
                return Response({'jokes': serializer.data})
            else:
                return Response({"error": "no category found"}, status=404)
        else:
            # Return any joke if category is not specified
            queryset = Joke.objects.all().values()
            if queryset.exists():
                joke = random.choice(queryset)
                serializer = JokeSerializer(joke)
                return Response({'jokes': serializer.data})
            else:
                return Response({'error': 'No jokes found'}, status=404)
            
    def post(self, request):
        post_new = Joke.objects.create(
            content = request.data['content'],
            category= request.data['category']
        )
        
        return Response({'jokes': model_to_dict(post_new)})