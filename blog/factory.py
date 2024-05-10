from django.contrib.auth.models import User
from .models import Post
import factory
from faker import Faker


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=10)
    slug = factory.Faker("slug")
    # image
    excerpt = factory.Faker("sentence", nb_words=10)
    author = factory.SubFactory(UserFactory)
    # favorite = User.objects.get_or_create(username="jo")[0]
    status = "published"
    # liked = User.objects.get_or_create(username="jo")[0]
    # content = factory.Faker("paragraph", nb_sentence=500)
    # tags = factory.Faker("word")

    @factory.lazy_attribute
    def content(self):
        fake = Faker()

        x = ""
        for _ in range(0, 5):
            x += "\n" + fake.paragraph(nb_sentences=30) + "\n"
            return x
