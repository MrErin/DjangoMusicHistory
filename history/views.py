from django.shortcuts import render


class ArtistView(View):
    def get(self, request):
        return HttpResponse('GET request!')

    def post(self, request):
        return HttpResponse('POST request!')
