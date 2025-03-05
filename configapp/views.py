from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import qrcode
from reportlab.lib.utils import ImageReader
from io import BytesIO
from reportlab.lib.pagesizes import A4


def index(request):
    kurs = Kurs.objects.all()
    student = Student.objects.all()
    context = {
        'kurs': kurs,
        'student': student,

    }
    return render(request, 'index.html', context=context)


def kursinfo(request, kurs_id):
    student = Student.objects.filter(pk=kurs_id)
    kurs = Kurs.objects.all()
    context = {
        'kurs': kurs,
        'student': student,
    }
    return render(request, 'kursinfo.html', context=context)


def student(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {
        'student': student,

    }

    return render(request, 'student.html', context=context)


def add_kurs(request):
    if request.method == 'POST':
        form = AddKurs(request.POST, request.FILES)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            kurs = form.save()
            return redirect('home')

    else:
        form = AddKurs()
    return render(request, 'add_kurs.html', context={'form': form})


def add_student(request):
    if request.method == 'POST':
        form = AddStudent(request.POST, request.FILES)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            student = form.save()
            return redirect('home')

    else:
        form = AddStudent()
    return render(request, 'add_student.html', context={'form': form})


def download_student_pdf(request, student_id):
    # 1. Talabani bazadan olish
    student = get_object_or_404(Student, id=student_id)

    # 2. PDF uchun javob obyektini yaratish
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_{student.sur_name}.pdf"'

    # 3. ReportLab canvas obyektini yaratish
    p = canvas.Canvas(response, pagesize=A4)  # A4 formatdagi sahifa
    width, height = A4  # Sahifaning kengligi va balandligi
    p.setFont("Times-Roman", 28)

    # 4. Sarlavha qo'shish
    p.drawString(100, height - 50, "Talaba ma'lumotlari")
    p.setFont("Times-Roman", 24)

    # 5. Talaba ma'lumotlarini qo'shish
    p.drawString(100, height - 80, f"Ism: {student.name}")
    p.drawString(100, height - 100, f"Familiya: {student.sur_name}")
    p.drawString(100, height - 120, f"Yosh: {student.age}")
    p.drawString(100, height - 140, f"Telefon: {student.phone}")
    p.drawString(100, height - 160, f"Email: {student.email}")

    # 6. QR kod uchun URL
    qr_data = "https://t.me/najottalim"

    # 7. QR kod yaratish
    qr = qrcode.make(qr_data)

    # 8. QR kodni xotirada saqlash
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_io.seek(0)

    # 9. QR kodni PDF'ga joylash
    qr_img = ImageReader(qr_io)
    qr_size = 100  # QR kodning eni va bo'yi
    qr_x = width - qr_size - 20  # O‘ng chekka koordinatasi
    qr_y = 20  # Pastki chekka koordinatasi

    p.drawImage(qr_img, qr_x, qr_y, width=qr_size, height=qr_size)

    # 10. PDF ni yakunlash
    p.showPage()
    p.save()

    return response

def del_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('index')

def update_new(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = NewForm(request.POST, instance=student)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form = NewForm(instance=student)
    return render(request, 'update.html', context={'form': form, 'student': student})

