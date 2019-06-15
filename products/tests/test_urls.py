from django.urls import reverse,resolve
# from django.urls import reverse

class TestUrls:
    def test_deatail_url(self):
        path=reverse('detail',kwargs={'pk':1})
        assert resolve(path).view_name=='detail'