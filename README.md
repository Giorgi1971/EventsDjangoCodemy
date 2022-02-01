# EventsDjangoCodemy

This is Events App from codemy wensday (Youtube)
<br />
> ## codemy wednesday (YouTube-ს არხი)

### Django-ს ვიდეო გაკვეთილები event-ს შექმნაზე

საიტის სანახავად უნდა გქონდეთ პითონის მე-3 ვერსია.
ასევე requirements.txt -ში მოთავსებული მოდულები.
სასურველია ეს ყოველივე დააყენოთ ვირტუალურ გარემოში.
გამოსაყენებელი ბრძანებები, რომლებიც აქედან შეიძლება გავიხსენო:
* python3 -m venv env (ვირტუალური გარემოს შექმნა) 
* python3 -m venv env (ლინუქსა ან მაკ ზე)
* pip freeze > requirements.txt (მოდულების ჩამონათვალის შექმნა)
* pip install pipreqs
* .\env\Scripts\activate (ვირტუალური გარემოს აქტივიზაცია ვინდოუსში)
* source env/bin/activate (აქტივიზაცია ლინუქსა ან მაკ ზე)
* python -m pip install Django (ჯანგოს დაყენება)
* https://github.com/ddatunashvili/flask_auto_association?fbclid=IwAR21fetsaMelgYAlg16uIRvEK3GcDgmVVu_hLgdV4_b4E-smPXgpGvynyPs#start-of-content

> ## ლექციების დროს ჩემთვის ახალი ან საინტერესო შენიშვნები:
* ამ პროექტში გვაქვს საიტის მონაცემების შენახვა .txt .pdf ან .csv (ექსელის ფაილი) ფორმატში
* venue_list = Venue.objects.all().order_by('?') - აბრუნებს ყოველ ჯერზე ახალ მიმდევრობას
*     if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()


