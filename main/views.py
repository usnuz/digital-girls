from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def slider(request):
    slider = Slider.objects.last()
    return Response(SliderSerializer(slider).data)


@api_view(['GET'])
def about(request):
    all_about = About.objects.all().order_by('-id')
    return Response(AboutSerializer(all_about, many=True).data)


@api_view(['GET'])
def direction(request):
    all_direction = Direction.objects.all().order_by('-id')
    return Response(DirectionSerializer(all_direction, many=True).data)


@api_view(['GET'])
def task(request):
    all_task = Task.objects.all().order_by('-id')
    return Response(TaskSerializer(all_task, many=True).data)


@api_view(['GET'])
def results(request):
    all_result = Result.objects.all().order_by('-id')
    r.item.all()
    return Response(ResultSerializer(all_result, many=True).data)


@api_view(['GET'])
def result_items(request, pk):
    result = Result.objects.get(pk=pk)
    return Response(ResultSerializer(result).data)


# @api_view(['POST'])
# def registration(request):
#     first_name = request.POST.get('first-name')
#     last_name = request.POST.get('last-name')
#     birthday = request.POST.get('birthday')
#     mail = request.POST.get('e-mail')
#     address = request.POST.get('address')
#     tel = request.POST.get('tel')
#     new_registration = Registration.objects.create(
#         first_name
#         last_name
#         birthday
#         mail
#         address
#         tel
#         date_created
#     )


