from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from .models import Guest, Room, Booking
from xml.dom.minidom import Document, parse
import os

def show_tables(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    bookings = Booking.objects.all()
    return render(request, 'show_tables.html',{
        'guests': guests,
        'rooms': rooms,
        'bookings': bookings,
    })


def export_to_xml(request):
    doc = Document()
    root = doc.createElement("hotel")
    doc.appendChild(root)

    # Guests
    guests_node = doc.createElement("guests")
    root.appendChild(guests_node)
    for guest in Guest.objects.all():
        guest_node = doc.createElement("guest")
        guest_node.setAttribute("id", str(guest.id))
        guests_node.appendChild(guest_node)

        first_name = doc.createElement("first_name")
        first_name.appendChild(doc.createTextNode(guest.first_name))
        guest_node.appendChild(first_name)

        last_name = doc.createElement("last_name")
        last_name.appendChild(doc.createTextNode(guest.last_name))
        guest_node.appendChild(last_name)

    # Rooms
    rooms_node = doc.createElement("rooms")
    root.appendChild(rooms_node)
    for room in Room.objects.all():
        room_node = doc.createElement("room")
        room_node.setAttribute("id", str(room.id))
        rooms_node.appendChild(room_node)

        room_number = doc.createElement("room_number")
        room_number.appendChild(doc.createTextNode(str(room.room_number)))
        room_node.appendChild(room_number)

        room_type = doc.createElement("room_type")
        room_type.appendChild(doc.createTextNode(room.room_type))
        room_node.appendChild(room_type)

    # Bookings
    bookings_node = doc.createElement("bookings")
    root.appendChild(bookings_node)
    for booking in Booking.objects.all():
        booking_node = doc.createElement("booking")
        booking_node.setAttribute("id", str(booking.id))
        bookings_node.appendChild(booking_node)

        guest_id = doc.createElement("guest_id")
        guest_id.appendChild(doc.createTextNode(str(booking.guest.id)))
        booking_node.appendChild(guest_id)

        room_id = doc.createElement("room_id")
        room_id.appendChild(doc.createTextNode(str(booking.room.id)))
        booking_node.appendChild(room_id)

        start_date = doc.createElement("start_date")
        start_date.appendChild(doc.createTextNode(booking.start_date.strftime('%Y-%m-%d')))
        booking_node.appendChild(start_date)

        end_date = doc.createElement("end_date")
        end_date.appendChild(doc.createTextNode(booking.end_date.strftime('%Y-%m-%d')))
        booking_node.appendChild(end_date)

    response = HttpResponse(doc.toprettyxml(indent="  "), content_type="application/xml")
    response['Content-Disposition'] = 'attachment; filename="export_data.xml"'
    return response

# Задание 8: Импорт из XML
def import_from_xml(request):
    # Укажите путь к файлу (замените на свой путь)
    file_path = os.path.join(os.path.dirname(__file__), "import_data.xml")
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)

    doc = parse(file_path)
    hotel = doc.documentElement

    # Guests
    guests = hotel.getElementsByTagName("guest")
    for guest_node in guests:
        guest_id = guest_node.getAttribute("id")
        first_name = guest_node.getElementsByTagName("first_name")[0].firstChild.data
        last_name = guest_node.getElementsByTagName("last_name")[0].firstChild.data
        Guest.objects.update_or_create(id=guest_id, defaults={"first_name": first_name, "last_name": last_name})

    # Rooms
    rooms = hotel.getElementsByTagName("room")
    for room_node in rooms:
        room_id = room_node.getAttribute("id")
        room_number = int(room_node.getElementsByTagName("room_number")[0].firstChild.data)
        room_type = room_node.getElementsByTagName("room_type")[0].firstChild.data
        Room.objects.update_or_create(id=room_id, defaults={"room_number": room_number, "room_type": room_type})

    return HttpResponse("Data imported successfully")
def home(request):
    return render(request, 'home.html')

def view_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'view_rooms.html', {'rooms': rooms})

def view_guests(request):
    guests = Guest.objects.all()
    return render(request, 'view_guests.html', {'guests': guests})

def add_guest(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        passport = request.POST['passport_number']
        Guest.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone,
            email=email,
            passport_number=passport
        )
        return redirect('home')
    return render(request, 'add_guest.html')

def add_room(request):
    if request.method == 'POST':
        room_number = request.POST['room_number']
        room_type = request.POST['room_type']
        price_per_night = request.POST['price_per_night']
        status = request.POST['status']
        Room.objects.create(
            room_number = room_number,
            room_type = room_type,
            price_per_night = price_per_night,
            status = status
        )
        return redirect('home')
    return render(request, 'add_room.html')