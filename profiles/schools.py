from .data.school_vectors import school_vectors

SCHOOL_DEFAULT_SCORE = 30

class School:
    def __init__(self, school_name):
        self.school_name = school_name.lower()
    
    def to_vector(self):
        return [school_vectors.get(self.school_name, SCHOOL_DEFAULT_SCORE) / 100]