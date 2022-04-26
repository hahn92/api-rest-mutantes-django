from rest_framework import serializers

# models
from .models import Mutant

class MutantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mutant
        fields = ('id', 'dna', "is_mutant", "created", "modified")
        extra_kwargs = {
            "dna": {"required": True, "allow_blank": False}, 
        }

