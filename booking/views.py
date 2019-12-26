from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotels, Reservations, Guests, Rooms, Employees
from django.template import loader
from datetime import date
from .forms import ReservationForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db import models



def index(request):
    qt = Reservations.objects.all()

    template = loader.get_template('booking/home.html')
    context = {
        'reservations': qt,
    }
    return HttpResponse(template.render(context, request))

def hotels(request):
    hotels = []
    for hotel in Hotels.objects.all():
        hotels.append(hotel.name + "," + str(hotel.stars) + " stars, in "+ hotel.location)


    template = loader.get_template('booking/hotels.html')
    context = {
        'hotels': hotels,
    }
    return HttpResponse(template.render(context, request))

def locations(request):
    hotelList = []
    for hotel in Hotels.objects.all():
        hotel1 = hotel.location
        if hotel1 not in hotelList:
            hotelList.append(hotel1)

    template = loader.get_template('booking/locations.html')
    context = {
        'hotelList': hotelList,
    }
    return HttpResponse(template.render(context, request))

def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservations, pk=pk)
    if request.method == "POST":

        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            guests = Guests(reservation.reservationid, reservation.firstname, reservation.lastname)
            count = 0
            roomsTaken = []
            for room in Rooms.objects.all():
                if room.reservation.hotel_hotelid == reservation.hotel_hotelid:
                    count += 1
                    roomsTaken.append(room.number)
            occupancy = reservation.hotel_hotelid.numofrooms
            roomspicked= []
            #return HttpResponse(str(occupancy)+ " "+str(len(roomsTaken))  )
            rooms = int(form['rooms'].value())
            if occupancy  - len(roomsTaken) > 0:
                for checkroom in range(1, occupancy+1):
                    if checkroom not in roomsTaken :
                        roomspicked.append(checkroom)
                        if rooms == len(roomspicked):
                            break
            else:
                return HttpResponse("There are not enough rooms #1")

            if len(roomspicked) == rooms:
                reservation.save()
                Guests(reservation.reservationid, reservation.firstname, reservation.lastname).save()
                
                for aroom in roomspicked:
                    Rooms(aroom, reservation.startdate, Employees.objects.get().ssn, reservation.reservationid ).save()
            else:
                return HttpResponse("There are not enough rooms #2")

            return redirect('reservation_detail', pk=reservation.reservationid)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'booking/reservation_edit.html', {'form': form})

def reservation_detail(request, pk):
    reservation_query = Reservations.objects.get(reservationid=pk)

    hotel_id = reservation_query.hotel_hotelid

    reservation_dict = {
        'reservationid': pk,
        'firstname': reservation_query.firstname,
        'lastname': reservation_query.lastname,
        'startdate':reservation_query.startdate,
        'enddate': reservation_query.enddate,
        'creditcard': reservation_query.creditcardnum,
        'hotel':  hotel_id.name,
        'city': hotel_id.location,
    }


    return render(request,'booking/reservation_detail.html',reservation_dict)

def reservation_new(request, city=None):

    if request.method == "POST":
        form = ReservationForm(request.POST)


        if form.is_valid():
            #retrive data from the html form
            reservation = form.save(commit=False)
            guests = Guests(reservation.reservationid, reservation.firstname, reservation.lastname)
            count = 0
            roomsTaken = []
            allRooms = Rooms.objects.all()
            #get all the rooms
            if allRooms.exists():
                #get all the rooms taken from that hotel
                for room in allRooms:
                    if room.reservation.hotel_hotelid == reservation.hotel_hotelid:
                        count += 1
                        roomsTaken.append(room.number)
            #how many rooms the hotel has to offer
            occupancy = int(reservation.hotel_hotelid.numofrooms)
            #the rooms picked for the reservation
            roomspicked= []
            #return HttpResponse(str(occupancy)+ " "+str(len(roomsTaken))  )
            #the number of rooms needed
            rooms = int(form['rooms'].value())
            #check if there are enough rooms available
            if occupancy  - len(roomsTaken) > 0:
                #check every rooms available
                for checkroom in range(1, occupancy+1):
                    #if room is free then add it to the reservation
                    if checkroom not in roomsTaken :
                        roomspicked.append(checkroom)
                        if rooms == len(roomspicked):
                            break
            else:
                return HttpResponse("There are not enough rooms #1")

            if len(roomspicked) == rooms:
                reservation.save()
                Guests(reservation.reservationid, reservation.firstname, reservation.lastname).save()
                
                for aroom in roomspicked:
                    #reservation.startdate
                    Rooms(number= aroom, day=reservation.startdate, employees_ssn=Employees.objects.get(ssn='123-12-1234' ), reservation=reservation ).save()
            else:
                return HttpResponse("There are not enough rooms #2")

            return redirect('reservation_detail', pk=reservation.reservationid)
    else:
        form = ReservationForm()
    if city != None:
        form['hotel_hotelid'].queryset =  Hotels.objects.filter(location=city)
            
    return render(request, 'booking/reservation_edit.html', {'form': form})
#cancels reservation
def reservation_cancel(request, pk):
    Rooms.objects.filter(reservation= pk).delete()
    Guests.objects.filter(reservationid= pk).delete()
    Reservations.objects.filter(reservationid= pk).delete()
    return index(request)

def employee_details(request):
    workers = Employees.objects.all()

    template = loader.get_template('booking/employee_detail.html')
    allEmp = {
        'employees':workers,
    }
    return HttpResponse(template.render(request, allEmp))


