from rettiwt.models import Post


def test_post_model_save():
    p = Post()
    p.save()

    assert p == Post.objects.first()
