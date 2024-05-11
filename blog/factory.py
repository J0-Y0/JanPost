from django.contrib.auth.models import User
from .models import Post
import factory
from faker import Faker
from taggit.models import Tag


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker("word")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=10)
    excerpt = factory.Faker("sentence", nb_words=10)
    author = factory.SubFactory(UserFactory)
    status = "published"

    @factory.lazy_attribute
    def content(self):
        fake = Faker()
        x = ""
        for _ in range(0, 5):
            x += "\n" + fake.paragraph(nb_sentences=30) + "\n"
        return x

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        fake = Faker()
        if not create:
            return

        try:
            if extracted:
                # If tags were provided, add them to the post
                for tag in extracted:
                    self.tags.add(tag)
            else:
                # If no tags were provided, create and add a random number of tags
                num_tags = fake.random_int(min=1, max=5)
                for _ in range(num_tags):
                    self.tags.add(TagFactory())
        except Exception as e:
            # Handle the IntegrityError, e.g., log the error
            print(f"IntegrityError: {e}")
