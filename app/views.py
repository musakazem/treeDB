from django.shortcuts import render
from .models import MainDb, TypeDb
from django.db.models import Q

# Create your views here.

def showResults(request):

	if(request.method == 'POST'):

	
			searched = request.POST['searched']

			if(searched.find("age:") != -1):

				searched = searched.replace('age:','')
				searched = searched.replace(' ','')
				print("**************", str(searched))

				

				try:
					searched = int(searched)
					objs = MainDb.objects.filter(age = searched)
				except:
					objs = MainDb.objects.filter(age__contains = "نیاز")
					

				return render(request, 'result_page.html', {"objs":objs})

			elif(searched.find("circumference:")!= -1):

				searched = searched.replace('circumference:', '')
				searched = searched.replace(' ','')
				objs = MainDb.objects.filter(trunk_circumference = int(searched))

				return render(request, 'result_page.html', {"objs":objs})


			else:

				lookups = Q(number_plate__icontains = searched)|Q(type_id__category__icontains = searched)
				objs = MainDb.objects.filter(lookups)
					
				
				print("***********", str(objs))

				context = {

					"objs": objs
				}

				return render(request, 'result_page.html', context)

	else:
		return render(request, 'result_page.html')

def search(request):

	return render(request, 'base.html')

def showDetails(request, plate_no):

	plate_no = plate_no.replace("(","")
	plate_no = plate_no.replace(")","")

	print("***************", str(plate_no))
	obj = MainDb.objects.filter(number_plate__icontains = plate_no).first()

	print(obj)

	return render(request, 'detail_page.html', {'obj': obj})
